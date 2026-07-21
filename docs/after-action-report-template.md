# after-action-report-template.md

# After-Action Report — Tabletop Exercise

**Fictional Utility:** Keystone Gas & Electric

---

## Exercise Metadata

| Field | Value |
|---|---|
| Exercise Name | Operation Lockout |
| Exercise Type | Full-Scale Annual Exercise |
| Date Conducted | [Insert Date] |
| Facilitator | [Insert Name] |
| Controller(s) | [Insert Name(s)] |
| Observer(s) | [Insert Name(s)] |
| Participants / Departments Represented | IT Security, OT Engineering, Legal, HR, Enterprise Risk Management, Corporate Communications, Executive Leadership |
| Report Prepared By | [Insert GRC Analyst Name] |
| Report Date | [Insert Date] |
| Distribution Classification | Internal — GRC Program Records |

---

## Executive Summary

**Strengths Observed:**
- [Insert strength — e.g., "IT Security escalation to the Incident Response Program Manager occurred within the target window following the initial EDR alert."]
- [Insert strength]
- [Insert strength]

**Areas for Improvement:**
- [Insert improvement area — e.g., "Cross-functional role clarity for Communications sign-off authority was not established prior to the exercise."]
- [Insert improvement area]
- [Insert improvement area]

**Critical Gaps Identified:**
- [Insert critical gap — e.g., "No documented manual/local control fallback procedure exists for HMI unavailability at compressor stations."]
- [Insert critical gap]

---

## Findings Log

| Finding ID | Category | Description | Impact | Recommended Action | Owner | Due Date | Status |
|---|---|---|---|---|---|---|---|
| FND-01 | Process | No documented, pre-agreed threshold exists for preemptive OT isolation ahead of confirmed OT compromise | High — delays containment decision-making during a live incident, increasing dwell time and potential OT exposure | Develop and formally document an OT isolation decision matrix, jointly owned by IT Security and OT Engineering, with pre-approved trigger conditions | OT Engineering Lead / IT Security Manager | +60 days | Open |
| FND-02 | Technical | No documented manual/local control fallback procedure exists for HMI unavailability at compressor stations | Critical — during an actual HMI outage (ransomware-caused or otherwise), operators would need to improvise a response without a tested procedure | Document and validate a manual/local control fallback procedure for each compressor station HMI, and incorporate into OT Engineering training | OT Engineering Lead | +90 days | Open |
| FND-03 | Communication | Corporate Communications sign-off authority for external statements during an active incident was not clearly defined before the exercise | Medium — risk of either unauthorized premature statements or paralysis/delay in responding to media inquiries during a real incident | Formally document sign-off authority and escalation path for external communications during declared incidents, with Legal and Coordinator concurrence | Corporate Communications Lead / Legal | +45 days | Open |
| FND-04 | Process | No documented emergency procedure exists for third-party vendor remote access revocation | Medium — ad hoc coordination required with individual vendors during a live incident increases response time and inconsistency | Develop a standardized emergency vendor-access-revocation procedure with pre-authorized execution rights for IT Security | IT Security Manager / Vendor Risk Analyst | +60 days | Open |
| FND-05 | Policy | CISA/TSA regulatory reporting clock calculation methodology is not documented in a readily accessible reference for the Cybersecurity Coordinator | High — risk of miscalculating regulatory reporting deadlines during a high-pressure live incident, with compliance and legal exposure | Create a one-page reporting clock quick-reference card for the CIRP, embedded in the Coordinator's incident response kit | Cybersecurity Coordinator | +30 days | Open |

*(Additional findings from the live exercise should be appended below using the same table structure.)*

---

## Improvement Plan

| Timeframe | Milestone |
|---|---|
| **90 Days** | FND-05 (reporting clock reference card) and FND-03 (Communications sign-off authority documentation) closed and validated |
| **180 Days** | FND-01 (OT isolation decision matrix) and FND-04 (vendor access revocation procedure) closed, tested via a functional exercise, and incorporated into the CIRP |
| **1 Year** | FND-02 (manual/local control fallback procedure) fully documented, validated through a dedicated OT-focused functional exercise, and incorporated into OT Engineering onboarding/training curriculum; full findings-recurrence check performed against the next annual full-scale exercise |

---

## Distribution List

- Global Cybersecurity Risk Manager
- Cybersecurity Coordinator
- IT Security Manager
- OT Engineering Lead
- Legal Counsel
- Enterprise Risk Management Lead
- Corporate Communications Lead
- HR Business Partner (Cybersecurity Program)

---

## Approval Signatures

| Role | Name | Signature | Date |
|---|---|---|---|
| Global Cybersecurity Risk Manager | | | |
| Cybersecurity Coordinator | | | |
| GRC Analyst (Report Preparer) | | | |
