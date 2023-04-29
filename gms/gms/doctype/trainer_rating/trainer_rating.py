# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TrainerRating(Document):
    # def before_save(self):
    #     if self.trainer == None:
    #         frappe.throw("You have not assign trainer")
	pass
    



@frappe.whitelist()
def select_trainer():
    user = frappe.get_doc("User", frappe.session.user)
    tnm=frappe.db.get_value("Gym Membership",{"gym_member": user.full_name},"gym_trainer")
    return tnm

