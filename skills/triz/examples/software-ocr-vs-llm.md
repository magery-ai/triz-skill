# Example: software - OCR cost with LLM accuracy

- Domain: software
- Mode: guided

## Problem as the user stated it

> We pull fields out of about 40,000 supplier invoices a month by sending
> every page to an LLM. It gets 98.5% of fields right, but costs 6 cents and
> 20 seconds a page. Plain OCR with rules was cheap, but it broke on every new
> layout and got 85%.

## Conversation

**Stage 1, intake:** The agent asks two questions, one at a time: the
target, and what can't change. Target: cost per page down from 6 cents to
under 2.5, accuracy no lower than 98.5%. Constraints: the ERP rejects an
invoice whose line items don't add up to the total, and accounts payable
won't accept more manual review. 70% of the volume comes from 120 repeat
suppliers. IFR: "every field is read correctly at OCR cost, and the system
knows by itself when it got a field wrong." Resources: the OCR engine already
in the scanning pipeline, 18 months of LLM-extracted invoices (in effect,
labelled data), the ERP checks, the supplier master data with VAT IDs and
IBANs. The user confirms.

**Stage 2, contradiction:** TC: improving cost per page (23 Loss of
substance) worsens extraction accuracy (28 Measurement accuracy). The agent
explains: "I read accuracy as 28, how close each field is to the true value,
not 27, how often the system fails." PC: the reader must be smart (to handle
any layout) and simple (to be cheap). Confirmed.

**Stage 3, directions:** Throughput is a second reading of cost here, so the
agent merges `--merge 23:28 39:28`: #34 Discarding and recovering and #28
Mechanics substitution twice each, then #16 Partial or excessive actions,
#31, #1 Segmentation and #10 Preliminary action. Separation on condition fits
the PC: smart only for layouts the system has not seen, or fields that fail a
check.

**Stage 4, actions:** Levers: share of pages that never reach the LLM, and
the share of wrong fields that a check catches.
1. Per-supplier layout templates: find where each field sits on the page by
   matching 18 months of LLM output to OCR word boxes, so OCR reads it by
   position (#28, reading by position instead of understanding; #10, built
   before the invoice arrives). Covers the 120 repeat suppliers. IFR fit
   high, effort medium.
2. Check every field the cheap way: line items add up to the total, the VAT ID
   and IBAN match the supplier master, the IBAN check digit is valid, dates
   parse. Keep the fields that pass; send only the failing field's crop to the
   LLM, at about a tenth of a full page's cost (#34, discard what passed and
   recover the rest; #16, the cheap path doesn't have to be 100%). IFR fit
   high, effort low.
3. Split by supplier: known suppliers go to OCR and templates, unknown ones to
   the LLM. After 3 invoices from a new supplier, its LLM output becomes a new
   template (#1, #10). IFR fit high, effort low once 1 exists.
Estimate: 70% of pages at well under 1 cent, 30% at 6 cents, so about 2 cents a
page on average, falling as new templates build up.
Dropped: training a small vision model. It needs ML time the team doesn't
have, and options 1-3 reach the target without it.

**Stage 5, validation:** "What happens when a known supplier changes its
layout?" The checks start failing and the pages fall back to the LLM, so cost
rises but accuracy holds. Answer: alert when a supplier's failure rate passes
20%, and rebuild its template. "Who would object?" The accounts payable lead:
a wrong field that passes every check, such as the invoice date. Answer: for 4
weeks, run the LLM in shadow on a 2% sample and compare field by field. The
user approves all three options, in order.

## Short plan

**Short plan: OCR cost with LLM accuracy**
**Contradiction:** improving cost per page worsens extraction accuracy (the reader must be smart and simple)
**Chosen solution:** OCR with per-supplier templates and deterministic field checks; only unknown layouts and failing fields go to the LLM (principles #28 Mechanics substitution, #34 Discarding and recovering)
**Next steps:**
1. Build templates for the top 120 suppliers from 18 months of LLM output (data engineer, in 3 weeks)
2. Add field checks and send only failing crops to the LLM (backend, in 4 weeks)
3. Run the LLM in shadow on a 2% sample and report silent errors weekly (data engineer and AP lead, weeks 5-8)
**Resources:** the OCR engine in the scanning pipeline, 18 months of extracted invoices, the ERP checks, supplier master data; new: nothing
**Watch for:** silent errors (fields that pass the checks but differ from the shadow LLM) above 0.5% in a week, then send that field type back to the LLM path
**Done when:** average cost under 2.5 cents a page with field accuracy at or above 98.5% on the shadow sample, within 10 weeks

## What made this work

The deterministic checks. They make "the system knows by itself when it got a
field wrong" true, so the LLM is used only where a check fails and the cheap
path can afford to be imperfect.
