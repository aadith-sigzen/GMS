# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data



def get_columns(filters=None):
	return[
		"member:FieldName",
		"class_type:",
		"select_day",
		"class_time"
	]

def get_data(filters=None):
	data=[]
	if frappe.session.user != "Administrator":
		user = frappe.get_doc("User", frappe.session.user)
		data = frappe.get_all("Group Class",filters={'member':user.full_name},fields=["member","class_type","select_day","class_time"])
		return data
	else:
		if filters.full_name:
			data = frappe.get_all("Group Class",filters={'member':filters.full_name},fields=["member","class_type","select_day","class_time"])
		else:
			data = frappe.get_all("Group Class",filters={},fields=["member","class_type","select_day","class_time"])
		return data
	
