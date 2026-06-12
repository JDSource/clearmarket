---
signal_id: "CMSIG2026061103"
signal_slug: "aug-2026-cpi-mom-implied-0-3-0-4-kalshi-ladder-2026-06-11"
headline: "Aug 2026 CPI MoM implied 0.3-0.4%: Kalshi ladder"
semantic_title: "August CPI month-over-month consensus anchors near 0.3 to 0.4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-11T20:48:22.000Z"
event_id: "CM-EVT-D057W6W251"
event_slug: "kxcpi-26aug"
event_question: "August 2026 CPI month-over-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26AUG-T0.4"
  question_raw: "Will CPI rise more than 0.4% in August 2026?"
  current_price: 0.45
  volume_24h_usd: 0.45
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-09-11T13:56:00Z"
bullets:
  - "Kalshi ladder implies August 2026 CPI MoM in the 0.3-0.4% range: 61% above 0.3%, 45% above 0.4%, 35% above 0.5%."
  - "May PPI at 6.5% YoY and upstream energy pressure are broadly consistent with elevated forward CPI readings priced into the August ladder."
  - "The 35% probability above 0.5% reflects a live upside tail, Iran war energy pass-through into consumer prices has not yet fully resolved."
  - "Resolves via the Bureau of Labor Statistics official CPI release for August 2026; the trimmed-mean ladder structure means each strike settles independently."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May PPI rose 6.5% year-over-year and initial jobless claims came in above consensus at 229K, signaling labor softening alongside persistent upstream price pressure."
    publisher: "aimsfx.com"
    published_at: "2026-06-11T20:48:22.000Z"
    source_url: "https://aimsfx.com/2026/06/11/u-s-labor-market-shows-signs-of-weakening-amid-inflationary-pressures-as-unemployment-claims-rise-and-ppi-exceeds-expectations/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aimsfx.com"
        source_url: "https://aimsfx.com/2026/06/11/u-s-labor-market-shows-signs-of-weakening-amid-inflationary-pressures-as-unemployment-claims-rise-and-ppi-exceeds-expectations/"
        retrieved_at: "2026-06-12T11:42:07+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distributes probability across MoM CPI strikes; the 0.3-0.4% implied range is the modal outcome given current energy and labor data inputs."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aimsfx.com: U.S. labor market shows signs of weakening amid inflationary pressures"
    url: "https://aimsfx.com/2026/06/11/u-s-labor-market-shows-signs-of-weakening-amid-inflationary-pressures-as-unemployment-claims-rise-and-ppi-exceeds-expectations/"
    published_at: "2026-06-11T20:48:22.000Z"
    retrieved_at: "2026-06-12T11:42:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
