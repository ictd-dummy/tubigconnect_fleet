app_name = "tubigconnect_fleet"
app_title = "TubigConnect Fleet"
app_publisher = "GSCWD ICTD"
app_description = "Fleet Management"
app_email = "administrator@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "tubigconnect_fleet",
# 		"logo": "/assets/tubigconnect_fleet/logo.png",
# 		"title": "TubigConnect Fleet",
# 		"route": "/tubigconnect_fleet",
# 		"has_permission": "tubigconnect_fleet.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tubigconnect_fleet/css/tubigconnect_fleet.css"
# app_include_js = "/assets/tubigconnect_fleet/js/tubigconnect_fleet.js"

# include js, css files in header of web template
# web_include_css = "/assets/tubigconnect_fleet/css/tubigconnect_fleet.css"
# web_include_js = "/assets/tubigconnect_fleet/js/tubigconnect_fleet.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tubigconnect_fleet/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "tubigconnect_fleet/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "tubigconnect_fleet.utils.jinja_methods",
# 	"filters": "tubigconnect_fleet.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "tubigconnect_fleet.install.before_install"
# after_install = "tubigconnect_fleet.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tubigconnect_fleet.uninstall.before_uninstall"
# after_uninstall = "tubigconnect_fleet.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "tubigconnect_fleet.utils.before_app_install"
# after_app_install = "tubigconnect_fleet.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "tubigconnect_fleet.utils.before_app_uninstall"
# after_app_uninstall = "tubigconnect_fleet.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "tubigconnect_fleet.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tubigconnect_fleet.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tubigconnect_fleet.tasks.all"
# 	],
# 	"daily": [
# 		"tubigconnect_fleet.tasks.daily"
# 	],
# 	"hourly": [
# 		"tubigconnect_fleet.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tubigconnect_fleet.tasks.weekly"
# 	],
# 	"monthly": [
# 		"tubigconnect_fleet.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "tubigconnect_fleet.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "tubigconnect_fleet.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tubigconnect_fleet.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tubigconnect_fleet.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["tubigconnect_fleet.utils.before_request"]
# after_request = ["tubigconnect_fleet.utils.after_request"]

# Job Events
# ----------
# before_job = ["tubigconnect_fleet.utils.before_job"]
# after_job = ["tubigconnect_fleet.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tubigconnect_fleet.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

