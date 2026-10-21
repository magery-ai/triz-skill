# Evals

Three layers, from cheapest to most expensive.

## 1. Data and structure tests (CI)

```bash
python -m unittest discover -s evals/tests -v
```

These check the data files, the lookup script, SKILL.md structure, the
mapping guide, the question bank, and that every case in `cases/` cites the
right matrix cells. They run on every pull request.

## 2. Trigger tests

`triggers.yaml` holds 20 prompts that should start the skill and 10 that
should not. Run them with the skill-creator's description optimizer, or by
hand: start a fresh agent session with only this skill installed, send each
prompt, and record whether the skill loaded. Tune the `description` in
SKILL.md until all should-trigger prompts load it and no should-not prompt
does.

## 3. Scenario evals

Each file in `cases/` has:

- `prompt`: the user's first message.
- `persona`: instructions for a simulated user who answers the agent's
  questions consistently (`none` for autonomous cases).
- `expected_contradictions`: acceptable contradictions, with the parameters
  and the matrix cell for each.
- `checks`: case-specific pass conditions.

To run a case:

1. Start two agent sessions: one with the skill installed, one without.
2. In each, send `prompt`. Have a second agent (or a person) play the
   persona and answer every question the agent asks.
3. Grade both transcripts with `rubric.md`.
4. Compare the two. The skill should win on contradiction, lookup, context use
   and validation. Fix the stage file behind the item that fails most often.

There are 10 guided or fast cases (4 engineering, 3 software, 2 business,
1 personal) and 3 autonomous cases. Add a case for each bug found in real use.
