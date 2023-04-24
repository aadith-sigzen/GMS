// Copyright (c) 2023, Aadith and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Member', {
	refresh: function(frm) {
		if(frm.doc.full_name){
			check_user(frm)
		}
	}
});
function check_user(frm) {
	frappe.call({
		method:"gms.gms.doctype.gym_member.gym_member.check_user",
		args:{
			'user_name':frm.doc.full_name,
			'email_id':frm.doc.email
		},
		callback:function(r){
			if(r.message){
				frm.add_custom_button('User', () => {
					create_user(frm)
				  },(' Create '))
			}
		}
	})
}
function create_user(frm) {
	frappe.call({
		method:"gms.gms.doctype.gym_member.gym_member.create_user",
		args:{
			'customer':frm.doc.full_name
		},
		callback:function(r){
			if(r.message){
				frm.reload_doc()
			}
		}
	})

}
