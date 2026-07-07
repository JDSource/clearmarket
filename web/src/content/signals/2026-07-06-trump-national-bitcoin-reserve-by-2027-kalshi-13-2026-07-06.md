---
signal_id: "CMSIG2026070606"
signal_slug: "trump-national-bitcoin-reserve-by-2027-kalshi-13-2026-07-06"
headline: "Trump National Bitcoin Reserve by 2027: Kalshi 13%"
semantic_title: "National Bitcoin Reserve by 2027 consensus wavers near low odds"
telemetry: "Kalshi 13%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-06T18:37:55.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve before 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.13
  volume_24h_usd: 113.59
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prediction market prices only a 13% probability that Trump creates a National Bitcoin Reserve before 2027."
  - "The Treasury-Commerce turf war reported today is consistent with Kalshi's low odds, showing implementation barriers the executive order alone could not resolve."
  - "A companion Polymarket contract on the Clarity Act being signed into law in 2026 sits at 46%, suggesting broader crypto legislation may advance even as the reserve stalls."
  - "Kalshi resolves via New York Times reporting; formal establishment of the reserve, not just an executive order reaffirmation, is the settlement standard."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump's Bitcoin reserve plan has stalled more than a year after Executive Order 14233 was signed, with interagency turf wars between Treasury and Commerce blocking implementation."
    publisher: "Editorial Team"
    published_at: "2026-07-06T18:37:55.000Z"
    source_url: "https://cryptobriefing.com/trump-bitcoin-reserve-faces-hurdles/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Editorial Team"
        source_url: "https://cryptobriefing.com/trump-bitcoin-reserve-faces-hurdles/"
        retrieved_at: "2026-07-07T10:52:00+00:00"
  - type: "pm_response"
    notes: "Kalshi resolves via New York Times confirmation; at 13% the market treats the interagency dispute as a material obstacle, not a procedural delay."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Editorial Team: Trump's Bitcoin reserve plan stalls amid Treasury-Commerce turf war: R"
    url: "https://cryptobriefing.com/trump-bitcoin-reserve-faces-hurdles/"
    published_at: "2026-07-06T18:37:55.000Z"
    retrieved_at: "2026-07-07T10:52:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
