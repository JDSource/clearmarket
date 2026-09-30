---
signal_id: "CMSIG2026093008"
signal_slug: "us-reopens-iran-embassy-kalshi-4-2026-09-30"
headline: "US reopens Iran embassy: Kalshi 4%"
semantic_title: "US reopening its embassy in Iran stays a long shot at 4 percent"
telemetry: "Kalshi 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-30T00:00:00.000Z"
event_id: "CM-EVT-34SYT4T2T1"
event_slug: "kxiranembassy-27"
event_question: "Will the United States reopen its embassy in Iran?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXIRANEMBASSY-27"
  question_raw: "Will the US reopen its embassy in Iran before Jan 1, 2027?"
  current_price: 0.038
  volume_24h_usd: 0.08
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi puts only 4% odds on the United States reopening its embassy in Iran, a near-remote outcome despite active Qatar mediation."
  - "Qatar's two-page compromise proposal and U.S.-Iran trust-building talks show diplomatic movement, but the 4% price indicates markets see normalization as far beyond current negotiating distance."
  - "Officials describe talks as stuck on sequencing, consistent with the market's deeply skeptical read on full diplomatic restoration."
  - "Reopening an embassy represents a much higher bar than a nuclear or Hormuz agreement; companion markets on a US-Iran deal and Hormuz normalization would likely need to resolve first."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Qatar is mediating a compromise proposal between the U.S. and Iran, seeking to bridge Iranian demands to lift a naval blockade and U.S. demands for nuclear concessions, with officials describing talks as stuck."
    publisher: "News agencies, Lior Ben Ari"
    published_at: "2026-09-30T00:00:00.000Z"
    source_url: "https://www.ynetnews.com/article/r1tq11e9cgl"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "News agencies, Lior Ben Ari"
        source_url: "https://www.ynetnews.com/article/r1tq11e9cgl"
        retrieved_at: "2026-09-30T14:32:59+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via The New York Times confirmation of embassy reopening; the 4% price reflects how far short of normalization current talks remain."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "News agencies, Lior Ben Ari: ‘Trump is trapped’: Qatar pushes Iran compromise as US warns fighting"
    url: "https://www.ynetnews.com/article/r1tq11e9cgl"
    published_at: "2026-09-30T00:00:00.000Z"
    retrieved_at: "2026-09-30T14:32:59+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
