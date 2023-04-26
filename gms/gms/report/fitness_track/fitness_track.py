# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data



def get_columns():
	return [
		"Weight:Float:200",
		"calories:int:200",
		"steps:int:200",
		"date:Date:200"
		
	]



def get_data(filters=None):
	data=[]
	from_date = None
	to_date = None
	if filters.date:
		from_date=datetime.strptime(filters.date[0], '%Y-%m-%d').date()
		to_date=datetime.strptime(filters.date[1], '%Y-%m-%d').date()
	if filters.gym_member:
		print(f'/n/n/n/n/from{type(from_date)}/n/n/n/n')
		doc= frappe.get_doc("Gym Member",filters.gym_member)
		for chi in doc.health_matrix:
			if from_date and to_date:
				if(from_date<=chi.date and to_date>=chi.date):
					row={
					"weight":chi.weight
					,"calories":chi.calories
                	,"steps":chi.steps
					,"date":chi.date
					}
					data.append(row)
			else:
				row={
					"weight":chi.weight
					,"calories":chi.calories
                	,"steps":chi.steps
					,"date":chi.date
					}
				data.append(row)
	return data