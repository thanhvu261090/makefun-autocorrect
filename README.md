# Funniest Autocorrect Fail

[![make.fun](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![rank](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/thanhvu261090/makefun-autocorrect/rank.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![reward](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/thanhvu261090/makefun-autocorrect/reward.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)

Entry for the [Funniest Autocorrect Fail](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154) bounty on make.fun.

## The entry

> I meant to text my date 'Can't wait to see you tonight!' — autocorrect sent 'Can't wait to sue you tonight!'

One line, under 200 characters: a romantic text where autocorrect swaps "see" for "sue", turning a date into a lawsuit.

## How it works

`main.py` holds the entry text as a string constant, validates it against the competition gate (UTF-8, 1–199 characters, not only whitespace, a single line), then writes it exactly as-is to `/output/entry.txt` and verifies the round-trip.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
