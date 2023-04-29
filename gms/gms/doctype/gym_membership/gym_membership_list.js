frappe.listview_settings['Gym Membership'] = {
    add_fields: ["status"],
    get_indicator: function(doc) {
      if (doc.status === "Active") {
        return [__("Active"), "green", "status,=,Active"];
      }else if (doc.status === "ECL Updated") {
        return [__("Deactive"), "red", "status,=,Deactive"];
      }
  },
  hide_name_column: true,
  }