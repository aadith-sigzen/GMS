import frappe
from frappe import _
from frappe.utils import date_diff
from frappe.utils import today


no_cache = True

def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)
    user = frappe.get_doc("User", frappe.session.user)
    context.tasks = frappe.get_all('Gym Membership',filters={'gym_member':user.full_name},fields=["gym_workout_plan","to_date","gym_trainer","gym_member"])
    for ta in context.tasks:
        ta["days"] = date_diff(ta.to_date,today())
        # ta["num"] = frappe.db.sql("""select phone from `tabGym Trainer` where full_name = 'ta.gym_trainer' """)
        ta["num"] = frappe.db.get_value("Gym Trainer",ta.gym_trainer,"phone")
        ta["plan"] = frappe.db.get_list("Gym Membership",filters={"gym_member":ta.gym_member},pluck="name")
    context.show_sidebar = True
        # context.tsk = frappe.db.sql("""select phone_number from `tabGym Trainer` where full_name = 'ta.gym_trainer' """)
    