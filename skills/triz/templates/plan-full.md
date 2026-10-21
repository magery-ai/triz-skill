# TRIZ plan: <problem in 6 words>

- Date: <YYYY-MM-DD>
- Mode: <guided | fast | autonomous>
- Validated: <yes | skipped (fast mode) | critic pass (autonomous)>

## Short plan

<paste the short plan here>

## 1. Problem statement and IFR

<one paragraph restatement>

**Ideal Final Result:** <the system does X by itself, with no added cost or harm>

## 2. Resources and constraints

- Resources: <things, people, time, information, by-products>
- Constraints: <time, money, people, tools, what must not change>

## 3. Contradiction analysis

- Cause chain: <symptom> because <cause> because <root cause>
- Technical contradiction: improving <A> worsens <B>
- Physical contradiction: <E must be P and not-P>
- Parameter mapping: improving <id name>, worsening <id name>

## 4. Directions considered

| Source | Principle | Why it fits |
|--------|-----------|-------------|
| Matrix cell <row x col> | #<n> <name> | <one line> |
| Separation in <time/space/condition/system level> | #<n> <name> | <one line> |

## 5. Options and scoring

| Option | Principle | IFR fit | Effort | Side effects |
|--------|-----------|---------|--------|--------------|
| <action> | #<n> | <high/medium/low> | <low/medium/high> | <notes> |

Why the winner won: <reason>

## 6. Validation log

| Question type | Question | Answer | Change made |
|---------------|----------|--------|-------------|
| <type> | <question> | <answer> | <change> |

## 7. Action plan

| Step | Owner | Date | Depends on |
|------|-------|------|------------|
| <step> | <who> | <when> | <step> |

## 8. Risks and fallbacks

- Secondary contradiction: <improving C worsens D>; next principle to try: #<n> <name>

## 9. Resources, watch for, done when

These three fields are required. Each one must be checkable without asking
anyone's opinion: a number, a threshold, or a yes/no fact.

**Resources**

| Resource | Exists or new | Cost or effort | Used in step |
|----------|---------------|----------------|--------------|
| <resource from section 2> | exists | <none or small> | <step> |
| <anything the plan adds> | new | <cost> | <step> |

**Watch for**

| Risk | Signal and threshold | Where to look | What to do if crossed |
|------|----------------------|---------------|-----------------------|
| <top risk> | <metric above or below a number> | <dashboard, log, person> | <fallback from section 8> |

**Done when**

| Metric | Baseline | Target | By |
|--------|----------|--------|----|
| <metric tied to the IFR> | <today's value, or "unknown"> | <number> | <date> |

- Review on: <date>

## Assumptions (autonomous mode only)

- <assumption>

**Confidence:** <high | medium | low>
