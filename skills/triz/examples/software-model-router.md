# Example: software - halve the inference bill without worse answers

- Domain: software
- Mode: fast

## Problem as the user stated it

> Every customer chat goes to our largest model. The bill is $42k a month and
> finance wants it halved. We tried a smaller model for everything and wrong
> answers went from 3% to 9%. Just give me options.

## Conversation

**Stage 1, intake (fast):** One question: "What can't change?" The answer:
no drop in quality, so wrong answers stay at or below 3%, and no new vendor.
The agent folds stages 1 and 2 into one check. IFR: "every chat gets a
correct answer at the cost of the cheapest model that can give it, with no
extra work per chat." Resources: both models on the same API, ticket tags
on every chat, a labelled eval set of 500 past conversations, the help-center
articles, the existing wrong-answer review (2% of chats graded weekly).

**Stage 2, contradiction:** TC: improving serving cost (23 Loss of
substance) worsens answer reliability (27 Reliability). PC: the model must be
small (to be cheap) and large (to be right). The agent says how it mapped:
"I read the bill as running cost, 23, not 32 Ease of manufacture, whose cell
against 27 is empty both ways. Wasted compute on easy chats is a second
reading, 22 Loss of energy." The user confirms in one line.

**Stage 3, directions:** `--merge 23:27 22:27` gives #10 Preliminary action
and #35 Parameter changes twice each, then #11 Beforehand cushioning, #29 and
#39. Separation on condition fits the PC: large only for the chats that need
it. The eval set shows where: 70% of chats are order status, returns and
password resets, where the small model scores within 0.5 points of the large
one; billing disputes and multi-step troubleshooting are where it fails.

**Stage 4, actions:** Levers: share of chats on the small model (cost is
about 1/12 per chat), wrong-answer rate per route.
1. Route by ticket tag: the 3 easy categories go to the small model, the
   rest to the large one (#35, the model's size changes per request). At 70%
   on the small model, the bill falls to about $15k. IFR fit high, effort low.
2. Escalate on doubt: if the small model's answer cites no help-center
   article or the customer replies "that's wrong", the chat re-runs on the
   large model (#11, a fallback prepared in advance). Adds about 5% to the
   bill. IFR fit high, effort medium.
3. Pre-answer the 50 most common questions from the help center and refresh
   when an article changes (#10). Removes about 15% of model calls. IFR fit
   medium, effort medium.
Dropped: fine-tuning the small model. It needs data and time the team does
not have this quarter, and options 1-2 reach the target without it.

**Stage 5, validation (skippable, the user answers one):** "What if the
router sends a hard chat to the small model?" Option 2 catches the ones that
fail loudly. For the quiet ones, the weekly review samples small-model chats
separately, so their wrong-answer rate is visible on its own. The user
takes options 1 and 2 now and option 3 later.

## Short plan

**Short plan: halve the bill, same answer quality**
**Contradiction:** improving serving cost worsens answer reliability (the model must be small and large)
**Chosen solution:** route easy ticket types to the small model and escalate doubtful answers to the large one (principles #35 Parameter changes, #11 Beforehand cushioning)
**Next steps:**
1. Run the 500-chat eval set per ticket tag on both models and confirm the 3 easy categories (ML engineer, this week)
2. Ship tag routing behind a flag at 10% of traffic, then 100% (backend, in 2 weeks)
3. Add the escalate-on-doubt rule and split the weekly review by route (backend and support lead, in 3 weeks)
**Resources:** both models on the current API, ticket tags, the 500-chat eval set, the help center, the weekly wrong-answer review; new: nothing
**Watch for:** wrong-answer rate on the small-model route above 4% for a week, then move that ticket tag back to the large model
**Done when:** monthly bill at or below $21k with wrong answers at or below 3% for 4 weeks in a row, within 8 weeks

## What made this work

Reading the bill as 23 Loss of substance instead of 32 Ease of manufacture.
32 against 27 is empty both ways; 23 against 27 gave #35 and #11, which
became the router and its fallback.
