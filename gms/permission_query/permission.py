import frappe
import json
from frappe import _
from frappe import get_roles
from frappe.api import get_request_form_data
from frappe.utils import add_months, today, get_fullname, fmt_money, now_datetime
from frappe.utils.pdf import get_pdf
from frappe.utils.user import get_users_with_role
from frappe.email.doctype.notification.notification import get_context
from frappe.utils import add_days, flt, get_datetime, get_time, get_url, nowtime, today

@frappe.whitelist()
def get_permission_query_conditions_for_gym_member(user):
    if not user:
        user = frappe.session.user
    full_name = get_user_name(user)
    user_roles = frappe.get_roles(user)
    if user != 'Administrator' and 'Gym Member' in user_roles:
        conditions = '`tabGym Member`.`name` = "{full_name}"'.format(full_name = full_name)
        return conditions

@frappe.whitelist() 
def get_permission_query_conditions_for_group_class(user):
    if not user:
        user = frappe.session.user
    full_name = get_user_name(user)
    user_roles = frappe.get_roles(user)
    if user != 'Administrator' and 'Gym Member' in user_roles:
        conditions = '`tabGroup Class`.`member` = "{full_name}"'.format(full_name = full_name)
        return conditions
    
@frappe.whitelist() 
def get_permission_query_conditions_for_trainer(user):
    if not user:
        user = frappe.session.user
    full_name = get_user_name(user)
    user_roles = frappe.get_roles(user)
    if user != 'Administrator' and 'Gym Trainer' in user_roles:
        conditions = '`tabGym Trainer`.`name` = "{full_name}"'.format(full_name = full_name)
        return conditions

@frappe.whitelist()
def get_user_name(user):
    if frappe.db.exists('User',{'name':user}):
        user_doc = frappe.get_doc('User',user)
        user_name = user_doc.full_name
        return user_name
