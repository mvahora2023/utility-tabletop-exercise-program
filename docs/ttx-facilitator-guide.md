# ttx-facilitator-guide.md

# Tabletop Exercise Facilitator Guide — "Operation Lockout"

**Fictional Utility:** Keystone Gas & Electric
**Exercise Type:** Full-Scale Annual Exercise
**Prepared By:** Mahmadarsh Vahora
**Estimated Duration:** 4 hours

---

## Scenario Background

A financially motivated ransomware group, tracked under the fictional designation **IRON CRANE**, gains initial access to Keystone Gas & Electric's corporate IT network via a phishing email targeting a Finance department employee. The email impersonates a known vendor invoice and contains a malicious macro-enabled attachment. Over the following 72 hours, IRON CRANE conducts internal reconnaissance, harvests credentials, and moves laterally toward the IT/OT DMZ boundary. A historian server sitting in the Level 3 site operations zone is encrypted. Separately, operators at one of three simulated compressor stations report that the HMI has become unresponsive — whether this is a direct consequence of the ransomware event or a coincidental operational issue is deliberately left ambiguous for players to investigate, mirroring the uncertainty present in real incidents.

## Timeline Narrative

- **Day 0 (T+0h):** Phishing email delivered and opened by Finance team member. Malicious macro executes, establishing initial foothold. (Not yet detected by the organization.)
- **Day 0 (T+6h):** Attacker begins internal reconnaissance and credential harvesting from the compromised Finance workstation.
- **Day 1 (T+22h):** EDR alert fires on the Finance workstation for suspicious PowerShell activity. This is the exercise's actual starting point for players (Inject 1).
- **Day 1–2:** Investigation, escalation, and containment decisions play out across IT Security, the Cybersecurity Coordinator, and executive stakeholders.
- **Day 2 (T+50h):** Historian server in the Level 3 zone is found encrypted.
- **Day 2 (T+52h):** HMI at Compressor Station Alpha becomes unresponsive.
- **Day 3 (T+68h):** Organization must decide on public/regulatory communication posture and return-to-operations timeline.

---

## Sequential Injects

| Inject ID | Time | Event Description | Expected Player Actions | Discussion Questions | Evaluation Criteria |
|---|---|---|---|---|---|
| INJ-01 | Day 1, T+22h | EDR alert: suspicious PowerShell execution on Finance workstation FIN-WKS-014 | IT Security triages alert; determines scope of initial compromise | Who is notified first? What is the internal escalation threshold for "this might be more than a single workstation"? | Escalation occurs within 30 minutes of alert; correct initial responder identified |
| INJ-02 | Day 1, T+23h | Investigation reveals lateral movement attempts from FIN-WKS-014 toward the domain controller | IT Security escalates to Incident Response Program Manager; begins containment planning | At what point does this become a "declared incident" vs. routine alert handling? | IR Program Manager engaged within 1 hour of INJ-01 |
| INJ-03 | Day 1, T+26h | Decision point: should FIN-WKS-014 and adjacent Finance segment be isolated from the network? | IT Security proposes isolation; Finance leadership raises business-continuity concerns (month-end close in progress) | How is a business-disruption objection weighed against containment urgency? Who has final authority? | A named decision-maker (not "the team") makes and documents the isolation call within the exercise timeframe |
| INJ-04 | Day 1, T+28h | Cybersecurity Coordinator formally activated per CIRP | Coordinator assumes incident command; confirms CISA 24-hour reporting clock has started | Is the CISA reporting clock correctly calculated from initial detection or initial compromise? | Players correctly identify INJ-01 (detection) as the reporting-clock trigger point, not Day 0 compromise |
| INJ-05 | Day 1, T+30h | CISA 24-hour reporting notification trigger point reached | Coordinator or designee prepares and submits CISA report | Who drafts the report? Who reviews before submission — Legal, executive leadership, both? | Report drafted and routed for review before the 24-hour deadline lapses |
| INJ-06 | Day 2, T+48h | Forensic review finds attacker activity approaching the IT/OT DMZ boundary firewall logs | IT Security and OT Engineering jointly assess whether OT isolation is warranted preemptively | Should OT be isolated before confirmed OT compromise, accepting operational impact, or only after confirmed compromise? | Players articulate a documented risk-based rationale either way — silence or indecision is a finding |
| INJ-07 | Day 2, T+50h | Historian server (Level 3) found encrypted with ransomware note | OT Engineering confirms Historian isolation; Coordinator reassesses incident severity tier | Does Historian encryption alone justify full OT/IT isolation, or only isolation of the Historian's specific network segment? | Decision documented with named owner and rationale tied to the architecture's zone/conduit model |
| INJ-08 | Day 2, T+52h | HMI at Compressor Station Alpha becomes unresponsive (cause ambiguous) | OT Engineering must determine whether this is ransomware-related or a coincidental operational fault before deciding on physical/manual control fallback | Does the organization have a documented manual/local control fallback procedure for this exact scenario? | Players identify (or identify the absence of) a manual control fallback procedure — this is a common real-world gap |
| INJ-09 | Day 2, T+54h | Media inquiry received: a local news outlet asks whether "a cyberattack has affected gas service in the region" | Corporate Communications drafts a holding statement; coordinates with Legal and the Coordinator before any public statement | Is there a pre-approved holding statement template? Who has final sign-off authority on external statements during an active incident? | A holding statement is produced and reviewed within the exercise's simulated time window, not left unaddressed |
| INJ-10 | Day 2, T+56h | Discovery that a third-party vendor's remote access credentials were used during the lateral movement phase | IT Security and Vendor Risk lead jointly decide to revoke/lock out all third-party remote access pending investigation | Is there a documented emergency vendor-access-revocation procedure, or does this require ad hoc coordination with each vendor individually? | Vendor access lockout executed and documented within 2 hours of discovery in exercise time |
| INJ-11 | Day 2, T+60h | Backup/recovery team confirms viable, uninfected backups exist for the Historian server | IT Operations initiates recovery planning; Coordinator briefs on estimated restoration timeline | Are backup integrity-verification steps documented, or is "restore and hope" the de facto plan? | Players articulate a specific backup-verification step before restoration begins |
| INJ-12 | Day 3, T+64h | Executive Leadership requests a full briefing ahead of a board-level update | Coordinator and IR Program Manager prepare an executive summary covering scope, containment status, and estimated full-recovery timeline | Is the briefing format pre-defined, or built ad hoc under time pressure? | A structured executive briefing (not a raw findings dump) is produced within the exercise timeframe |
| INJ-13 | Day 3, T+66h | OT Engineering confirms Compressor Station Alpha HMI issue was operational (unrelated hardware fault), not ransomware-caused | Team must decide whether this changes the incident severity classification and reporting posture | Does discovering the HMI issue was unrelated change any regulatory reporting obligations already triggered? | Players correctly determine that CISA/TSA reporting obligations, once triggered, are not retroactively withdrawn |
| INJ-14 | Day 3, T+68h | Return-to-operations decision point: IT systems cleared for restoration; Historian rebuild in progress | Coordinator, IT, and OT Engineering jointly decide on phased return-to-operations sequencing | What is the criteria for declaring "operational normal" — full system restoration, or partial restoration with monitoring? | A phased RTO plan with explicit criteria (not a single "all clear") is documented |
| INJ-15 | Day 3, T+70h | Exercise closes: facilitator initiates hot-wash discussion | All players participate in structured hot-wash before formal After-Action Report drafting begins | What surprised you most about today's exercise? What would you change about your own team's response? | Every functional group contributes at least one specific, actionable observation (not "it went fine") |

