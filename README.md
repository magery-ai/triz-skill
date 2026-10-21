# TRIZ skill for AI agents

An open-source [agent skill](https://agentskills.io) that teaches an AI agent
to solve stuck problems with TRIZ, the theory of inventive problem solving. It
finds the contradiction behind your problem, uses the 40 inventive principles
and the classic Altshuller contradiction matrix to find solution directions,
turns them into actions that fit your situation, checks them with you, and
hands back a short plan and a full one.

> **Status: v0.4 evals and examples.** The workflow, data, lookup script,
> scenario evals and three worked examples are in. The matrix is cross-checked
> between two copies; see the [roadmap](#roadmap) for what comes next.

## What a session looks like

> **You:** Our support team has to answer tickets faster, but every time we
> push for speed the answers get sloppier and customers write back.
>
> **Agent:** Let's work through this with TRIZ. First, a few questions, one at
> a time. What does "fast" mean for you today, and what is the target?
>
> **You:** First reply takes about 9 hours. We want under 1 hour.
>
> **Agent:** What have you already tried?
>
> **You:** We set a 1-hour target. Replies got faster, but reopen rates went
> from 8% to 19%.
>
> **Agent:** What can't change? For example headcount, tools or tone.
>
> **You:** No new hires this year. We use Zendesk. Senior agents are our best
> asset.
>
> **Agent:** Here's my restatement. A team of fixed size has to cut first reply
> time from 9 hours to under 1 hour without raising the reopen rate above 8%.
> **Ideal result:** every customer gets a correct answer at once, with no extra
> staff. **Resources:** Zendesk macros and triggers, ticket history, senior
> agents' knowledge. Is that right?
>
> **You:** Yes.
>
> **Agent:** The contradiction: improving **speed** (parameter 25, Loss of
> time) worsens **reliability** (27, Reliability) of the answers. In physical
> form: the reply must be *instant*, so agents don't investigate, and
> *considered*, so it is correct. Does that match what you see?
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
> **Watch for:** reopen rate on macro tickets above 8%
> **Done when:** median first reply under 1 hour with reopen rate at or below 8%
>
> I saved the full plan, with the analysis, options and validation log, to
> `triz-plans/2026-10-21-support-speed-vs-quality.md`.

The principles come from the matrix cells 25x27 (#10, #30, #4) and 39x27
(#1, #35, #10, #38). The full walkthrough is in
[`skills/triz/examples/business-support-speed-vs-quality.md`](skills/triz/examples/business-support-speed-vs-quality.md).

## Install

With the [skills CLI](https://skills.sh):

```bash
npx skills add magery-ai/triz-skill --skill triz
```

Or copy the folder by hand (Claude Code shown; other agents use their own
skills folder):

```bash
git clone https://github.com/magery-ai/triz-skill
cp -r triz-skill/skills/triz ~/.claude/skills/
```

A Claude Code plugin marketplace entry (`/plugin marketplace add
magery-ai/triz-skill`) and a release zip for Claude.ai come with v1.0.

## How it works

The skill runs six stages and stops at the gates to check with you:

1. **Intake:** clarify the problem, write the Ideal Final Result, list resources.
   *Gate: you confirm the restatement.*
2. **Contradiction:** find the "improving A worsens B" conflict at the root.
   *Gate: you pick or correct it.*
3. **Directions:** look up the contradiction matrix and separation principles.
4. **Actions:** turn each principle into concrete steps that use your resources.
5. **Validation:** Socratic questions, one at a time, until you approve an
   option. *Gate: your approval.*
6. **Plan:** a short plan in chat, and a full plan saved to
   `triz-plans/YYYY-MM-DD-<slug>.md` in your project.

Three modes:

- **Guided** (default): every gate.
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
  *(this release)*
- **v1.0 Release:** matrix verified against Altshuller's *40 Principles*
  (Shulyak and Rodman, 1997), plugin marketplace entry, release zip.

## Sources

The skill uses only the classic 1971 Altshuller 39x39 contradiction matrix and
the 40 inventive principles. Descriptions and data are written in this
project's own words and format.

Matrix values come from the [triz40.com](https://www.triz40.com/aff_Matrix_TRIZ.php)
online matrix (Source: TRIZ40 - www.triz40.com), cross-checked cell by cell
against a second copy. Differences are logged in
`skills/triz/data/matrix-discrepancies.md`. The primary reference for the
v1.0 check is Altshuller's *40 Principles* (Shulyak and Rodman, 1997).

## License

[MIT](LICENSE)
