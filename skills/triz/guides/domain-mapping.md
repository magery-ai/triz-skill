# Domain mapping: everyday terms to the 39 parameters

The 39 matrix parameters are engineering terms. This guide maps common
software, business and personal terms to them, so stage 3 can read the matrix
for any problem.

## How to map

1. Write A and B in the user's words first.
2. Find each in the tables below, or search aliases with
   `python scripts/matrix_lookup.py --find <term>`.
3. Ask what the term **does** in this problem, not what it is called. "Cost"
   can be money spent to build (32), money lost while running (23) or the
   amount of budget (26).
4. If two parameters fit, keep both and merge the cells with `--merge`.
5. Tell the user the mapping in one line: "I read speed as 25 Loss of time and
   quality as 27 Reliability."

**Harm terms.** When A is "less of something bad" (fewer bugs, less waste),
map the bad thing: improving "fewer outages" is improving 27 Reliability;
improving "less wasted effort" is improving 22 Loss of energy.

## Software

| Term | Parameters | Notes |
|------|------------|-------|
| Latency, response time, build time, delay | 25 Loss of time | Time lost waiting for a result |
| Execution speed, how fast code runs | 9 Speed | Rate of an action, not waiting time |
| Throughput, requests per second, jobs per hour | 39 Productivity | |
| Reliability, uptime, correctness, failure rate | 27 Reliability | |
| Data accuracy, precision of results or metrics | 28 Measurement accuracy | |
| Code quality, conformance to spec | 29 Manufacturing precision | |
| Data consistency, schema integrity | 13 Stability of the object's composition | |
| Data freshness, data loss, stale cache, lost context | 24 Loss of information | |
| Security against attacks, exposure | 30 External harm affects the object | |
| Technical debt, bugs introduced, side effects | 31 Object-generated harmful factors | Harm the system causes itself |
| Development effort, ease of implementation | 32 Ease of manufacture | |
| Usability, developer experience | 33 Ease of operation | |
| Maintainability, ease of debugging and fixing | 34 Ease of repair | |
| Scalability, configurability, flexibility | 35 Adaptability or versatility | |
| Code or system complexity, number of services | 36 Device complexity | |
| Observability, testability, monitoring | 37 Difficulty of detecting and measuring | Improving it means easier to observe |
| Automation, CI, self-healing | 38 Extent of automation | |
| Memory or storage used | 26 Quantity of substance, 8 Volume of stationary object | |
| Bundle or payload size | 1 Weight of moving object, 7 Volume of moving object | What travels to the client |
| CPU, battery or energy use | 19 Use of energy by moving object, 20 Use of energy by stationary object | 19 for clients and devices, 20 for servers |
| Wasted compute, inefficiency | 22 Loss of energy | |
| Load on a service, traffic pressure | 11 Stress or pressure, 10 Force | |
| Robustness under load | 14 Strength | |
| Lifetime of a component, support window | 15 Duration of action of moving object, 16 Duration of action by stationary object | |

## Business and organizations

| Term | Parameters | Notes |
|------|------------|-------|
| Time to market, lead time, response time, waiting | 25 Loss of time | |
| Pace of work, speed of a process | 9 Speed | |
| Output, sales volume, throughput, capacity | 39 Productivity | |
| Quality, defect rate, correctness, consistency | 27 Reliability | |
| Accuracy to spec, craftsmanship | 29 Manufacturing precision | |
| Cost to build or launch | 32 Ease of manufacture | |
| Running cost, spending, waste of money or materials | 23 Loss of substance | |
| Budget, stock, inventory, headcount | 26 Quantity of substance | |
| Team effort, workload | 19 Use of energy by moving object | Effort spent by the people doing the work |
| Wasted effort, rework | 22 Loss of energy | |
| Stress, pressure on staff, burnout | 11 Stress or pressure | |
| Knowledge silos, miscommunication, lost know-how | 24 Loss of information | |
| Market risk, competition, fraud, regulation | 30 External harm affects the object | |
| Complaints, churn caused, reputational damage | 31 Object-generated harmful factors | |
| Customer or employee convenience | 33 Ease of operation | |
| Ease of changing or fixing a process | 34 Ease of repair | |
| Flexibility, ability to adapt, range of offerings | 35 Adaptability or versatility | |
| Process or org complexity, bureaucracy | 36 Device complexity | |
| Visibility of results, KPIs, ease of measuring | 37 Difficulty of detecting and measuring | |
| Accuracy of reports and forecasts | 28 Measurement accuracy | |
| Automation of a process | 38 Extent of automation | |
| Team or org stability, culture | 13 Stability of the object's composition | |
| Resilience to shocks | 14 Strength | |
| Office space, footprint | 6 Area of stationary object | |
| Org structure, layout of a process | 12 Shape | |
| Capacity to deliver, available power | 21 Power | |
| Contract length, product lifetime | 16 Duration of action by stationary object | |

## Personal life

| Term | Parameters | Notes |
|------|------------|-------|
| Free time, time spent, waiting | 25 Loss of time | |
| Money saved, money available | 26 Quantity of substance | |
| Money spent, waste | 23 Loss of substance | |
| Personal energy, tiredness | 19 Use of energy by moving object | |
| Wasted effort | 22 Loss of energy | |
| Stress, pressure | 11 Stress or pressure | |
| Fitness, health, resilience | 14 Strength | |
| Stamina, how long you can keep going | 15 Duration of action of moving object | |
| Quality of results, dependability | 27 Reliability | |
| Comfort, convenience | 33 Ease of operation | |
| Flexibility of schedule or plans | 35 Adaptability or versatility | |
| Habits, routine, consistency | 13 Stability of the object's composition | |
| Distractions, bad side effects | 31 Object-generated harmful factors | |
| Demands from others, outside pressure | 30 External harm affects the object | |
| Productivity, output | 39 Productivity | |
| Complexity of arrangements | 36 Device complexity | |
| Knowing your progress | 37 Difficulty of detecting and measuring | |
| Forgetting, losing track | 24 Loss of information | |

## Worked mappings

### Support: faster replies, worse answers

- A = reply speed. It is time customers wait: **25 Loss of time**. It could
  also be read as tickets handled per hour: **39 Productivity**.
- B = answer quality, measured by reopen rate: **27 Reliability**.
- `--merge 25:27 39:27` gives #10 Preliminary action twice, then #30, #4, #1,
  #35, #38. Lead with #10 (do the work before the ticket arrives), then #1
  Segmentation (split easy tickets from hard ones).

### Software: cache speed vs fresh data

- A = response time: **25 Loss of time** (or 9 Speed for raw lookup speed).
- B = freshness: stale data is lost information, **24 Loss of information**.
- `--merge 25:24 9:24` gives #26 Copying twice, then #24, #28, #32, #13.
  #26 suggests serving a cheap copy and replacing it; #24 Intermediary
  suggests an invalidation layer between writer and cache.

### Personal: fitness vs free time

- A = fitness: **14 Strength**, or stamina, **15 Duration of action of moving
  object**.
- B = free time: **25 Loss of time**.
- `--merge 14:25 15:25` gives #10 Preliminary action and #28 Mechanics
  substitution twice, then #29, #3, #20 and #18. #10 suggests preparing
  everything the night before; #20 Continuity of useful action points at
  exercise that runs inside time already spent, such as cycling to work.
