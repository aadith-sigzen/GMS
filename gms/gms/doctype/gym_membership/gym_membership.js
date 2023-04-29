// Copyright (c) 2023, Aadith and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Membership', {
	durnation: function(frm) {
		if(frm.doc.durnation=="1-Month plan"){
			frm.set_value("to_date",frappe.datetime.add_months(frm.doc.from_date,1))
			frm.set_value("total_amount",frm.doc.rate*1)}
		else if(frm.doc.durnation=="3-Month plan") {
			frm.set_value("to_date",frappe.datetime.add_months(frm.doc.from_date,3))
			frm.set_value("total_amount",frm.doc.rate*3)
		}
		else if (frm.doc.durnation=="6-Month plan") {
			frm.set_value("to_date",frappe.datetime.add_months(frm.doc.from_date,3))
			frm.set_value("total_amount",frm.doc.rate*6)
		}
		else if (frm.doc.durnation=="12-Month plan") {
			frm.set_value("to_date",frappe.datetime.add_months(frm.doc.from_date,12))
			frm.set_value("total_amount",frm.doc.rate*12)
		}else{
			frm.set_value("to_date",null)
			frm.set_value("total_amount",0)
		}
	},
	gym_workout_plan: function(frm) {
		if(frm.doc.durnation=="1-Month plan"){
			frm.set_value("total_amount",frm.doc.rate*1)}
		else if(frm.doc.durnation=="3-Month plan") {
			frm.set_value("total_amount",frm.doc.rate*3)
		}
		else if (frm.doc.durnation=="6-Month plan") {
			frm.set_value("total_amount",frm.doc.rate*6)
		}
		else if (frm.doc.durnation=="12-Month plan") {
			frm.set_value("total_amount",frm.doc.rate*12)
		}
		else{
			frm.set_value("total_amount",0)
		}
	}
});
