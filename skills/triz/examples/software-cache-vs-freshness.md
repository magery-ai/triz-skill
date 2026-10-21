# Example: software - fast pages with fresh prices

- Domain: software
- Mode: guided

## Problem as the user stated it

> Our product pages are fast because of a 10-minute cache, but customers see
> wrong prices and stock after changes.

## Conversation

**Stage 1, intake:** Without the cache, p95 latency goes from 80 ms to 900 ms.
About 200 price changes a day, all from one admin tool. The database can't
take more read load. IFR: "every page shows current prices at cache speed,
with no extra load on the database." Resources: the admin tool, the cache,
the CDN, the change events the admin tool already writes to an audit log.
The user confirms.

**Stage 2, contradiction:** TC: improving response time (25 Loss of time)
worsens freshness (24 Loss of information). PC: the cached page must stay
(to be fast) and must change (to be fresh). Confirmed.

**Stage 3, directions:** The agent maps freshness to 24 and says so. Merging
25x24 and 9x24 gives #26 Copying (x2), then #24 Intermediary, #28, #32 and
#13. Separation in time fits: the page should be stable between changes and
change at the moment of a change, not every 10 minutes.

**Stage 4, actions:**
1. The admin tool sends a purge for the product's URLs when a price changes,
   using the audit log events it already writes (#24). IFR fit high, effort low.
2. Cache the page without price and stock, and fill those from a tiny
   per-product endpoint cached for 5 seconds (#26, #1 Segmentation). IFR fit
   high, effort medium.
3. Shorter TTL. Dropped: it trades freshness for load and breaks the database
   constraint.

**Stage 5, validation:** "What happens if a purge fails?" The page stays stale
for up to 10 minutes, as today. Answer: keep the TTL as a fallback and alert on
purge errors. "Who would object?" The CDN bill owner; purges are free on their
plan. The user approves option 1 now and option 2 for the next quarter.

## Short plan

**Short plan: fresh prices at cache speed**
**Contradiction:** improving response time worsens data freshness (page must stay and must change)
**Chosen solution:** purge on change from the admin tool, keep TTL as fallback (principles #24 Intermediary, #26 Copying)
**Next steps:**
1. Add a purge call to the admin tool's save handler (backend, this sprint)
2. Alert when a purge fails (backend, this sprint)
3. Spike the split page with a 5-second price fragment (backend, next quarter, proposed)
**Watch for:** purge error rate above 0.1%
**Done when:** stale-price complaints drop to zero with p95 still under 100 ms

## What made this work

Mapping freshness to "loss of information" instead of "reliability" led to a
cell with #24 and #26, which fit the cache directly.
