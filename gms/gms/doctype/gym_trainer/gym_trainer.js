// Copyright (c) 2023, Aadith and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Trainer', {
	refresh: function(frm) {
		if(frm.doc.full_name){
			check_user(frm)
		}
	},
	dob:function(frm){
		var today = new Date(); 
		// this is how you get data from form
		var birthDate = new Date(frm.doc.dob); 
		var age = today.getFullYear() - birthDate.getFullYear(); var m = today.getMonth() - birthDate.getMonth(); 
		if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) { 
		  age--; 
		}
		// use frm.set_value to set value of a field
		frm.set_value('age', age);
	}
});
function check_user(frm) {
	frappe.call({
		method:"gms.gms.doctype.gym_trainer.gym_trainer.check_user",
		args:{
			'user_name':frm.doc.full_name,
			'email_id':frm.doc.email
		},
		callback:function(r){
			if(r.message){
				frm.add_custom_button('Create User', () => {
					create_user(frm)
					frappe.msgprint("User created successfully")
				  },)
			}
		}
	})
}
function create_user(frm) {
	frappe.call({
		method:"gms.gms.doctype.gym_trainer.gym_trainer.create_user",
		args:{
			'user_name':frm.doc.full_name,
			'email_id':frm.doc.email
		},
		callback:function(r){
			if(r.message){
				frm.reload_doc()
			}
		}
	})
}