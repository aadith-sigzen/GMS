// Copyright (c) 2023, Aadith and contributors
// For license information, please see license.txt

frappe.ui.form.on('Trainer Rating', {
	refresh:function(frm){
		frappe.call({
			method:"gms.gms.doctype.trainer_rating.trainer_rating.select_trainer",
			callback:function(r){
				if(r.message){
					console.log(r);
					frm.set_value("trainer",r.message);
				}
			}
		})
	}
});
