# TRIZ skill for AI agents

An open-source [agent skill](https://agentskills.io) that teaches an AI agent
to solve stuck problems with TRIZ, the theory of inventive problem solving. It
finds the contradiction behind your problem, uses the 40 inventive principles
and the classic Altshuller contradiction matrix to find solution directions,
turns them into actions that fit your situation, checks them with you, and
hands back a short plan and a full one.

> **Status: v1.0.** Workflow, data, lookup script, evals and worked examples
> are in. The matrix is cross-checked against three copies but not yet
> against the book; see [Sources](#sources).

## What a session looks like

> **You:** Our support team has to answer tickets faster, but every time we
> push for speed the answers get sloppier and customers write back.
>
> **Agent:** Let's work through this with TRIZ. Two quick questions first,
> one at a time. What does "fast" mean for you today, and what is the target?
>
> **You:** First reply takes about 9 hours. We want under 1 hour.
>
> **Agent:** What have you already tried, and what can't change?
>
> **You:** We set a 1-hour target. Replies got faster, but reopen rates went
> from 8% to 19%. No new hires this year, we use Zendesk, and senior agents
> are our best asset.
>
> **Agent:** Here's my restatement. A team of fixed size has to cut first reply
> time from 9 hours to under 1 hour without raising the reopen rate above 8%.
> **Ideal result:** every customer gets a correct answer at once, with no extra
> staff. **Resources:** Zendesk macros and triggers, ticket history, senior
> agents' knowledge.
>
> The contradiction behind it: improving **speed** (parameter 25, Loss of
> time) worsens **reliability** (27, Reliability) of the answers. In physical
> form: the reply must be *instant*, so agents don't investigate, and
> *considered*, so it is correct. Is that the problem, and does the conflict
> match what you see?
>
> **You:** Exactly that.
>
> **Agent:** Speed here is the time customers wait (25, Loss of time) or
> tickets handled per hour (39, Productivity). Reading both matrix cells against
> 27 Reliability, #10 shows up in both, so I'll lead with it, then #1 from
> the second cell:
> - **#10 Preliminary action:** do the investigating before the ticket arrives.
> - **#1 Segmentation:** split tickets that can be answered instantly from those
>   that can't.
>
> Concrete options, ranked:
> 1. Seniors write and own macros for the 20 most common ticket types, which
>    cover about 60% of volume (#10). Low effort, high fit.
> 2. A Zendesk trigger routes tickets that match a macro to an "instant" queue
>    and everything else to "investigate", with an honest 4-hour promise (#1).
> 3. An intake form asks for the order number and a screenshot before a human
>    sees the ticket (#10).
>
> One question before we commit: who would object to option 1, and why?
>
> **You:** Seniors might hate writing canned replies.
>
> **Agent:** What if they own them instead: each senior maintains five macros
> and reviews reopen data for them weekly? Does that answer the objection?
>
> **You:** Yes, they'd like owning the quality numbers.
>
> **Agent:**
> **Short plan: support speed without losing quality**
> **Contradiction:** improving speed worsens answer reliability
> **Chosen solution:** senior-owned macros plus split queues (#10, #1)
> **Next steps:**
> 1. Pull the top 20 ticket types from last quarter (team lead, Friday)
> 2. Each senior writes and owns five macros (seniors, in 2 weeks)
> 3. Add the instant/investigate trigger in Zendesk (admin, in 2 weeks)
>
> **Resources:** Zendesk macros and triggers, last quarter's ticket history, seniors' time (about 2 hours each); new: nothing
> **Watch for:** reopen rate on macro tickets above 8% for a week, then pull that macro for review
> **Done when:** median first reply under 1 hour with reopen rate at or below 8%, within 6 weeks
>
> I saved the full plan, with the analysis, options and validation log, to
> `triz-plans/2026-10-21-support-speed-vs-quality.md`.

The principles come from the matrix cells 25x27 (#10, #30, #4) and 39x27
(#1, #35, #10, #38). The full walkthrough is in
[`skills/triz/examples/business-support-speed-vs-quality.md`](skills/triz/examples/business-support-speed-vs-quality.md).

## Install

**Claude Code** (plugin marketplace):

```
/plugin marketplace add magery-ai/triz-skill
/plugin install triz@triz-skill
```

**Claude.ai:** download `triz-skill-<version>.zip` from the
[latest release](https://github.com/magery-ai/triz-skill/releases/latest) and
upload it under Settings > Capabilities > Skills.

**Any agent** with the [skills CLI](https://skills.sh):

```bash
npx skills add magery-ai/triz-skill --skill triz
```

Or copy the folder by hand (Claude Code shown; other agents use their own
skills folder):

```bash
git clone https://github.com/magery-ai/triz-skill
cp -r triz-skill/skills/triz ~/.claude/skills/
```

## How it works

The skill runs six stages and stops at the gates to check with you:

1. **Intake:** up to two clarifying questions, then the Ideal Final Result and
   resources. *Gate: you confirm the restatement (asked together with stage 2
   when nothing is left to resolve).*
2. **Contradiction:** find the "improving A worsens B" conflict at the root.
   *Gate: you pick or correct it.*
3. **Directions:** look up the contradiction matrix and separation principles.
4. **Actions:** turn each principle into concrete steps that use your resources.
5. **Validation:** two Socratic questions, one at a time, then you approve an
   option. Ask for more if you want them. *Gate: your approval.*
6. **Plan:** a short plan in chat, and a full plan saved to
   `triz-plans/YYYY-MM-DD-<slug>.md` in your project. Every plan has three
   required fields: **Resources** (what it uses, and anything new with its
   cost), **Watch for** (the top risk, a measurable signal, and what to do)
   and **Done when** (a metric, a target and a date).

A guided session takes about 5-8 of your replies.

Three modes:

- **Guided** (default): every gate, at most two questions per gate.
- **Fast:** say "just give me options"; one check, and you can skip validation.
- **Autonomous:** for agents with no human in the loop; the agent answers the
  gates itself, lists its assumptions and flags low-confidence plans for review.

## Repository layout

```
skills/triz/
├── SKILL.md            # trigger, rules, stage map, modes, state block
├── workflow/           # one file per stage, plus autonomous.md
├── guides/             # domain-mapping.md: software, business, personal terms
├── templates/          # plan-short.md, plan-full.md
├── data/               # parameters, principles, matrix, separation, check status
├── scripts/            # matrix_lookup.py (standard library only)
└── examples/           # worked examples, plus TEMPLATE.md
.claude-plugin/         # marketplace.json for Claude Code
tools/build_zip.py      # builds the Claude.ai release zip
evals/
├── cases/              # 13 scenario cases (10 guided or fast, 3 autonomous)
├── triggers.yaml       # should / should-not trigger prompts
├── rubric.md           # how to grade a run
└── tests/              # data, script, structure and case tests, run in CI
```

Run the tests with `python -m unittest discover -s evals/tests`. See
[`evals/README.md`](evals/README.md) for trigger tests and scenario evals.

## Contributing

Worked examples, eval cases and matrix corrections are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md); to report a wrong matrix cell, open a
[Wrong matrix cell](https://github.com/magery-ai/triz-skill/issues/new?template=wrong-matrix-cell.yml)
issue.

## Roadmap

- **v0.1 Skeleton:** SKILL.md, draft workflow, templates.
- **v0.2 Data:** 39 parameters, 40 principles, 39x39 matrix, separation
  principles, lookup script, data tests and CI.
- **v0.3 Workflow:** full stage files, domain-mapping guide for non-engineering
  problems, Socratic question bank.
- **v0.4 Evals and examples:** scenario evals, trigger tests, worked examples.
- **v1.0 Release:** plugin marketplace entry, release zip, matrix status
  documented. *(this release)*

Next: a cell-by-cell check of the matrix against Altshuller's *40 Principles*
(Shulyak and Rodman, 1997), and recorded with/without eval runs.

## Sources

The skill uses only the classic 1971 Altshuller 39x39 contradiction matrix and
the 40 inventive principles. Descriptions and data are written in this
project's own words and format.

Matrix values come from the [triz40.com](https://www.triz40.com/aff_Matrix_TRIZ.php)
online matrix (Source: TRIZ40 - www.triz40.com), cross-checked cell by cell
against a second copy. Differences are logged in
`skills/triz/data/matrix-discrepancies.md`. A third copy with a documented
origin, the table on the [G.S. Altshuller Foundation](https://www.altshuller.ru/triz/technique2.asp)
site (from Altshuller's *Algorithm of Invention*, 1973), agrees on 1,492 of
1,521 cells; the 29 cells where it differs are marked `disputed`, and the
lookup script says so. The cells have **not** yet been checked against the primary
reference, Altshuller's *40 Principles* (Shulyak and Rodman, 1997);
`skills/triz/data/matrix-status.json` tracks each cell's status. If you have
the book and find a difference, please open a
[Wrong matrix cell](https://github.com/magery-ai/triz-skill/issues/new?template=wrong-matrix-cell.yml)
issue.

## License

[MIT](LICENSE)
