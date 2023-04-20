// Copyright (c) 2023, Aadith and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Member', {
	validate:function(frm){
		var full_name = frm.doc.first_name + ' ' + frm.doc.last_name
		frm.set_value('full_name',full_name)
	}
	// refresh: function(frm) {

	// }
});
