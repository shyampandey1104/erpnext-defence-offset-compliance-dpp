# ERPNext Defence Offset Compliance & DAP 2020 Banking Engine

[![Frappe Framework](https://img.shields.io/badge/Frappe-v15.x-blue.svg)](https://frappeframework.com/)
[![Defence Procurement](https://img.shields.io/badge/MoD-DAP%202020%20Offsets-red.svg)]()
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📌 Executive Overview & Real-World Client Problem

Under the Ministry of Defence (MoD) **Defence Acquisition Procedure (DAP 2020)**, foreign Original Equipment Manufacturers (OEMs) winning capital acquisition contracts exceeding ₹2,000 Crores must fulfill mandatory **30% to 50% offset obligations** through Indian Offset Partners (IOPs).

**Critical Enterprise Bottlenecks:**
1. **Liquidated Damages Exposure:** Failure to meet annual offset milestones triggers punitive **5% liquidated damages (LD)** levied by the Defence Offset Management Wing (DOMW).
2. **Complex Tier Multiplier Verification:** MSME suppliers qualify for a 1.5x credit multiplier, while critical aerospace technologies qualify for up to 4.0x. Calculating these without auditable evidence leads to rejected offset claims.
3. **Offset Banking & Discharge Reconciliation:** OEMs struggle to bank surplus credits and draw them down against multiple concurrent MoD defense contracts.

This Frappe application implements an institutional Defence Offset Banking & Compliance Ledger ensuring zero audit friction with DOMW inspectors.

---

## 🏛️ System Architecture Flow

```mermaid
flowchart TD
    A["MoD Capital Acquisition Contract (DAP 2020)"] -->|Set Offset Obligation (30-50%)| B["Master Offset Obligation Ledger"]
    C["Indian Offset Partner (IOP) Deliverables"] -->|Physical Purchase & Services| D["Transaction Claim Generator"]
    D -->|Apply Category Multipliers (1.5x MSME / 2.0x Tech)| E["Eligible Offset Credit Calculator"]
    E -->|Quarterly DOMW Claim Filing| F["DOMW Offset Banking Vault"]
    F -->|Milestone Discharge| G{"Annual Milestone Met?"}
    G -->|Yes| H["Compliance Cleared: Zero Penalty"]
    G -->|No (Shortfall Detected)| I["Liquidated Damages (5% LD) Risk Flagged"]
```

---

## 🚀 Key Engineering Capabilities

- **DOMW Multiplier Engine:** Automatically applies statutory multipliers (1.5x for MSMEs, 2.0x for deep-tech/critical aerospace tech).
- **Offset Credit Banking Ledger:** Maintains banked credits with statutory validity windows and multi-contract drawdown rules.
- **Liquidated Damages Risk Forecaster:** Computes potential 5% shortfall penalties and notifies defense compliance directors.
- **Form 1-5 Offset Claim Exporter:** Formats quarterly progress submissions directly compatible with DOMW audit templates.

---

## 📂 Frappe DocType Schema & Data Structure

```text
defence_offset_compliance/
├── defence_offset_compliance_core/
│   ├── doctype/
│   │   ├── defence_offset_contract/
│   │   │   ├── defence_offset_contract.json
│   │   │   ├── defence_offset_contract.py
│   │   │   └── defence_offset_contract.js
│   │   └── offset_transaction_claim/
│   │       └── offset_transaction_claim.json
│   └── workspace/
│       └── defence_offset_compliance_workspace/
│           └── defence_offset_compliance_workspace.json
```

---

## ⚡ Frappe Hooks & Whitelisted APIs

- **REST Endpoint:** `POST /api/method/defence_offset_compliance.api.submit_offset_transaction_claim`
- **Whitelisted Method:** `@frappe.whitelist() def evaluate_domw_annual_audit(current_period_year)`
- **Hooks Event:** `on_submit` of `Purchase Invoice` (Defence IOP) validates offset credit eligibility.

---

## 🛠️ Installation & Bench Setup

```bash
bench get-app https://github.com/shyampandey1104/erpnext-defence-offset-compliance-dpp
bench --site erp.yourdomain.com install-app defence_offset_compliance
bench --site erp.yourdomain.com migrate
python3 -m unittest discover tests
```

---

## 📄 License
MIT License. Built for Global Aerospace & Defence OEMs and Tier-1 Indian Offset Partners.
