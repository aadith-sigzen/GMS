# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GroupClass(Document):
    def validate(self):
            self.trainer = frappe.db.sql(""" select full_name from `tabGym Trainer` where trainer_category = {}""").format(self.class_type)
	# def validate(self):
	# 	glen=frappe.db.get_list("Group Class")
	# 	if len(glen)>2:
	# 		frappe.throw("Slot is not available")
