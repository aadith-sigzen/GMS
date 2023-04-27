# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters) 
	dance =0
	boxing =0
	yoga =0
	pilates =0
	garba =0
	zumba =0
	lable=["Dance","Boxing","Yoga","Pilates","Garba","Zumba Class"]
	for data1 in data:
		if data1.class_type == "Dance":
			dance+=1
		if data1.class_type == "Boxing":
			boxing+=1
		if data1.class_type == "Yoga":
			yoga+=1
		if data1.class_type == "Pilates":
			pilates+=1
		if data1.class_type == "Garba":
			garba+=1
		if data1.class_type == "Zumba Class":
			zumba+=1
	chart = {
        "type": "bar",
        "data": {
			"labels": lable,
			"datasets": [
				{"values": [dance, boxing, yoga, pilates, garba ,zumba]},	
        	],
        }
    }
	return columns, data, "njcej", chart


def get_columns():
	return[
		"class_type::200",
		"member::200",

	]

def get_data(filters=None):
	doc = frappe.get_all("Group Class",fields=['class_type','member'])
	return doc
