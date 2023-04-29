// Copyright (c) 2023, Aadith and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Calories Progress Report"] = {
	"filters": [{
		"fieldname":"gym_member",
		"label":"Gym Member",
		"fieldtype":"Link",
		"options":"Gym Member"
	},
	{
		"fieldname":"from_date",
		"label":"From Date",
		"fieldtype": "Date",

	},
	{
		"fieldname":"to_date",
		"label":"To Date",
		"fieldtype": "Date",

	}
]
};

