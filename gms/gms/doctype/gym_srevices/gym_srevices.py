# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymSrevices(Document):
	def validate(self):
		if self.book_locker==1:

			book_locker = frappe.db.count('Gym Srevices',{'book_locker': 1})
			if book_locker >= frappe.db.get_single_value('Gym Settings', 'locker_limt'):
				frappe.throw("Locker is not avible, please check after some time.")
			else:
				frappe.msgprint(('Your locker is booked successfully.'))
