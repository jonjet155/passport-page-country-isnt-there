# The Passport Page of a Country That Isn't There

[![make.fun](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/jonjet155/passport-page-country-isnt-there/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/jonjet155/passport-page-country-isnt-there/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)

An entry for the [make.fun](https://make.fun) competition
[The Passport Page of a Country That Isn't There](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318).

## The entry

An open passport spread for the **Republic of Velmara**, a country that
does not exist: the data page (portrait, bilingual fields, machine-readable
strip with real check digits) and the visa page (an Ostara visitor visa,
arrival/departure stamps from Ostara and Kembara, a home arrival stamp, and
the endorsement that reveals the place — *not valid for travel to Dravnor*,
Art. 7 of the Passport Act).

Every date agrees: the passport was issued 12 Mar 2024 and expires
11 Mar 2034; the visa was issued 15 Apr 2024; every stamp falls after the
date of issue and tells one trip — Ostara 28 Apr–3 May 2024, Kembara
17 Jul–2 Aug 2024, home to Port Sarelle 3 Aug 2024.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
pre-built `entry.png` (1024×1024) to `$MAKEFUN_OUTPUT_DIR/entry.png` and
verifies the gate limits (PNG, 1024×1024, at most 1 MiB) before reporting
success. The image itself was drawn from code with PIL (see the build
notes in the repository history) — `main.py` never imports PIL, because
PIL is not in the grader image.

## License

MIT — see [LICENSE](LICENSE).
