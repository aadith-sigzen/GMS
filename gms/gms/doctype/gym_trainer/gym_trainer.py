# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class GymTrainer(Document):
	def get_feed(self):
		return self.full_name
	def autoname(self):
		full_name = self.salutation + ' ' + self.first_name + ' ' + self.last_name
		self.full_name = full_name
		self.name = full_name
	def validate(self):
		full_name = self.salutation + ' ' + self.first_name + ' ' + self.last_name
		self.full_name = full_name

@frappe.whitelist()
def check_user(user_name,email_id):
	if not frappe.db.exists('User', {'full_name': user_name,'name':email_id}):
		return True

@frappe.whitelist()
def create_user(user_name,email_id):
	if not frappe.db.exists('User', {'name': user_name}):
		user = frappe.get_doc({
		'doctype': 'User',
		'email': email_id,
		'first_name': user_name,
		'send_welcome_email': 1,
		'enabled': 1,
		'role_profile_name': "Gym Trainer",
		'user_type': "System User",
		})
		user.insert(ignore_permissions = True)
		frappe.msgprint(_('User created for <b>{0}</b>'.format(user_name)), alert = 1)
		return True