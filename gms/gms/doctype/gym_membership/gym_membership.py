# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import *
from frappe.model.docstatus import DocStatus
from frappe.utils import date_diff
from frappe.utils import today



class GymMembership(Document):
    def validate(self):
        if frappe.db.exists('Gym Membership', {"gym_member": self.gym_member}) and self.is_new():
            gym_membership = frappe.get_last_doc('Gym Membership', filters={"gym_member": self.gym_member})
            if str(gym_membership.to_date) >= nowdate():
                frappe.throw("You are alredy membership")
            else:	
                frappe.msgprint(('Your changes are saved succefully  '))
    def before_save(self):
        if self.durnation == "Monthly":
            self.total_amount = self.rate*1
            self.to_date= frappe.utils.add_days(self.from_date, 30)
        elif self.durnation == "Quarterly":
            self.total_amount = self.rate*6
            self.to_date= frappe.utils.add_days(self.from_date, 180)
        else:
            self.total_amount = self.rate*12
            self.to_date= frappe.utils.add_days(self.from_date, 365)


