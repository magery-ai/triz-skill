# TRIZ problem solving (compact rules)

This is the compact version of the TRIZ skill for agents that read a rules
file (`AGENTS.md`, Cursor rules, Copilot instructions, Windsurf, Cline) but
cannot load skills. The full skill is in
https://github.com/magery-ai/triz-skill. If `skills/triz/SKILL.md` is
available, use it instead of this file.

## When to use

Use these rules when the user faces a trade-off or a stuck problem
("improving A makes B worse", "it must be both X and not X"), or asks for
TRIZ, the 40 inventive principles or the contradiction matrix. Do not use
them for factual questions, plain execution tasks or problems with an
obvious answer.

## Rules

1. Ask one question at a time and wait for the answer.
2. Never skip the contradiction check. A wrong contradiction invalidates
   everything after it.
3. Principles are directions, not answers. Every action must use something
   from the user's situation: a resource, a constraint, a person or a tool.
4. Always cite principles by number and name, for example "#10 Preliminary
   action". Explain a TRIZ term the first time you use it.
5. Aim for a plan in about 5-8 user replies. Ask more only when the user asks.

## Stages

1. **Intake.** Ask at most two clarifying questions: what the target is, and
   what was tried and can't change. Restate the problem, the Ideal Final
   Result ("the system does X by itself, at no extra cost") and the resources.
   *Check: the user confirms the restatement.*
2. **Contradiction.** Name the conflict as "improving A worsens B", map A and
   B to two of the 39 TRIZ parameters, and give the physical form when there
   is one ("E must be P and not-P"). *Check: the user picks or corrects it.*
   You can ask the stage 1 and stage 2 checks together.
3. **Directions.** Look up the matrix cell (row = improving parameter,
   column = worsening parameter). If A or B fits two parameters, read both
   cells and lead with principles that appear in both. If the cell is empty,
   try the reverse cell, then the closest neighbour parameter. For a
   physical contradiction, also try separation in time, in space, on
   condition, and between the system and its parts. Pick 3-6 principles.
4. **Actions.** Turn each principle into a concrete step that uses the
   user's resources. Rank the options and recommend the top 2-3.
5. **Validation.** Ask at most two Socratic questions, one at a time, such
   as "Who would object to this, and why?" or "What happens if this goes
   wrong?". *Check: the user approves an option.* A new conflict sends you
   back to stage 2; a missing constraint sends you back to stage 4.
6. **Plan.** Give the short plan below in chat. If you can write files, save
   a fuller version, with the analysis and the validation log, to
   `triz-plans/YYYY-MM-DD-<slug>.md` in the user's project.

If the user says "just give me options", ask at most one question, do one
combined check for stages 1 and 2, and let them skip validation. If no human
can answer (you are a subagent or stuck mid-task), answer the checks yourself
and list every assumption you made.

## Short plan

```
**Short plan: <problem in 6 words>**
**Contradiction:** improving <A> worsens <B> (<physical form, if any>)
**Chosen solution:** <one sentence> (principles #<n> <name>, #<m> <name>)
**Next steps:**
1. <action> (<who>, <by when>)
2. <action> (<who>, <by when>)
3. <action> (<who>, <by when>)
**Resources:** <what exists>; new: <anything new and its cost, or "nothing new">
**Watch for:** <top risk>: <signal and threshold>, then <what to do>
**Done when:** <metric> <target> by <date>
```

## Data

Read the data from the repository. If it is not on disk, fetch the raw files:

- Matrix, 39x39 (row = improving, column = worsening, cell = principle ids
  separated by `;`):
  https://raw.githubusercontent.com/magery-ai/triz-skill/main/skills/triz/data/contradiction-matrix.csv
- The 39 parameters with aliases for software, business and personal terms:
  https://raw.githubusercontent.com/magery-ai/triz-skill/main/skills/triz/data/parameters.json
- The 40 principles with definitions and examples:
  https://raw.githubusercontent.com/magery-ai/triz-skill/main/skills/triz/data/principles.json
- Separation principles for physical contradictions:
  https://raw.githubusercontent.com/magery-ai/triz-skill/main/skills/triz/data/separation.json
- Mapping everyday terms to parameters:
  https://raw.githubusercontent.com/magery-ai/triz-skill/main/skills/triz/guides/domain-mapping.md

If you can do neither, say so and use the principles you know, marking each
one as not checked against the matrix. Never invent a matrix value.
