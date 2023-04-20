# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class GymTrainer(Document):
	def get_feed(self):
		return self.full_name
	def autoname(self):
		full_name = self.salutation +' '+ self.first_name + ' ' + self.last_name
		self.full_name = full_name
		self.name = full_name
	def validate(self):
		full_name = self.salutation +' '+ self.first_name + ' ' + self.last_name
		self.full_name = full_name
