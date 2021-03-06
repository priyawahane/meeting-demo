# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "meeting_demo"
app_title = "meeting-demo"
app_publisher = "frappe"
app_description = "prepare agenda"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "priya.wahane@usense.co"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/meeting_demo/css/meeting_demo.css"
# app_include_js = "/assets/meeting_demo/js/meeting_demo.js"

# include js, css files in header of web template
# web_include_css = "/assets/meeting_demo/css/meeting_demo.css"
# web_include_js = "/assets/meeting_demo/js/meeting_demo.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "meeting_demo.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "meeting_demo.install.before_install"
# after_install = "meeting_demo.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "meeting_demo.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"meeting_demo.tasks.all"
# 	],
# 	"daily": [
# 		"meeting_demo.tasks.daily"
# 	],
# 	"hourly": [
# 		"meeting_demo.tasks.hourly"
# 	],
# 	"weekly": [
# 		"meeting_demo.tasks.weekly"
# 	]
# 	"monthly": [
# 		"meeting_demo.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "meeting_demo.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "meeting_demo.event.get_events"
# }

