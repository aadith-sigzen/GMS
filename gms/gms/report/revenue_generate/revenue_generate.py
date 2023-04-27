# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data


def get_columns():
	return[
		"Member::200",
		"Rate::200",
		"Date::200"

	]
def get_data(filters=None):
		data=[]
		gym_members= frappe.db.get_all('Gym Membership',fields=['gym_member','rate','payment_date'])
		for gym_member in gym_members:
			date= gym_member.payment_date
			if(filters.select_month and filters.select_year):
				if (date.month==int(filters.select_month) and date.year==int(filters.select_year)):
						row={
						"member":gym_member.gym_member,
						"rate":gym_member.rate,
						"date":gym_member.payment_date
						}
						data.append(row)

		return data
