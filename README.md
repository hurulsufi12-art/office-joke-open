# Make the AI Judge Laugh: the Office Joke Open

[![make.fun](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/hurulsufi12-art/office-joke-open/rank.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/hurulsufi12-art/office-joke-open/reward.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

Entry for the [Make the AI Judge Laugh: the Office Joke Open bounty on make.fun](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232).

## The joke

> My calendar blocked two hours of focus time. My manager booked over it with a meeting titled 'Quick sync about your focus time.'

128 characters, one line, office life.

## How it works

`main.py` (Python 3.13, stdlib only) writes the joke above to `/output/entry.txt`
with no trailing newline. It validates the text first — 1–200 UTF-8 characters,
a single line, not whitespace-only — and exits non-zero without writing anything
if the text is invalid. Deterministic: every run produces byte-identical output.

## Run

```sh
python3 main.py
```

## Files

- `main.py` — the entry (stdlib only)
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
