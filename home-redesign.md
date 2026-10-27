# Home page redesign

*28 October 2026 · Gau Yi Chi · with Claude*

## Five reasons it felt scattered (before)

1. **Three look-alike grids in a row.** "How it works" (4 items), "Why not a senior or a chatbot" (3) and "More ways Checkie helps" (4 cards) had the same visual weight, so nothing told the eye which mattered. Students skimmed past all three.
2. **Repetition.** The 12 questions were explained in the intro and again in "How it works". "Ask a real person" appeared as a step and again as a card. The FAQ's "Is it free?" and "Who made it?" repeated the trust line.
3. **Tools, guidance and help mixed together.** The four cards put two tools (price, areas) next to a help route (ask your university) and a reading page (guide), so the student had to work out what each was for.
4. **Trust information spread out.** Pieces were in the trust row, the chatbot comparison, the FAQ and the footer. No single place said "what Checkie can and can't do".
5. **A thin footer.** It held one sentence, so supporting pages (data, universities, guide) were only reachable through the menu or buried links.

## New structure (one journey)

| Order | Student question | What's there |
|---|---|---|
| 1 | What is it, and why care? | Headline + one sentence |
| 2 | What do I do first? | One filled button: "Check a listing · 2 minutes"; the three-step flow in one line underneath; Free · No sign-up · Nothing saved unless you send feedback |
| 3 | What else can it do? | **Also useful before you pay**: two tools only (Check a rent, Explore areas) |
| 4 | I need more guidance | **Need more guidance?**: a plain list of links (renting guide, ask your university, already paid). A different visual pattern from the tools, so the two don't compete. |
| 5 | Can I trust it? | **What Checkie can and can't do**: three statements (warning signs, not verdicts; privacy with a link to "What goes where"; independence), then the student FAQ, folded |
| 6 | I'm from a university | The "For universities" button in the header and a footer column; nothing on the student page competes with the main action |

**Layout:** after the hero, each block is a ruled row, with the heading on the left on computers and the content on the right. There's one card style (the two tools) and one list style (guidance). On phones everything is a single column, in the same order.

## Moved, merged or removed

| Before | Now |
|---|---|
| "How it works" (4 cards) | One line under the button. "Ask a real person" lives in the guidance list. |
| "Why not just ask a senior, or a chatbot?" (3 columns) | One FAQ answer, with the same points |
| "More ways Checkie helps" (4 cards) | Split by purpose: 2 tools + guidance links |
| FAQ "I already paid. What now?" | "Already paid and worried?" in the guidance list (more visible) |
| Footer sentence | Three-column footer on every page: For students, For universities, About (data and privacy, source and documentation), plus the independence line |

Nothing was removed outright, and no safety guidance was hidden. All the FAQ answers, the data page link and the "never safe" statement are still on the home page.

## Tests (headless Chrome)

- **Every home link** at 1440px and 390px opens the right page or section:
  - renting guide, ask your university, already paid (lands on the steps),
  - "What goes where",
  - "Read how to rent safely".
- **Every footer link** opens the right page or section: check, rent, areas, guide, ask, universities, pilot form, data and privacy. GitHub link checked.
- **Tool cards:** Check a rent lands on the rent checker (the rent box is focused with a mouse; the heading on touch). Explore areas lands on the map. Both glow briefly, and the glow is off with reduced motion.
- **Keyboard:** Tab reaches the tool card and Enter works.
- **The home page has exactly one filled button.** The FAQ opens.
- **No sideways scroll** at 320, 390, 768 and 1440px.
- **Regression:** questionnaire, scoring, result, landlord message, share, feedback, pilot form, "Ask your university" and screenshots all pass. No console errors.

**Not verified:** real phones and screen readers.

## Files to deploy

`index.html`, `architecturedoc.md`, `ai-orchestration-log.md`, `README.md`, `home-redesign.md`
