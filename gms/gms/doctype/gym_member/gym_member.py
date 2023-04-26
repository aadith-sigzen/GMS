# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class GymMember(Document):
	def get_feed(self):
		return self.full_name
	def autoname(self):
		full_name = self.first_name + ' ' + self.last_name
		self.full_name = full_name
		self.name = full_name
	def validate(self):
		full_name = self.first_name + ' ' + self.last_name
		self.full_name = full_name
		self.create_customer()
	def create_customer(self):
		if not frappe.db.exists('Customer',{'customer_name':self.full_name}):
			customer = frappe.new_doc('Customer')
			customer.customer_name = self.full_name
			customer.email_id = self.email
			customer.mobile_no = self.phone
			customer.customer_type = "Individual"
			customer.customer_group = "Individual"
			customer.territory = "India"
			customer.save()
			address_doc = frappe.new_doc('Address')
			address_doc.address_title = self.full_name+"-"+"Billing"
			address_doc.address_type = "Billing"
			address_doc.address_line1 = self.address_line1
			if self.address_line2:
				address_doc.address_line2 = self.address_line2
			address_doc.city = self.city
			address_doc.state = self.state
			address_doc.country = self.country
			address_doc.append('links', {
			'link_doctype': 'Customer',
			'link_name': customer.name
			})
			address_doc.save(ignore_permissions=True)
			frappe.msgprint(_('Customer created for <b>{0}</b>'.format(self.full_name)), alert = 1)

	def compute_age(self):
		if self.date_of_birth:
			self.age = frappe.utils.date_diff(frappe.utils.today(),self.date_of_birth) / 365


@frappe.whitelist()
def check_user(user_name,email_id):
	if not frappe.db.exists('User', {'full_name': user_name,'name':email_id}):
		return True

@frappe.whitelist()
def create_user(customer):
	if frappe.db.exists('Customer', {'name': customer}):
		customer_doc = frappe.get_doc('Customer', {'name': customer})
		user = frappe.get_doc({
		'doctype': 'User',
		'email': customer_doc.email_id,
		'first_name': customer_doc.customer_name,
		'send_welcome_email': 1,
		'enabled': 1,
		'role_profile_name': "Gym Menber",
		'user_type': "Website User",
		})
		user.insert(ignore_permissions = True)
		contact_doc = frappe.get_doc('Contact',{'email_id':customer_doc.email_id})
		contact_doc.append('links', {
		'link_doctype': 'User',
		'link_name': user.name
		})
		contact_doc.save(ignore_permissions=True)
		frappe.msgprint(_('User created for <b>{0}</b>'.format(customer_doc.customer_name)), alert = 1)
		return True
