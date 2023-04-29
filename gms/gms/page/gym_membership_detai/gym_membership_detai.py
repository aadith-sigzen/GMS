import json
import frappe
from frappe.utils import cint
from datetime import datetime


@frappe.whitelist()
def get_gym_membership():
    user = get_user_name(frappe.session.user)
    if frappe.db.exists("Gym Membership",{'gym_member':user}):
        gym_membership_doc = frappe.get_last_doc("Gym Membership",{'gym_member':user})
        return gym_membership_doc

@frappe.whitelist()
def get_user_name(user):
    if frappe.db.exists('User',{'name':user}):
        user_doc = frappe.get_doc('User',user)
        user_name = user_doc.full_name
        return user_name