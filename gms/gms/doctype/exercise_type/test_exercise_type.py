# Copyright (c) 2023, Aadith and Contributors
# See license.txt

import frappe
import unittest
from frappe.tests.utils import FrappeTestCase


class TestExerciseType(unittest.TestCase):
    def test_case1(self):
        frappe.set_user("Administrator")
        doc = frappe.get_doc({
             "doctype": "Exercise Type",
             "exercise_type" :"TEST2"
             }).insert()




