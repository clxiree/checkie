# Checkie: Architecture Document

*Last updated: 28 October 2026 (redesign; Session 7 learning loop on 27 October). First updated after my demo on 13 October, before class ended; later sections added after the session.*
*Author: Gau Yi Chi*

## 1. What Checkie is

Checkie is a free web tool for international and exchange students looking for a room in Barcelona. Before they pay anything, they answer 12 questions about a listing. Checkie shows which common scam patterns are present and what to verify. **It never tells a student that a listing is safe.**

The customer is the university. My plan is an annual subscription for a co-branded link in pre-arrival and welcome emails. Students always use it for free. Checkie never takes money from landlords, agencies or housing platforms, so students can trust the result.

## 2. Versions

| Version | Where it runs | What works |
|---|---|---|
| `index.html` + `learned.json` | Static site on Netlify: https://symphonious-jelly-dabdfa.netlify.app (code: https://github.com/clxiree/checkie) | Everything in section 3 except the AI screenshot check. Feedback and pilot requests are **saved through Netlify Forms**. |
| `checkie_claude.html` | Claude-hosted artifact: https://claude.ai/artifact/9kZSvrctAsLUYHTei1FiJ4. It runs the screenshot check through Claude on the student's own account (no API key in the page, no cost to me). | The 13 October version: the check, the AI screenshot check and the saved review section. **It does not have the later changes** (price check, new map, guide, redesign). |

Both are a single HTML file (HTML, CSS and plain JavaScript). There is no build step, framework or backend server of my own. Since 27 October, Netlify deploys the public site automatically from the GitHub repository (branch `main`), so the live site always matches the latest commit.

## 3. Components

*Rewritten on 28 October 2026 to match the code after the redesign.*

