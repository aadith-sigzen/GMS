// Copyright (c) 2023, Aadith and contributors
// For license information, please see license.txt
/* eslint-disable */
frappe.query_reports["Fitness track"] = {
	"filters": [{
		"fieldname":"gym_member",
		"label":"Gym Member",
		"fieldtype":"Link",
		"options":"Gym Member"
	},
	{
		"fieldname":"date",
		"label":"Date",
		"fieldtype": "DateRange",

	}
]
};
