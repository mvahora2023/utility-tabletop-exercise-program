# ttx-program-charter.md

# Tabletop Exercise (TTX) Program Charter

**Fictional Utility:** Keystone Gas & Electric
**Program Owner:** Global Cybersecurity Risk Manager (GRC Analyst as program administrator)
**Prepared By:** Mahmadarsh Vahora
**Version:** 1.0

> **Portfolio Disclosure:** This charter is a self-directed portfolio artifact demonstrating a Tabletop Exercise program design for a regulated utility. "Keystone Gas & Electric" is fictional; no content reflects the real posture or programs of UGI Utilities, Inc.

---

## 1. Program Purpose

The Keystone Gas & Electric Tabletop Exercise (TTX) Program exists to validate, through structured discussion-based simulation, the organization's ability to detect, respond to, contain, and recover from cybersecurity incidents affecting both IT and OT/SCADA systems — without the risk or cost of a live-fire exercise against production infrastructure. The program is designed to satisfy the exercise requirements embedded in TSA Security Directive Pipeline-2021-02 while producing genuinely useful organizational learning, not a compliance-only checkbox exercise.

## 2. Scope

The program covers cybersecurity incident scenarios affecting:
- Corporate IT systems with connectivity to OT/Critical Cyber Systems (CCS)
- OT/SCADA control systems supporting pipeline and LDC operations
- Third-party/vendor access paths into either environment
- Cross-functional response coordination among IT, OT Engineering, Legal, HR, Enterprise Risk Management (ERM), and Corporate Communications

## 3. Regulatory Drivers

- **TSA Security Directive Pipeline-2021-02** — requires a documented, tested Cybersecurity Incident Response Plan (CIRP), with exercises validating the plan's effectiveness
- **PA Public Utility Commission (PUC) oversight** — expects demonstrable incident preparedness as part of broader utility reliability and safety obligations
- **NIST SP 800-82 Rev. 3, Chapter 4 (Applying the Risk Management Framework to OT)** — establishes security program development expectations, including periodic testing of incident response capability against OT-specific scenarios

## 4. Program Governance

| Role | Responsibility |
|---|---|
| **Program Owner** | Global Cybersecurity Risk Manager — accountable for program existence, budget, and reporting exercise outcomes to executive leadership |
| **Program Administrator** | GRC Analyst — owns scenario development calendar, facilitator scheduling, findings tracking, and TSA-facing documentation |
| **Facilitator** | Designated exercise lead (rotates among GRC Analyst, IR Program Manager, or contracted third party for full-scale exercises) |
| **Controller(s)** | Support the Facilitator by injecting scenario events and managing exercise pacing |
| **Observers** | Document player actions and decision points without participating, feeding the After-Action Report |
| **Players** | IT Security, OT Engineering, Legal, HR, Enterprise Risk Management, Corporate Communications, and Executive Leadership (for escalation-tier exercises) |

## 5. Annual TTX Calendar

| Exercise Type | Frequency | Typical Duration | Participant Level |
|---|---|---|---|
| Full-Scale Exercise | 1 per year | Half-day (4 hours) | Cross-functional, including executive leadership for final escalation segment |
| Functional Exercise | 2 per year | 2 hours each | Department-level (e.g., IT Security + OT Engineering only, or Legal + Communications only) |

This cadence exceeds the minimum TSA testing requirement to build organizational muscle memory ahead of the Biennial Cybersecurity Audit cycle (see companion [[tsa-biennial-audit-readiness-checklist]]).

## 6. Metrics Tracked by the GRC Analyst

| Metric | Purpose |
|---|---|
| Findings count per exercise | Tracks whether exercises are surfacing genuine gaps (a zero-findings exercise is a red flag for exercise realism, not a success) |
| Remediation closure rate | Percentage of prior-exercise findings closed before the next exercise cycle |
| Attendance rate by department | Identifies departments consistently under-represented in exercises, a governance risk in itself |
| Time-to-close (findings) | Average days from finding identification to remediation closure, reported to IT senior leadership |
| Recurrence rate | Percentage of findings that reappear across multiple exercise cycles, indicating a systemic (not one-off) gap |

## 7. Relationship to Other Program Artifacts

- Exercise scenarios and findings feed directly into the Cybersecurity Incident Response Plan (CIRP) revision cycle referenced in the [[tsa-biennial-audit-readiness-checklist]]
- Architecture-related findings (e.g., segmentation gaps surfaced during a scenario) are routed to the [[architecture-design-review-template]] process for formal design review
- Aggregate exercise metrics are reported through the [[compliance-gap-tracker-v2]] dashboard for executive visibility