1. **Navigation**: a sticky header with three student tabs (Check · Areas · Guide) and a separate "For universities" button. Keyboard focus is visible only for keyboard users.
2. **Home** (restructured 28 October): one hero (headline, one sentence, the single filled button "Check a listing · 2 minutes", a link to the renting guide, a one-line "Answer 12 questions → See the warning signs → Know what to check", and "Free · No sign-up · Nothing saved unless you send feedback"), then three ruled blocks: **Also useful before you pay** (two tools: Check a rent, Explore areas), **Need more guidance?** (a list of links: renting guide, ask your university, already paid), **What Checkie can and can't do** (three statements on limits, privacy and independence, then the student FAQ, folded). A footer with student, university and about links appears on every page.
3. **12-question check**: all 12 questions on one page as compact rows (icon, question, description, a "Why?" fold-out with an example and the reason, small Yes / No / Not sure buttons), a sticky count of answered questions, and a link to ask a person instead. Unanswered questions don't count. Patterns covered: paying before a viewing, landlord abroad, untraceable payment, price far below the area, pressure, no contract, ID requested early, chat moved off the platform, no exact address, no live video, more than two months upfront, unexplained fees. Each question also has a concrete "what to do" action used on the result page.
4. **Screenshot step (optional, Claude version only)**: since 28 October the public site goes straight from the questions to the result, because screenshots only add value where the AI check exists. In the Claude version: up to 10 images, read in the browser with `FileReader`, shown next to the result. Nothing is uploaded. A "Skip and see my result" link makes skipping obvious.
5. **Result**: the scoring is unchanged: Stop before you pay (3 or more Yes), Be careful (1 or more Yes, or 2 or more Not sure), No common patterns found (otherwise, with "that does not mean it's safe"). Below it: each warning sign with why it matters and what to do; each "not sure" sign with how to find out; "What to do next" (don't pay if 3+ signs; always see the room, read a contract and pay a named account; check the price unless question 4 was answered No; ask your university; already paid?); and the note "These are warning signs, not proof of fraud." **Ask the landlord**: a copyable message in English or Spanish built from the student's answers (up to five questions: their Yes and Not sure signs first, then viewing, contract and address unless they answered No, then the owner's name). Nothing is sent or saved; the student pastes it into their own chat. **Send Checkie to a friend**: the phone's share sheet, or copies the link and a one-line message.
6. **AI screenshot check (Claude version only, beta)**: unchanged; on the public site the AI box is now hidden instead of showing an unavailable feature.
7. **"Ask your university"**: reachable from the home page, the questionnaire and the result. The student picks a university and gets its public international office contact (email only where officially published: UPC, UAB, UB; official page for Esade, UPF, IESE) and an editable message: a general one when opened directly, or one listing what Checkie flagged after the check. Checkie sends nothing itself and states it isn't affiliated with any university.
8. **Feedback and learning loop**: unchanged (see sections 4 and 4a): the warning-sign question, 1–5 rating, improvement tags, comment, and the ticked-by-default "Also send which warning signs I flagged" box with its "What exactly is sent?" preview.
9. **Areas page**: price check (room in a shared flat by area; student residence about €600–1,200 and studio about €700–1,200 city-wide); campus picker with straight-line distance and rough travel time; a Leaflet map with OpenStreetMap tiles in calm grey tones that opens on Barcelona's 12 areas (area names first, prices when zoomed in), pop-up cards with price, description, commute and a Google Maps route link, "back to Barcelona", full screen and "Show my campus"; an area list whose rows expand in place; "Other types of place"; sources. Falls back to a drawn map if tiles can't load.
10. **Renting guide**: 8 steps in one readable column with a timeline (budget, protected platforms, checking the listing, talking to the landlord, who owns the flat, contract, paying, moving in), "Already paid and think it's a scam?" steps, and a glossary of Spanish rental words.
11. **For universities page**: written for an international office: four key facts (who it's for, what the office does, what it collects, cost to students); the problem; evidence with its limits; what Checkie offers beyond a housing resources page; available now vs what could be added for a partner (each labelled "simple to add", "manual" or "not built"); a proposed one-intake pilot (length, what each side provides, cost: no pilot charge proposed, no price set); copyable pre-arrival paragraph and orientation announcement; a QR code for the site (static SVG, generated once, verified to decode to the site address); a printable one-page staff guide; an escalation pathway; office FAQ (data, responsibility, usage, currency, maintenance, downtime); pilot measures marked available now / small addition / new functionality; and a pilot enquiry form (university, work email and topic required; role, intake size and message optional) with a confirmation saying who reads it and what happens next.
13. **Data page** ("What goes where", linked from the footer, the student FAQ and the universities page): one row per data flow (check, campus memory, map tiles, Google Maps route link, feedback, copied messages, AI check in the Claude version, pilot enquiries), what is not used, and why feedback can't be deleted per person. Described as how the site works, not a legal privacy notice.
12. **Learning loop (Session 7)**: see section 4a. The page reads `learned.json` and, only once it holds at least 10 reviewed answers, tags the warning signs students report most ("Often reported"), can show clearer wording that I approved, and says when a person last reviewed it. Tags never change the result level.

## 4. Data: what is stored and where

| Data | Stored? | Where | Who can read it |
|---|---|---|---|
| Answers to the 12 questions | No. Netlify Forms keeps only the feedback form. If the student sends feedback, it includes the names of the warning signs they answered Yes / Not sure to, never listing details. | Page memory only | Nobody |
| Screenshots | No | Browser only; sent to Claude only if the student taps the AI check | The student; Claude processes them for that one answer |
| Review entry, public site: warning-sign answer, rating, tags, comment, result level, which warning signs the student answered Yes or Not sure to (pattern names only, never listing details), number of screenshots, timestamp | Yes (since 25 October) | Netlify Forms, form `checkie-feedback`. **Netlify also records the submitter's IP address**, and this can't be turned off; the page says so. | Only me, in the Netlify dashboard. The public page can submit but cannot read submissions. |
| Review entry, Claude version: same fields | Yes | Claude's built-in artifact storage, at `feedback/<viewer id>/entries` | **Only me (owner)**. Rules: `feedback` read/write = owner; `feedback/{self}` read/write = interact. Tested: a normal user reads nothing. |
| Sign names in feedback | Only if the student leaves the box "Include which warning signs I answered Yes or Not sure to" ticked (ticked by default, explained next to it) | Netlify Forms, same entry | Only me |
| `learned.json` | Yes, public | Next to index.html | Anyone (counts and approved tags only; no individual answers) |
| Map tiles | No data stored | Loaded from OpenStreetMap, which sees the visitor's IP address like any website (stated in the Areas page sources line) | — |
| Chosen campus | Yes | The student's own `localStorage` | Only that student, on that device |
| Pilot enquiries (universities only): university, work email, topic; optional role, intake size, message | Yes, only when university staff send the "Request a demo" form | Netlify Forms, form `checkie-demo` (Netlify also records the IP address; the form says so) | Only me. Used only to reply about Checkie. |
| Feedback retention | Kept in Netlify Forms until I delete it | — | No fixed deletion schedule yet (stated on the site); see the trust audit for the proposed policy |
| Students' names, emails, listing URLs, landlord details | **Never collected** | — | — |

In block 1, AI drafted SQL for an insert-only Supabase table for the questionnaire answers. I was tight on time, so I left saving answers for after the hackathon. On 25 October I chose Netlify Forms instead of Supabase: the site is already on Netlify, it needs no extra account or keys in the page, and the public page can only submit, never read.

## 4a. Learning loop (Session 7)

| Step | What happens |
|---|---|
| Input | When a student sends feedback (and leaves the box ticked), the names of the signs they answered Yes and Not sure to. |
| Processing | Weekly, I download the Netlify CSV and run `loop/learn.py propose`. It counts Yes and Not sure for each of the 12 signs. |
| Learning | The script proposes: tag the top 3 signs (each with at least 3 Yes answers) as often reported; mark any question with 30% or more Not sure for rewording. Nothing is proposed below 10 answers. It warns about one-day spikes and unknown sign names. |
| **Human safety check** | `loop/learn.py approve`: I read `review.md` and accept or reject each change; I write any new wording by hand. Only approved changes reach `learned.json`, and only a redeploy makes them live. |
| Output | Tagged signs and clearer wording on the question screens, plus "Checkie last learned from N student answers, reviewed by a person on DATE". |
| Improvement | Measured by the Not sure rate on reworded questions and by how often students' flagged signs include a tagged sign. |

What the human catches: too few answers, spam or one group flooding the counts, and any change that would make a listing look safe or blame a nationality, area or named person. Cost: about 20 to 30 minutes a week of my time; €0.

Status (27 October): built and tested with made-up test data (`loop/test/`, every row marked TEST ROW). The live `learned.json` has 0 answers, so the site shows no tags yet. The red line: Checkie must never learn to call a listing safe or to judge a person.

## 5. User evidence so far (Guess 1)

| Who | When | How | Result |
|---|---|---|---|
| 5 international students | Before and during class, 13 October | Asked in conversation: "Have you come across scam warning signs while looking for a room?" | **2 of 5 said yes** |
| 15 students: 12 Esade exchange students, 3 UPF students | 25 October | I sent the link to exchange students I know, mostly classmates from my modules, and asked them to share it; I asked whether Checkie was useful for spotting warning signs | **12 of 15 had struggled and met scam warning signs**; they usually ask previous exchange students or seniors. 3 of 15 had no housing problems but saw the benefit for first-time students. Answers given verbally (I transcribed them) or by text. |

On 13 October the in-app question did not save answers, so those 5 answers came from conversation. On 25 October, 12 of 15 (80%) said they had met warning signs, above my 3-in-10 line, so Guess 1 holds for now. I keep the two groups separate because they may overlap. All 15 are my target users, but I reached them through people I know and collected answers through conversation and texts, so it is strong early support, not proof. No one has paid or signed up yet. Next: count the warning-sign answers saved in the app by students I don't know.

## 6. Security and privacy choices

- No API keys or secrets in the page.
- Netlify Forms: a honeypot field (`bot-field`) filters simple spam bots. The free plan allows 100 submissions a month.
- No personal data in the self-check. The review form asks students not to include names, phone numbers or addresses. On the public site, the page states that Netlify records the IP address of anyone who sends the review form.
- The AI is instructed never to call a listing safe, never to accuse a named person, and never to repeat personal data from the images.
- AI output is treated as untrusted text (`textContent` only). The AI has no tools and cannot act.
- Checkie never takes sponsorship or money from landlords, agencies or housing platforms.
- Checkie flags patterns and sites, **never named landlords**. Hosting accusations about people would create a worse harm than the one Checkie prevents (decision from Session 5).
- Known gap: someone with Contributor access could submit many review entries. This is acceptable at prototype scale.

## 7. What Checkie does NOT do

- It does not confirm that any listing is safe or legitimate.
- It does not store listings, addresses or landlord identities.
- It does not give legal advice. The one legal point (agency fees under Spain's 2023 housing law) is stated as general information, with "ask what any fee is for".
- It does not offer human review yet. With a partner university, a trained person would vet the screenshots students submit.
- The Netlify version does not run the AI check.

## 8. External sources and services

- Room prices: idealista (Q2 2026 room report), Uniplaces and CasaRadar (2026 guides). Residences and studios: Uniplaces and Uniscopio (2026), 3Cat (September 2025). Shown as approximate ranges.
- Map tiles: OpenStreetMap (attribution shown); Leaflet 1.9.4 (BSD-2-Clause) is included inside index.html, so no other script is loaded.
- Libre Caslon Text 700 (SIL Open Font License, from the @fontsource package) embedded in index.html for the wordmark; no font is loaded from Google.
- Google Maps links for exact routes. No Maps API is used.
- Claude via the artifact `sample` capability (Claude version only).

## 9. Change log

**Session 6, in class (13 October)**

*During the build blocks*
- Wrote the questionnaire: the scam warning signs to check and why each matters.
- Built a single-file prototype (goal: a student can answer the anonymous question in under 60 seconds, with no personal data collected): a 6-question check, result, an anonymous question card (not saving answers) and a local-only screenshot step (not connected to AI yet, which I said during the demo).
- Added a logo, illustrations and an animated street scene.
- Published it on Netlify during the demo.
- Asked 5 international students whether they had come across scam warning signs: 2 said yes.

*Later in the session, after my demo (based on feedback from my professors during the demo)*
- Expanded to 12 questions with clearer wording and examples.
- Up to 10 screenshots, and an AI screenshot check in the Claude version.
- Replaced the separate anonymous card with a review section (answers kept by Claude's built-in storage, in the Claude version only).
- Added the area & price guide with an accurate map, the campus travel check and the universities page.
- New logo and serif wordmark; clearer buttons.

**After the session (13 October)**
- Added "Need to ask a real person?": the student's university international office contact (officially published addresses only) and a ready-made message listing what was flagged.
- Clarified that human screenshot review comes with partner universities.

**25 October (for the Summary Document)**
- Connected the public site's review section to Netlify Forms, so the warning-sign answer is now saved and countable.
- Updated the privacy note: Netlify records the IP address of anyone who sends the review form.
- Each saved answer now also records which warning signs the student flagged (Yes / Not sure), so I can see which scam patterns are most common, not only how many students met one.
- Added a "Copy the Checkie link to share" button after the review is sent, to help reach more students.
- Enabled form detection, redeployed and confirmed a live test submission in the Netlify dashboard.
- Asked 15 students (12 Esade exchange, 3 UPF): 12 said they had met scam warning signs.

**27 October (Session 7)**
- Built learning loop version 1: `loop/learn.py` (propose, then human approve), `learned.json`, and the question-screen tag and "last reviewed" line.
- Added a ticked-by-default box so students can choose not to send which signs they flagged, and a "How Checkie learns" note next to the Send button.
- Linked Netlify to GitHub: every commit to `main` now deploys the live site automatically. Checked live: the tick box and "How Checkie learns" note show.
- Made the consent clearer: a boxed "Also send which warning signs I flagged" option with a "What exactly is sent?" fold-out that previews the student's own sign names, lists what is never sent, and explains how the counts are used. I chose this over a terms-and-conditions pop-up, which students tend to click through without reading.
- Added the price check (intro, price map and question 4), an interactive zoomable map with the campus pin (Sant Cugat and UAB now visible), area rows that expand in place, and an 8-step renting guide before the questionnaire.
- Full-width layout on computers: header with tabs across the page, a two-column home page, the price check and area list beside a sticky map, and two-column guide and universities pages; phones keep the single-column layout.
- Home page: "How it works" in 4 steps and a short FAQ (safety, what is saved, cost, already paid). Guide page: "Already paid and think it's a scam?" steps and a glossary of Spanish rental words. Inspired by the structure of scam-check sites such as Scamwise.
- Tabs shortened to Check · Areas · Guide, with "For universities" as a separate button; "Ask your university" can now be opened directly, without the check.
- Redesign: sticky tab bar, a tidier home page, the 12 questions on one page with small answer buttons, and a place-type choice in the price check (room, residence, studio).
- Universities page: free-for-students vs partner-university comparison and a "Request a demo" form (Netlify form `checkie-demo`). Decision: the student check stays free for everyone; universities pay for the partner extras, not for access.
- Fixed in testing: one sign name contains ";", so the script matches whole sign names instead of splitting on ";".

**28 October (redesign for students and universities)**
- Audited the site against the code; fixed documentation that no longer matched (component list, map description, Claude version).
- Home: clearer headline, one primary action, a secondary link to the guide, a trust row, and an FAQ answer on university affiliation; on phones the button now comes before the illustration.
- Result: each warning sign now shows why it matters and what to do; "not sure" signs show how to find out; a "What to do next" list links to the price check, your university and the "already paid" steps. Scoring unchanged.
- Public site: the AI box is hidden instead of showing an unavailable feature; the screenshot step has a clear "Skip" link.
- Universities page rebuilt: available-now vs planned, proposed pilot steps, copyable materials, data and responsibilities, pilot measures as hypotheses, cost with no price set, and a "Request a pilot conversation" form with a topic field. Human screenshot review is described as planned everywhere.
- Fixes after review: the screenshot step's "Last step" label had picked up the guide's card style (class clash) and now has its own style; the result page is centred on computers; the street scene no longer covers content on phones and now shows more of Barcelona (Montjuïc cable car, café terrace, Bicing bike, Torre Glòries, a yellow-and-black taxi, Arc de Triomf, palms, the beach).
- Student evaluation (28 October, later): "Why not just ask a senior, or a chatbot?" on the home page; an "Ask the landlord" message in English or Spanish on the result; the public site skips the screenshot step and the button says "See my result"; a "Send Checkie to a friend" share button on the result; "Who made Checkie?" in the FAQ and an independence line in the footer.
- Visual consistency: one palette across the site, logo and street scene (deep green, terracotta, ochre, sand); a logo without a background tile: a Modernista façade (wavy roof, three arched windows, terracotta balcony and door) in green line work, with an ochre check badge (also used as the browser-tab icon, built into the page); the street scene's off-palette blues and greys recoloured; the universities call-to-action band changed from a pastel gradient to the brand green with an ochre button.
- Street scene: small, slow movements (a cable car on the Montjuïc wire, swaying palms, drifting clouds, a seagull, café steam, a window light, a cat's tail, the sea) and a taxi driving along the road; all CSS, no extra files, and switched off for anyone who has reduced motion turned on.
- Universities page rewritten for an international office's concerns (liability, privacy, maintenance, evidence, pilot terms); QR code, printable staff guide, escalation pathway and a shorter enquiry form.
- Visual review: one design layer at the end of the stylesheet (type scale, section spacing, button hierarchy, focus, touch sizes). Pages no longer sit in a boxed container on phones either; "How it works" and "Why not…" are plain columns instead of cards; answer buttons are at least 44px tall; all four navigation items fit at 320px; every interactive element has a visible keyboard focus ring; university actions use dark terracotta so they never look like the student's main action. Removed references to a font (Inter) that was never loaded.
- Trust and privacy audit (see trust-audit.md): data-flow statements corrected (feedback includes the result level, screenshot count and, by default, flagged sign names; "anonymous" replaced by "no name or email"; retention stated); weekly-learning and "goes straight into the next update" claims removed; superlatives softened; an unsourced crime claim about El Raval replaced; commute estimate labelled in map pop-ups; pilot feedback summary clarified as covering all users; data page added; Google Fonts removed (font embedded), so the only third-party request is OpenStreetMap map tiles.
- Pre-deployment review of the home cards: Price check jumps to the price checker (focuses the rent box with a mouse or keyboard; on touch screens focuses the heading instead, so the keyboard doesn't pop up); Areas jumps to the map; both glow briefly (off with reduced motion). Removed unused code from the old one-question-per-screen layout that referred to elements that no longer exist.
- Home page decluttered: shorter intro and trust line, "How it works" as four short steps, the senior/chatbot comparison in three one-line points, shorter card text and more space between sections. Card destinations unchanged.
- Areas page reorganised: a "Check a rent" bar across the top; below it the campus picker and area list on the left and the map on the right (sticky on computers); area details open inside the list (no separate detail card); tapping an area on the map opens its row in the list (on phones without moving the page); "Other types of place" and "Before you pay" moved below.
- Home page information architecture rebuilt (see home-redesign.md): removed the separate "How it works", "Why not a senior or chatbot" and four-card "More ways" sections; their content now sits in the hero flow line, the FAQ and two grouped blocks; "I already paid" moved from the FAQ to the guidance links; added a three-column footer.
- Unchanged on purpose: scoring, the 12 questions, consent default, data collected, learning-loop rules, static architecture.

## 10. Next steps

1. Deploy index.html with learned.json, and keep sharing the link with students I don't know.
2. Once there are 10 real answers, run the first weekly review and publish the first approved learned.json.
3. Decide whether to add anonymous counts (visits, finished checks, which next step was used) to measure a pilot. Options: Netlify's server-side analytics (paid) or a count-only form; either changes what is collected, so it needs a decision and a privacy note first.
4. Approach Esade's international office about a pilot; a partner university's reviewer could take over the weekly human check.
5. If a pilot is agreed: a small server (e.g. a Netlify Function) holding a Claude API key, so the AI check works on the public site, with a spending limit and a privacy notice.
