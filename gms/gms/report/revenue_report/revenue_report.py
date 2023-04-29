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
		"Total Amount::200",
		"Date::200"

	]
def get_data(filters=None):
		data=[]
		date1=0
		if(filters.select_month== "January"):
			date1=1
		if(filters.select_month== "February"):
			date1=2
		if(filters.select_month== "March"):
			date1=3
		if(filters.select_month== "April"):
			date1=4
		if(filters.select_month== "May"):
			date1=5
		if(filters.select_month== "June"):
			date1=6
		if(filters.select_month== "July"):
			date1=7
		if(filters.select_month== "August"):
			date1=8
		if(filters.select_month== "September"):
			date1=9
		if(filters.select_month== "October"):
			date1=10
		if(filters.select_month== "November"):
			date1=11
		if(filters.select_month== "December"):
			date1=12
		gym_members= frappe.db.get_all('Gym Membership',fields=['gym_member','total_amount','from_date'])
		for gym_member in gym_members:
			date= gym_member.from_date
			if(filters.select_month and filters.select_year):
				if (date.month==date1 and date.year==int(filters.select_year)):
						row={
						"member":gym_member.gym_member,
						"total_amount":gym_member.total_amount,
						"date":gym_member.from_date
						}
						data.append(row)

		return data
