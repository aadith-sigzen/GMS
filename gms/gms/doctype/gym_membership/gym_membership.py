# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class GymMembership(Document):
	def before_save(self):
		if self.durnation == "Monthly":
			self.total_amount = self.rate*1
		elif self.durnation == "Quarterly":
			self.total_amount = self.rate*6
		else:
			self.total_amount = self.rate*12
