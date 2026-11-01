# Checkie trust, privacy and credibility audit

*28 October 2026 · Gau Yi Chi · with Claude*
*Method: every user-facing statement in `index.html` on the listed topics was extracted and checked against the JavaScript (what is actually sent, stored and requested), architecturedoc.md and the AI log. Network requests were recorded in a browser.*

## Issues found

| # | Severity | Issue | Status |
|---|---|---|---|
| 1 | **Critical** | Universities FAQ said the 12 answers "aren't sent anywhere". In fact, if a student sends feedback, the flagged/unsure sign names (box ticked by default), the result level and the screenshot count are sent. | **Fixed**: wording now matches the code. |
| 2 | **Critical** | The "What exactly is sent?" fold-out didn't mention that the result level and the screenshot count are always sent with feedback. | **Fixed** |
| 3 | **High** | Feedback was called "anonymous" (student page, universities page, staff guide), but Netlify records IP addresses and the comment box is free text. | **Fixed**: "no name or email; the host records IP addresses". |
| 4 | **High** | Every page loaded a font from Google Fonts, sending visitors' IP addresses to Google, and this wasn't disclosed anywhere. | **Fixed**: font embedded (SIL OFL); only OpenStreetMap map tiles are now requested from a third party (verified in the browser). |
| 5 | **High** | No statement of how long feedback is kept. | **Fixed (disclosure)**: "kept until I delete it; no fixed schedule yet". A schedule needs your decision; see proposals. |
| 6 | **High** | No single place explaining all data flows (check, campus memory, map tiles, route links, feedback, AI beta, enquiries). | **Fixed**: new "What goes where" data page, linked from the footer, FAQ and universities page. |
| 7 | **High** | Pilot offered "a summary of anonymous feedback after the intake", implying it covers that university's students. Feedback can't be linked to a university. | **Fixed**: now says the summary covers all users in the pilot period. |
| 8 | **High** | The consent box for sending sign names is ticked by default. Under EU data protection rules, a pre-ticked box is generally not valid consent, if consent is the legal basis. | **Proposed, not changed** (changes data collection; needs your decision and ideally advice). |
| 9 | **High** | No legal privacy notice (who is responsible, legal basis, rights, contact) although IP addresses and staff work emails are collected. | **Proposed, not implemented** (needs legal review). The data page states it isn't one. |
| 10 | **Medium** | "About once a week I count…" described a learning process as running; there are 0 real answers. | **Fixed**: "once at least 10 students have sent feedback…". |
| 11 | **Medium** | Feedback thank-you: "It goes straight into the next update of Checkie." | **Fixed**: counted, and reviewed by a person before anything changes. |
| 12 | **Medium** | AI beta (Claude version): "Checkie stores nothing" didn't say that screenshots, answers and prices go to Anthropic under the user's account and terms. | **Fixed** in this file. **The published Claude artifact (13 October) still has the old wording**; see remaining risks. |
| 13 | **Medium** | "This is the most common rental scam pattern" and "one of the most common scam signs": superlatives not backed by a source. | **Fixed**: "one of the most common", "a common scam sign". |
| 14 | **Medium** | Area card for El Raval: "More petty crime, and some blocks feel unsafe at night": an unsourced safety claim about a neighbourhood. | **Fixed**: neutral advice to visit the exact street, day and evening. |
| 15 | **Medium** | "Seniors usually know one or two flats from last year" and "the questions scammers hope you skip": generalisations without evidence. | **Fixed**: softened. |
| 16 | **Medium** | Map pop-ups showed "~25 min to Esade" without saying it's an estimate (area cards did). | **Fixed**: "(rough estimate)". |
| 17 | **Medium** | Trust row "Your answers stay on your device" was true only if no feedback is sent. | **Fixed**: "…unless you send feedback". |
| 18 | **Medium** | The universities page referred to "the public architecture document" without a link. | **Fixed**: links to GitHub and the data page. |
| 19 | **Medium** | Campus choice saved in local storage wasn't mentioned in the student FAQ (it was in the docs). | **Fixed** |
| 20 | **Low** | Feedback tag "Better AI check" appears on the public site, which has no AI check. | Left (harmless, and useful if the AI comes later). |
| 21 | **Low** | `loop/test/` holds made-up data in the public repo. | Left: every row and file is labelled TEST. |

