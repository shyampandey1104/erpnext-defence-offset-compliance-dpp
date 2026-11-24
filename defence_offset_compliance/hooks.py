# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "defence_offset_compliance"
app_title = "Erpnext Defence Offset Compliance Dpp"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Defence Offset Compliance Dpp - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/defence_offset_compliance/css/defence_offset_compliance.bundle.css"
app_include_js = "/assets/defence_offset_compliance/js/defence_offset_compliance.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Defence Offset Compliance Dpp Entry": {
        "validate": "defence_offset_compliance.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "defence_offset_compliance.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "defence_offset_compliance.tasks.hourly_sync"
    ],
    "daily": [
        "defence_offset_compliance.tasks.daily_reconciliation"
    ],
    "weekly": [
        "defence_offset_compliance.tasks.weekly_digest"
    ]
}
