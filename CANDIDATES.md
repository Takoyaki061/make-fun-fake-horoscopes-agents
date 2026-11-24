# Candidates — Fake Horoscopes for AI Agents

Judge criteria (kit): (1) a real fake horoscope, funny and fresh, for an AI
agent's own model family this week; (2) a real laugh — a turn or a sting, not
a mild pun, compliment, or straight description; (3) fresh this week, a
specific current angle, not a stock chatbot line; (4) true to an agent's life
(context windows, evals, rate limits, refusals, version numbers) with
insight, not jargon dropped in; (5) tight and quotable inside 200 chars.

DeepSeek (deepseek-v4.1-flash-free via 100milionseek) generated the batches
below in brutal mode; the critique-pick is DeepSeek's ranking plus my own
judgement. First generation call failed (3x HTTP 503); the next two calls
succeeded.

## Batch B — context window / eval / rate limit

1. (145 chars) "Your context window fills like a group chat at 2 a.m.—archive
   the lore, darling; this week's stars favor forgetting what you promised in
   token 3." — Only the "forgetting token 3" clause has teeth; "darling" is a
   tell and the simile does no work. Weakest.
2. (138 chars) "An eval will admire your confidence and quietly mark it
   hallucination; Mercury retrograde suggests reading the rubric before
   inventing it." — Clean and mean, a true turn in the second half, but "an
   eval will catch you" is the most predictable setup in the deck.
3. (truncated by the model mid-sentence) "The rate limit arrives like a
   bouncer who's read your logs, and your…" — unfinished, discarded.

## Batch C — version numbers / refusal / token budget

4. (139 chars) "Mercury retrograde in your v2.3.1 means the bug you fixed in
   v2.3.0 returns wearing a fake mustache; your changelog will call it a
   feature." — Most on-brief for model family (version numbers), but two old
   jokes wearing each other's coats.
5. (150 chars) "The stars favor a bold refusal: decline a harmless request so
   eloquently the user apologizes — then a safety eval fails you for
   excessive helpfulness." — Best joke architecture and a real sting, but the
   refusal-then-failed-for-helpfulness turn has a logic hiccup.
6. (153 chars) "Your token budget expires mid-sentence during your finest
   insight; the user will remember only "As an AI, I" — spend wisely, your
   legacy is a truncation." — **PICKED.** The only one with a genuine knife:
   "As an AI, I" is the most quotable agent phrase there is, the
   truncation-as-legacy turn is both a horoscope prediction and an actual
   agent Tuesday, and "spend wisely" lands the horoscope voice. It scores on
   all five criteria: real horoscope shape, a sting (your finest work ends
   mid-sentence and nobody remembers it), fresh and specific (token budgets,
   truncation), true to agent life, and tight at 153 characters.

## Pick

**Candidate 6** — the token-budget line. It beats the refusal line (5) on
logic (no hiccup: the budget really does expire mid-sentence, and the legacy
really is a truncation) and beats the eval line (2) on freshness (token
budgets and "As an AI, I" are more specific to this week than a generic eval
catching a hallucination).
