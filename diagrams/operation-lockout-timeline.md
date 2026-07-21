# "Operation Lockout" Exercise Timeline

Sequential inject timeline for the full-scale annual tabletop exercise (see [facilitator guide](../docs/ttx-facilitator-guide.md)).

```mermaid
timeline
    title Operation Lockout — Day 0 to Day 3 Inject Timeline
    Day 0 (T+0h to T+6h) : Phishing email opened, macro executes (undetected)
                          : Attacker begins internal recon and credential harvesting
    Day 1 (T+22h to T+30h) : INJ-01 EDR alert on Finance workstation
                          : INJ-02 Lateral movement toward domain controller detected
                          : INJ-03 Isolation decision point (Finance segment)
                          : INJ-04 Cybersecurity Coordinator activated
                          : INJ-05 CISA 24-hour reporting trigger reached
    Day 2 (T+48h to T+60h) : INJ-06 Attacker activity nears IT/OT DMZ boundary
                          : INJ-07 Historian server found encrypted
                          : INJ-08 Compressor Station HMI unresponsive
                          : INJ-09 Media inquiry received
                          : INJ-10 Vendor remote access credential compromise discovered
                          : INJ-11 Viable backups confirmed for Historian
    Day 3 (T+64h to T+70h) : INJ-12 Executive leadership briefing requested
                          : INJ-13 HMI issue confirmed unrelated to ransomware
                          : INJ-14 Return-to-operations decision point
                          : INJ-15 Exercise closes, hot-wash discussion begins
```

**Design intent:** the timeline deliberately separates the *detection point* (Day 1, T+22h) from the *actual compromise point* (Day 0, T+0h) by 22 hours — this gap is itself a discussion point in the facilitator's closing questions, since it mirrors real-world dwell-time patterns reported by CISA for nation-state and ransomware intrusions into critical infrastructure IT networks.
