# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	get_columns()
	get_data() 
	return columns, data


def get_columns(filters=None):
	return[
		"",
		"class_type:",
		"select_day",
		"class_time"
	]

def get_data(filters=None):
	data=[]
	