// Copyright (c) 2023, Aadith and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["revenue generate"] = {
	"filters": [
		{
			"fieldname":"select_month",
			"label":"Select Month",
			"fieldtype":"Select",
			"options":[1,2,3,4,5,6,7,8,9,10,11,12]
		},
		{
			"fieldname":"select_year",
			"label":"SelectYear",
			"fieldtype":"Select",
			"options":[2023,2024]
	
		}

	]
};
	