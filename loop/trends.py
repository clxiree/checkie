#!/usr/bin/env python3
"""Checkie scam trends: count which warning signs students flagged, for a person to review.

Usage:
  python3 loop/trends.py feedback.csv --from 2026-11-01 --to 2026-11-30
      -> prints the proposed counts (nothing is changed)
  python3 loop/trends.py feedback.csv --from 2026-11-01 --to 2026-11-30 --approve "Gau Yi Chi"
      -> after you have read the counts, writes them to learned.json as "trend"

feedback.csv is the Netlify Forms export of the "checkie-feedback" form. Only the "flagged"
column (signs answered Yes, sent only when the student left the consent box ticked) is counted.
Rows marked TEST ROW are ignored. Nothing about a listing or a person is read or written.
"""
import csv, json, sys, argparse, datetime, pathlib, collections

FLAGS = ["Payment requested before any viewing", "Landlord 'abroad', keys sent after payment",
 "Unusual or untraceable payment method", "Price well below the area", "Pressure to pay quickly",
 "No written contract before payment", "ID requested before any viewing", "Conversation moved off the platform",
 "No exact address before payment", "No live video tour; photos can't be verified", "Large upfront payment",
 "Unexplained extra fee"]

ap = argparse.ArgumentParser()
ap.add_argument("csv"); ap.add_argument("--from", dest="d0", required=True); ap.add_argument("--to", dest="d1", required=True)
ap.add_argument("--approve", help="your name; writes the trend to learned.json"); ap.add_argument("--learned", default="learned.json")
a = ap.parse_args()

counts, reports = collections.Counter(), 0
with open(a.csv, newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        if "TEST ROW" in " ".join(str(v) for v in row.values()): continue
        at = (row.get("at") or row.get("created_at") or "")[:10]
        if not (a.d0 <= at <= a.d1): continue
        flagged = [x.strip() for x in (row.get("flagged") or "").split(";") if x.strip()]
        if not flagged: continue          # only students who shared their signs count as reports
        reports += 1
        for f in set(flagged):
            if f in FLAGS: counts[FLAGS.index(f)] += 1

learned = json.loads(pathlib.Path(a.learned).read_text(encoding="utf-8"))
minimum = learned.get("minAnswers", 10)
signs = [{"k": k, "count": c} for k, c in counts.most_common()]
print(f"Reports with shared signs, {a.d0} to {a.d1}: {reports} (minimum to publish: {minimum})")
for x in signs: print(f"  {x['count']:>3}  ({round(100*x['count']/reports) if reports else 0}%)  {FLAGS[x['k']]}")
print("\nCheck before approving: enough reports? one day or one group flooding the counts? anything that could judge a person or area?")
if not a.approve:
    print("Nothing written. Add --approve \"Your Name\" once you have reviewed the counts."); sys.exit(0)
if reports < minimum:
    print("Not written: fewer reports than the minimum."); sys.exit(1)
learned["trend"] = {"from": a.d0, "to": a.d1, "reports": reports, "signs": signs}
learned["reviewedOn"] = datetime.date.today().isoformat(); learned["reviewedBy"] = a.approve
pathlib.Path(a.learned).write_text(json.dumps(learned, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Written to {a.learned}. Commit it to GitHub to publish.")
