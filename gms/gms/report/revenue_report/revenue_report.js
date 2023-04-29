// Copyright (c) 2023, Aadith and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Revenue Report"] = {
"filters": [
		{
			"fieldname":"select_month",
			"label":"Select Month",
			"fieldtype":"Select",
			"options":["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		},
		{
			"fieldname":"select_year",
			"label":"SelectYear",
			"fieldtype":"Select",
			"options":[2023,2024]
	
		}

	]
};
	
