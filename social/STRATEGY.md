# X strategy — World State Forecast (@WorldStateFC)

This file governs every public post, reply and image. It overrides older drafts, the Execution Book's templates and any habit of the drafting agent.

## Position

**We put a number on what happens next, and we keep score.** The account reads like a news desk that gives the odds: one event, one number, one clear reason. The track record is the brand, so results, hits and misses alike, are posted as prominently as forecasts.

## The rule behind every post

**One post = one story = one number = one image.** If a reader cannot repeat the post in one sentence after three seconds, it is not ready.

- Lead with the news or the question. Never lead with us, the project or the process.
- Plain words only. On X there are no question IDs, no edition numbers, no "AGG_RT", no "lens", "registry", "stage", "resolve", "frozen in commit", no file paths. Say "our forecast", "we locked it on 9 Oct", "it happened", "it didn't".
- Numbers as people say them: 18%, $120, €2.24, 3 killed. Dates as "Wed 28 Oct", "by 31 Dec".
- At most 3 short lines plus the number line. Aim for 200 characters, never more than 280.
- Every word must earn its place: cut the qualifiers, the disclaimers and the restated context. The bio, the pinned post and the site carry "AI-assisted, human-reviewed" and "not advice", so posts do not.
- No link in the post itself. One link, if it adds something (the primary source, or the brief on release days), goes in the first reply.
- No hashtags, no emoji, no tagging of big accounts, no threads longer than 4 posts.
- Neutral and confident. No sides, no sarcasm, no hype ("breaking", "huge"), no hedging stacks.
- Avoid machine tells: "Here's…", "Let's…", "🧵", "It's worth noting", "In a world where", "not X but Y", colon-then-reveal openers, lists of three adjectives, the same opening twice in a week.

## The seven formats (use no others)

| Format | When | Post shape | Image |
|---|---|---|---|
| **Call** | 1–3 days before a decision, vote or deadline people are watching | Question · "Our forecast: NN%." · one-line reason · when we'll know | `call` card: the question, the big number, "Decided: <day>" |
| **Result** | As soon as the outcome is official | **Quote-post your own Call** (the timestamp is the proof). What happened · what we had · "Called it." or "Missed." | `result` card: question, our number, HAPPENED / DID NOT HAPPEN |
| **Shift** | A verified new fact cuts against one of our numbers | The fact (dated) · our current number · which way it pushes · when we update | none, or the `call` card of that question |
| **Week ahead** | Monday | "Three things to watch this week:" · three lines "<event>, <day>: NN%" | `week` card, the same three lines |
| **Connection** | Thursday, at most weekly | A "why" headline · 2–3 dated steps · the number that would move | `chain` card, the same steps |
| **Big picture** | Friday after an edition | One-sentence state of the world · three numbers to 31 Dec · up to 3 replies, one storyline each with its region card · last reply: the brief | `edition` card, then the region cards |
| **Scorecard** | Tuesday after a release | Settled so far · our accuracy score vs a "nothing changes" guess (lower is better) · best call · worst miss | `score` card |

**Replies** (10 minutes a day under bigger accounts) follow the same rule: one fact with its date, or our number in plain words, in one or two lines. No link unless asked, never our site unprompted, never "great point", never an argument.

## What we post about

Three storylines carry the account, so followers know what to expect: **Iran, oil and shipping** · **Russia, Ukraine and NATO** · **USA–China**. Elections and central banks appear when they are scheduled news.

A question earns a post when it is (1) in the news this week, (2) settled within about 14 days, and (3) understandable by anyone in one line. Technical questions (canal slots, customs tonnage, local fuel quotes) stay in the report and are never posted on their own.

## Examples (edition 02 values)

Call:
> Will Brazil re-elect Lula on Sunday?
>
> Our forecast: 29%.
>
> Flávio Bolsonaro led the first round 47.0% to 45.2%.

Week ahead:
> Three things to watch this week:
>
> Bank of Russia cuts rates, Fri: 14%
> Lula wins Brazil's runoff, Sun: 29%
> Bulgaria elects Iotova outright, Sun: 27%

Big picture (post 1):
> The land war with Iran is paused. The sea war around Hormuz is not.
>
> Our forecasts to 31 Dec:
> US strike on Iran: 35%
> US–Iran deal that reopens Hormuz: 16%
> Brent above $120: 23%

Scorecard:
> 17 of our forecasts have now settled.
>
> Our accuracy score: 0.117. A "nothing changes" guess: 0.302. Lower is better.
>
> Worst miss: a Houthi attack on Riyadh that we rated unlikely. It happened.

Reply under a post saying a US–Iran deal is close:
> Talks are still indirect, through Qatar. We put a deal that reopens Hormuz by 31 Dec at 16%.

## Images

Rendered by `tools/brief.py card …` (or by stage E for the edition and region cards). One message per image, matching its post word for word where they overlap: a headline of at most 8 words, one big number or at most three rows, one context line, and the footer "World State Forecast · locked <date>" with the site address. Nothing else: no IDs, no hashes, no file paths, no "+N more", no tables.

## Rhythm

One slot, weekdays at 20:30 Warsaw (US midday): one own post and 10 minutes of replies. Nothing at weekends. Results go out the first evening after the outcome.

| | Normal week | Edition week |
|---|---|---|
| Mon | Week ahead | Week ahead |
| Tue | Call (the week's biggest event) | Scorecard of the last edition, or a Call |
| Wed | Shift or Result | Start the edition; a Result only if one is due |
| Thu | Connection or Call | Verify and publish; no post unless a Result is due |
| Fri | Result, or the weekly review | Big picture |

## Rules that never bend

- Only published official numbers, rounded to whole percent; never a new probability, never a lens value. A Shift says which way, never a new number.
- The draft file records, for every number, the question ID, edition and value, and for every fact its date, publisher and URL. The post itself carries none of that.
- Facts are checked on the day of posting against a primary source; a government statement is reported as a statement.
- A result is "Called it" when our number was above 50% and it happened, or below 50% and it didn't; otherwise "Missed". Exactly 50% is "a coin flip". The formal score comes later, with the next edition.
- Never quote, name or link outlets on `sources/harvest/no_republish.txt`. Never mention crowd or market forecasts.
- The user posts every word by hand. Nothing is automated.

## Measuring

Every Friday without a release, compare views, replies, profile visits and follows by format. After four weeks, keep the two best formats at full weight and halve the weakest.
