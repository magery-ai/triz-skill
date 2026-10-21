# Stage 1: Intake

**Goal:** understand the problem well enough to state it back in one paragraph,
describe the ideal result, and know what the user already has to work with.

## Steps

1. **Let the user describe the problem** in their own words. If they already
   did, do not ask again; start at step 2.
2. **Ask 3-5 clarifying questions, one at a time.** Pick the ones the user's
   description leaves open, in this order of priority:
   - **Goal:** "What would success look like? Is there a number or a date?"
   - **History:** "What have you already tried, and what happened?"
   - **Constraints:** "What limits do you have: time, money, people, tools?"
   - **Fixed points:** "What must not change, whatever we do?"
   - **Stakeholders:** "Who is affected, and who decides?"
   - **Scale:** "How often does this happen, and how big is the cost when it does?"

   Skip a question when the answer is already clear. Stop at 5 even if gaps
   remain; note the gaps as open questions in the state block.
3. **Restate the problem** in one paragraph: who, what goes wrong, how much it
   costs, what has been tried, and the target.
4. **Write the Ideal Final Result (IFR).** See below.
5. **List resources** with the checklist below.
6. **Update the state block** and run the gate.

## Writing the IFR

The IFR describes the result as if the problem solved itself. Use this form:

> The system <delivers the wanted result> by itself, with no added cost,
> complexity or harm.

- Name the **result**, not a solution. "Customers get a correct answer at
  once" is a result; "a chatbot answers customers" is a solution.
- Keep "by itself": it pushes later stages toward using what is already there.
- If the IFR sounds impossible, that is fine. It is a direction, not a promise.
  Stage 4 scores actions by how close they get to it.

Examples:

| Problem | IFR |
|---------|-----|
| A turbine blade must be light but stiff | The blade stays stiff in any wind with no added weight |
| A cache serves stale data | Users always see fresh data at cache speed, with no extra load on the database |
| Support replies are fast but sloppy | Every customer gets a correct answer at once, with no extra staff |
| No time to exercise | Exercise happens as part of the day, with no time taken from anything else |

## Resource checklist

Ask yourself, and the user where needed, what already exists in or around the
problem. Resources that are free, idle or wasted are the most valuable.

- **Things:** parts, tools, equipment, products, code, documents.
- **People:** who has the skill, time or motive to help, including customers.
- **Time:** idle periods, slack before or after the critical moment, off-peak hours.
- **Space:** unused room, capacity, slots, channels.
- **Energy and fields:** heat, motion, gravity, attention, momentum, habits.
- **Information:** data already collected, logs, history, feedback, patterns.
- **By-products and waste:** anything the system already produces and throws
  away, including complaints and failed attempts.
- **Money:** budget that is already allocated, even if earmarked elsewhere.

## Output

```
Problem: <one paragraph restatement>
IFR: <the system does X by itself, with no added cost or harm>
Resources: <list>
Constraints: <list, including what must not change>
Open questions: <gaps the user could not or did not answer>
```

## Gate

Show the restatement, IFR and resources, then ask: "Is that right? Anything to
correct or add?" Do not continue until the user confirms. If they correct it,
update the state block and ask again only if the correction was large.

In fast mode, combine this gate with the stage 2 gate: show the restatement
and the contradiction together and ask once.
