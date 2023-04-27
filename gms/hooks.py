from . import __version__ as app_version

app_name = "gms"
app_title = "Gms"
app_publisher = "Aadith"
app_description = "Gym Management Systeam"
app_email = "aadith.p@sigzen@123#"
app_license = "MIT"
from route import routes
# Includes in <head>
# ------------------
website_route_rules = routes

# include js, css files in header of desk.html
# app_include_css = "/assets/gms/css/gms.css"
# app_include_js = "/assets/gms/js/gms.js"

# include js, css files in header of web template
# web_include_css = "/assets/gms/css/gms.css"
# web_include_js = "/assets/gms/js/gms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "gms.utils.jinja_methods",
#	"filters": "gms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "gms.install.before_install"
# after_install = "gms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gms.uninstall.before_uninstall"
# after_uninstall = "gms.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Gym Member": "gms.permission_query.permission.get_permission_query_conditions_for_gym_member",
    "Group Class":"gms.permission_query.permission.get_permission_query_conditions_for_group_class"
}
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"gms.tasks.all"
# 	],
# 	"daily": [
# 		"gms.tasks.daily"
# 	],
# 	"hourly": [
# 		"gms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gms.tasks.weekly"
# 	],
# 	"monthly": [
# 		"gms.tasks.monthly"
# 	],
# }

# Testing
# -------
fixtures = [{"dt": "Role","filters":[["name", "in", ["Gym Member","Gym Trainer","Gym Admin"]]]},
            {"dt":"Role Profile","filters":[["name","in",["Gym Menber","Gym Trainer"]]]},
            {"dt":"Web Page"}, {"dt":"Website Slideshow"} ,  {"dt":"Website Settings"},
            {"dt":"Homepage"},{"dt":"Web Page"}, {"dt":"Website Slideshow"},
            {"dt":"Website Settings"},{"dt": "Gym Workout Plan"}] 


# before_tests = "gms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "gms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "gms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["gms.utils.before_request"]
# after_request = ["gms.utils.after_request"]

# Job Events
# ----------
# before_job = ["gms.utils.before_job"]
# after_job = ["gms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"gms.auth.validate"
# ]