---

## Facilitator Notes (What to Watch For / Common Gaps)

- **INJ-01 to INJ-03:** Watch for a diffusion-of-responsibility failure mode where "IT Security" as a group is expected to escalate, but no individual actually picks up the phone. This is one of the most common real-world tabletop findings and should be actively probed if it doesn't surface naturally.
- **INJ-04 to INJ-05:** A frequent gap is miscalculating the CISA reporting clock start time. Facilitators should not correct this in the moment — let the miscalculation play out and capture it as a finding, since the value of the exercise is surfacing this before a real incident does.
- **INJ-06 to INJ-08:** These injects are designed to surface whether OT Engineering and IT Security have a shared, pre-agreed threshold for preemptive OT isolation. Organizations frequently discover in exercises (not before) that this threshold has never been explicitly defined.
- **INJ-08 specifically:** If players cannot answer whether a manual/local control fallback exists, do not supply the answer — this ambiguity is itself the finding and should be captured verbatim in the After-Action Report.
- **INJ-09:** Watch for Communications acting without Legal/Coordinator sign-off, or conversely, total paralysis waiting for sign-off with no interim holding statement — both are findings worth capturing distinctly.
- **INJ-10:** This inject frequently reveals that vendor access revocation is technically possible but procedurally undefined — i.e., "we could do it, we just don't have a documented process for who authorizes it."
- **INJ-13:** This is a deliberate "false flag" inject. Its purpose is to test whether players understand that regulatory reporting obligations, once triggered by a good-faith assessment at the time, are not undone by later learning the full picture was less severe. Players who suggest "un-reporting" or downplaying the earlier CISA report should have this specifically discussed in the hot-wash.

---

## Facilitated Discussion Questions (End-of-Exercise)

1. At what specific point in today's timeline did we cross from "monitoring an alert" to "managing a declared incident," and was that transition documented in real time?
2. Did every functional group (IT, OT, Legal, HR, Communications, ERM) know their specific role before the exercise began, or did roles have to be improvised during play?
3. Is our CISA/TSA reporting clock calculation methodology written down anywhere our Coordinator can reference under pressure, or does it rely on institutional memory?
4. Do we have a documented, tested manual/local control fallback procedure for OT systems in the event of HMI unavailability — regardless of cause?
5. Who has actual sign-off authority for an external communications statement during an active incident, and is that authority documented or assumed?
6. Is there a defined, pre-authorized procedure for emergency third-party vendor access revocation, or does each vendor relationship require ad hoc handling?
7. How would today's exercise have changed if the ransomware had directly encrypted a PLC or RTU rather than the Historian — do we have confidence in our answer, or are we assuming?
8. What is our actual criteria for declaring "return to normal operations," and is it documented anywhere outside of today's discussion?
9. Which finding from today are we most likely to actually remediate in the next 90 days, and which are we most likely to let slide — and why?
10. If TSA requested evidence that this exercise occurred and that its findings were tracked to closure, what would we produce today, and is it audit-ready?
