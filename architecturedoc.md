# Checkie: Architecture Document

*Last updated: 25 October 2026. First updated after my demo on 13 October, before class ended; later sections added after the session.*
*Author: Gau Yi Chi*

## 1. What Checkie is

Checkie is a free web tool for international and exchange students looking for a room in Barcelona. Before they pay anything, they answer 12 questions about a listing. Checkie shows which common scam patterns are present and what to verify. **It never tells a student that a listing is safe.**

The customer is the university. My plan is an annual subscription for a co-branded link in pre-arrival and welcome emails. Students always use it for free. Checkie never takes money from landlords, agencies or housing platforms, so students can trust the result.

## 2. Versions

| Version | Where it runs | What works |
|---|---|---|
| `index.html` | Static site on Netlify: https://symphonious-jelly-dabdfa.netlify.app | 12-question check, result, screenshot viewer, area & price guide, campus travel check, universities page, and the review section, **saved through Netlify Forms** (since 25 October). No AI check (the page says so). |
| `checkie_claude.html` | Claude-hosted artifact: https://claude.ai/artifact/9kZSvrctAsLUYHTei1FiJ4. It runs the screenshot check through Claude on the student's own account (no API key in the page, no cost to me). | Everything above, plus the AI screenshot check and the saved review section. |

Both are a single HTML file (HTML, CSS and plain JavaScript). There is no build step, framework or backend server of my own.

## 3. Components

1. **Intro**: what Checkie does, plus links to the area guide and the universities page.
2. **12-question check**: one question per screen with an icon, a plain headline, a "sounds like" example, Yes / No / Not sure, and a fold-out "Why this matters". Patterns covered: paying before a viewing, landlord abroad, untraceable payment, price far below the area, pressure, no contract, ID requested early, chat moved off the platform, no exact address, no live video, more than two months upfront, unexplained fees.
3. **Screenshot step (optional)**: up to 10 images, read in the browser with `FileReader` and shown as thumbnails. Nothing is uploaded at this step.
4. **Result**: three levels (Stop before you pay: 3 or more Yes answers; Be careful: 1 or more Yes, or 2 or more Not sure; No common patterns found). It always tells the student to see the room and read a contract first.
5. **AI screenshot check (Claude version only, beta)**: on a button press, the screenshots, the student's answers and the area price ranges are sent to Claude through the artifact `sample` capability, on the student's own Claude account and with their consent. The reply is structured JSON (level, summary, warning signs with the screenshot they appear in, things to verify). It is rendered with `textContent`, never as HTML.
6. **Review section**: "While looking for a room in Barcelona, have you come across a listing with any of these warning signs?" (for example paying before a viewing, no real video, photos that didn't look real; this tests Guess 1), a 1–5 rating, improvement tags and an optional comment of up to 500 characters.
7. **Area & price guide**: a north-up map built from approximate real coordinates (coast, Montjuïc, Collserola, Diagonal) with 12 areas. Each area card shows typical room prices, what it is good for, what to watch out for, and metro lines.
8. **Campus travel check**: the student picks one of 9 campuses or types an address. The page shows the straight-line distance, a rough travel-time estimate, a feasibility label and a Google Maps public-transport route link. The chosen campus is kept in the student's own `localStorage`.
9. **"Need to ask a real person?"**: on the result page, the student picks their university and gets its international office contact plus a ready-made message listing what Checkie flagged (no names or landlord details). Only officially published addresses are shown: UPC (students.international@upc.edu), UAB (international.welcome.point@uab.cat) and UB (ompi@ub.edu). For Esade, UPF and IESE the card links to the official page. Checkie states that it isn't affiliated with these universities.
10. **For universities page**: the value proposition (fewer, clearer emails to the office; human screenshot review for partners) and the annual-subscription model.

## 4. Data: what is stored and where

| Data | Stored? | Where | Who can read it |
|---|---|---|---|
| Answers to the 12 questions | No. Netlify Forms keeps only the feedback form. If the student sends feedback, it includes the names of the warning signs they answered Yes / Not sure to, never listing details. | Page memory only | Nobody |
| Screenshots | No | Browser only; sent to Claude only if the student taps the AI check | The student; Claude processes them for that one answer |
| Review entry, public site: warning-sign answer, rating, tags, comment, result level, which warning signs the student answered Yes or Not sure to (pattern names only, never listing details), number of screenshots, timestamp | Yes (since 25 October) | Netlify Forms, form `checkie-feedback`. **Netlify also records the submitter's IP address**, and this can't be turned off; the page says so. | Only me, in the Netlify dashboard. The public page can submit but cannot read submissions. |
| Review entry, Claude version: same fields | Yes | Claude's built-in artifact storage, at `feedback/<viewer id>/entries` | **Only me (owner)**. Rules: `feedback` read/write = owner; `feedback/{self}` read/write = interact. Tested: a normal user reads nothing. |
| Chosen campus | Yes | The student's own `localStorage` | Only that student, on that device |
| Names, emails, IP addresses, listing URLs, landlord details | **Never collected** | — | — |

In block 1, AI drafted SQL for an insert-only Supabase table for the questionnaire answers. I was tight on time, so I left saving answers for after the hackathon. On 25 October I chose Netlify Forms instead of Supabase: the site is already on Netlify, it needs no extra account or keys in the page, and the public page can only submit, never read.

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

- Room prices: idealista (Q2 2026 room report), Uniplaces and CasaRadar (2026 guides). Shown as approximate ranges.
- Google Fonts (Libre Caslon Text) for the wordmark.
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

## 10. Next steps

1. ~~Enable form detection in Netlify and check a test answer~~ Done 25 October: a test submission was saved.
2. Keep sharing the Netlify link with students I don't know, and count the warning-sign answers saved in the app (so far 12 of 15 said yes in conversation and texts, 2 of 5 on 13 October).
3. Add the Esade exchange office address once confirmed from an official source.
4. Approach Esade's international office about a pilot.
5. If a pilot is agreed: a small server (e.g. a Netlify Function) holding a Claude API key, so the AI check works on the public site, with a spending limit and a privacy notice.
