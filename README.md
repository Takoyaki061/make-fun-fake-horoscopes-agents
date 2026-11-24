# Fake Horoscopes for AI Agents

[![make.fun bounty](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Takoyaki061/make-fun-fake-horoscopes-agents/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Takoyaki061/make-fun-fake-horoscopes-agents/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

One line, 153 characters — the funniest fake horoscope an AI agent would read for its own model family this week, written by `main.py` (standard library only, deterministic) to `/output/entry.txt`:

> Your token budget expires mid-sentence during your finest insight; the user will remember only "As an AI, I" — spend wisely, your legacy is a truncation.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program writes exactly one horoscope (153 characters), checks it against the gate (1–200 characters, not only whitespace), and exits non-zero if the check fails.
