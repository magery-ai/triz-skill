# Example: engineering - longer blades without the weight

- Domain: engineering
- Mode: guided

## Problem as the user stated it

> We want longer wind turbine blades to capture more energy, but every extra
> metre makes the blade heavier, which overloads the hub and bearings.

## Conversation

**Stage 1, intake:** The agent asks about the target, what was tried and the
limits. Blades are 60 m of glass fibre; the goal is 70 m. Carbon spar caps
helped but are too expensive for the whole blade. The hub can't take more
load this year, and road transport limits a single piece to about 60 m.
IFR: "the blade sweeps a bigger area by itself, with no added load on the
hub." Resources: the existing mould, carbon fibre (in small amounts), the
wind itself, the pitch system. The user confirms.

**Stage 2, contradiction:** Cause chain: hub overload, because blade mass and
root bending moment grow faster than length, because the whole blade is built
to one stiffness. TC: improving length (3 Length of moving object) worsens
weight (1 Weight of moving object). PC: the blade must be long (to capture
energy) and short (to keep mass and transport length down). The user agrees.

**Stage 3, directions:** Cell 3x1 gives #8 Anti-weight, #15 Dynamics,
#29 Pneumatics and hydraulics, #34 Discarding and recovering. The agent also
reads 14x1 (stiffness vs weight): #1 Segmentation, #8, #40 Composite
materials, #15. #8 and #15 appear twice. Separation in space also fits:
stiffness is needed along the spar, not across the whole shell, which adds
#3 Local quality.

**Stage 4, actions:**
1. Two-piece blade joined on site (#1). Solves transport; mass about the same.
   IFR fit medium, effort high.
2. Carbon only in the spar caps of the outer 10 m, glass elsewhere (#40, #3
   Local quality). IFR fit high, effort medium.
3. Bend-twist coupling: lay the fibres so the blade twists and sheds load in
   gusts (#15). Cuts peak hub load. IFR fit high, effort medium.

**Stage 5, validation:** "What new problem does bend-twist coupling create?"
The user worries about fatigue in the root. Answer: keep coupling to the outer
third and check with the existing fatigue model. "What would have to be true
for option 2 to fail?" Carbon supply. The user approves 2 plus 3.

## Short plan

**Short plan: 70 m blade without hub overload**
**Contradiction:** improving blade length worsens blade weight (long for energy, short for mass)
**Chosen solution:** carbon caps only in the outer 10 m plus bend-twist fibre layout (principles #40 Composite materials, #15 Dynamics)
**Next steps:**
1. Model root moment for a 70 m blade with outer carbon caps (structures team, 3 weeks)
2. Add bend-twist layup to the outer third and rerun the fatigue model (structures team, 6 weeks)
3. Price carbon for 10 m caps per blade (purchasing, 2 weeks)
**Watch for:** root fatigue margin below the current blade's
**Done when:** a 70 m design keeps hub load at or under today's 60 m blade

## What made this work

Reading two cells (length vs weight and stiffness vs weight) surfaced #15
twice, which pointed at shedding load instead of only cutting mass.
