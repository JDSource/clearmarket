---
signal_id: "CMSIG2026081108"
signal_slug: "wi-dem-gov-primary-2nd-place-called-kalshi-1-2026-08-11"
headline: "WI Dem Gov primary 2nd place called: Kalshi 1%"
semantic_title: "Wisconsin Democratic governor primary second place stays near certain to be decided"
telemetry: "Kalshi 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-11T14:06:40.503Z"
event_id: "CM-EVT-C2VSFP4N78"
event_slug: "kxwidgov2nd-govwinomd26-2"
event_question: "Will the second-place finisher in the Wisconsin Democratic Governor primary be decided by August 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXWIDGOV2ND-GOVWINOMD26-2-DCRO"
  question_raw: "Will David Crowley finish 2nd in the 2026 Wisconsin Democratic gubernatorial primary?"
  current_price: 0.01
  volume_24h_usd: 61.37
  arbitration_model: "kalshi_staff"
  resolution_source: "official election authority responsible for certifying results in geography"
  resolves_at: "2027-08-11T14:00:00Z"
bullets:
  - "The Kalshi contract prices only a 1% chance the second-place finisher in the Wisconsin Democratic governor primary remains undecided past the certification deadline."
  - "A too-close-to-call race between Hong and Crowley is in tension with that near-certainty; a contested count could push toward the 1% tail."
  - "The near-zero price implies markets expect a clean, called result even in a tight race, relying on Wisconsin's established certification process."
  - "Resolves via the official Wisconsin election authority responsible for certifying results; a recount request in a very tight margin is the key tail risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Francesca Hong and David Crowley are locked in a too-close-to-call Democratic gubernatorial primary in Wisconsin, with progressives and moderates in a tight race."
    publisher: "Garrett Downs"
    published_at: "2026-08-11T14:06:40.503Z"
    source_url: "https://www.cnbc.com/2026/08/11/minnesota-wisconsin-primaries-hong-flanagan-craig-run-in-key-races.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Garrett Downs"
        source_url: "https://www.cnbc.com/2026/08/11/minnesota-wisconsin-primaries-hong-flanagan-craig-run-in-key-races.html"
        retrieved_at: "2026-08-12T09:07:43+00:00"
  - type: "pm_response"
    notes: "Kalshi is the venue; the 1% price reflects strong prior that even close Wisconsin primaries resolve without prolonged certification disputes."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Garrett Downs: Democrats clash again in Minnesota and Wisconsin primaries as big midt"
    url: "https://www.cnbc.com/2026/08/11/minnesota-wisconsin-primaries-hong-flanagan-craig-run-in-key-races.html"
    published_at: "2026-08-11T14:06:40.503Z"
    retrieved_at: "2026-08-12T09:07:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
