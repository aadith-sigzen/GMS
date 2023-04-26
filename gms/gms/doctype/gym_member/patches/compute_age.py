from __future__ import unicode_literals
import frappe

def execute():
    for member in frappe.db.get_all('Gym Member', pluck='name'):
        doc = frappe.get_doc('Gym Member', member)
        doc.compute_age()
        doc.save()