from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
timeline=(root/"diagrams/operation-lockout-timeline.md").read_text(encoding="utf-8")
guide=(root/"docs/ttx-facilitator-guide.md").read_text(encoding="utf-8")
assert "Fictional" in guide
ids=re.findall(r":\s*(INJ-\d+)\b",timeline)
assert len(ids)==15 and len(set(ids))==15
assert ids==[f"INJ-{i:02d}" for i in range(1,16)]
for id_ in ids: assert id_ in guide,("Inject missing from facilitator guide",id_)
for day in range(4):assert f"Day {day}" in timeline
print(f"Validated {len(ids)} distinct, sequential fictional exercise injects across Day 0–3.")
