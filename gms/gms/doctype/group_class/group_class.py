# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GroupClass(Document):
	def validate(self):
		glen=frappe.db.get_list("Group Class")
		if len(glen)>1:
			frappe.throw("Slot is not available")
