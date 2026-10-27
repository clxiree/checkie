# Checkie

A free scam-pattern check for international and exchange students renting a room in Barcelona. Students answer 12 questions about a listing before paying; Checkie shows which common scam patterns are present and what to verify. It never says a listing is safe.

- Live site: https://symphonious-jelly-dabdfa.netlify.app
- AI version (screenshot check through Claude on the student's own account): https://claude.ai/artifact/9kZSvrctAsLUYHTei1FiJ4

## Files
- `index.html`: the whole app (HTML, CSS and plain JavaScript, no build step). Feedback is saved through Netlify Forms.
- `architecturedoc.md`: components, data stored, security choices, change log.
- `scope.md`: riskiest guess, goal, what is in and out of scope.
- `ai-orchestration-log.md`: AI Orchestration Log.
- `learned.json`: what the site has learned, approved by a person (empty until 10 real answers).
- `loop/`: the learning loop script and how to run it.
- `redesign-report.md`: 28 October audit, redesign decisions and test report.
- `student-evaluation.md`: the site evaluated as a new exchange student, the five fixes, and how to test them.
- `university-and-design-review.md`: the international-office review, pilot proposal and visual review.
- `trust-audit.md`: trust, privacy and credibility audit, fixes and open decisions.
- `home-redesign.md`: home page information architecture: problems, new structure, what moved.

## Deploy
Drag a folder containing `index.html` and `learned.json` onto Netlify. Forms detection is already on.

Author: Gau Yi Chi (Esade, Session 6 hackathon)