**Checked and found correct (no change):**
- **Never "safe":** the result never calls a listing safe. "No common patterns found" always adds "That does not mean it's safe." The same holds in the FAQ, the email paragraph and the staff guide.
- **No accusations:** no result, message or tag names or accuses a landlord. The landlord message asks questions only. The learning loop's red line forbids judging people by name, nationality or neighbourhood, and the questions are about behaviour (payment, viewing, contract), not people.
- **Affiliation:** no university endorsement is implied. "Not affiliated" appears on the help card, in the FAQ, the footer and the universities page. Contacts are public addresses, and emails are shown only where published.
- **Human review:** labelled planned or "not built" everywhere.
- **No landlord money:** the principle is stated and nothing contradicts it.
- **Price check:** sources and date are stated, ranges are called approximate, and residence and studio ranges are city-wide (said so). Nothing typed into it is sent (verified: the feedback POST has no price fields).
- **Learning loop:** live `learned.json` has 0 answers, so no "Often reported" tag or "last learned" line shows on the live site.
- **Universities:** no price, partner, testimonial or impact figure is claimed. Measures are labelled by availability. "No university-specific impact report" is stated.

## Can the university offer be delivered with the current architecture?

| Offer | Deliverable today? |
|---|---|
| Link and materials, QR code, staff guide | Yes |
| Office contact shown on Checkie | Yes (edit the contacts list) |
| Content review before an intake | Yes (manual) |
| Summary of feedback during the pilot | Yes, but **all users**, manual, only if ≥10 responses |
| Feedback from that university's students only | No: needs an intake code saved with feedback (changes data collection) |
| Visit/completion counts | No: needs anonymous counting (new instrumentation) |
| Human screenshot review | No: needs an upload channel, storage, a reviewer and a privacy assessment |
| Annual subscription | Not defined; nothing to deliver yet, correctly stated as "no price set" |

## Proposals that need your decision (not implemented)

1. **Consent default:** untick the "Also send which warning signs I flagged" box by default (opt-in). You'll get fewer sign names, but valid consent. Smallest change: one attribute.
2. **Retention:** for example, "raw feedback deleted from Netlify within 30 days of each count; only the counts in learned.json are kept". Then delete on that schedule and update the site's wording.
3. **Privacy notice:** add a short notice naming you as the person responsible, a contact address, the purpose, the legal basis, the retention period, Netlify as processor (US) and how to make requests. Have it checked (for example by Esade's legal or data-protection contact) before a university pilot.
4. **Intake code (`?u=esade`):** save which partner link a student came from with feedback, so a university-specific summary becomes possible. Disclose it on the data page first.
5. **Republish the Claude version** with the updated AI wording, or stop linking to it until it's updated.

## Remaining risks

- The site is not a legal privacy notice and has had no data-protection review.
- The consent default may not meet consent rules (proposal 1).
- A contact address now exists (Contact page, 1 November); feedback still can't be found per person.
- The Claude artifact (claude.ai/artifact/9kZSvrctAsLUYHTei1FiJ4) is the 13 October version with older wording; it's linked from architecturedoc.md and section C of the Session 6 summary.
- Price ranges and platform rules will go out of date; there's no automatic check, only "last reviewed October 2026".
- Evidence for value is small and from my own network (12 of 15); every institutional benefit is still a hypothesis.

## Tests after the fixes

All flows re-run on phone and desktop sizes:
- questionnaire and scoring,
- result,
- landlord message,
- price check,
- map,
- feedback with and without sign names,
- pilot enquiry,
- "Ask your university".

All passed, with no console errors. The embedded font loads. The only third-party host contacted while using the site was `tile.openstreetmap.org` (recorded in a browser session covering home, check, result, data page and the Areas map).
