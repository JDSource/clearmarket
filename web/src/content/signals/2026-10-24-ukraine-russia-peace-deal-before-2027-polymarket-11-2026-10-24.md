---
signal_id: "CMSIG2026102406"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-11-2026-10-24"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 11%"
semantic_title: "Ukraine peace deal before 2027 stays a long shot at 11 percent"
telemetry: "Polymarket 11%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-24T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.11
  volume_24h_usd: 8573.460670999999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Ukraine signing a peace deal with Russia before 2027 sits at 11%, a firm long-shot read."
  - "US efforts to revive peace talks and a reported energy-for-diplomacy deal are positive signals, but the market is not moving significantly toward a deal scenario."
  - "The companion Polymarket contract on Russia and Ukraine reaching a ceasefire in 2026 at 14% (CM-EVT-2089XJ01Y3) corroborates the long-shot stance, with a ceasefire seen as only marginally more likely than a full peace deal."
  - "Resolution via Polymarket's uma_oracle; settlement requires a signed peace agreement, not merely resumed talks or partial ceasefires."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russian diesel tankers are headed for North America as part of a US-Russia deal, while the US attempts to revive peace talks between Ukraine and Russia."
    publisher: "Guardian staff"
    published_at: "2026-10-24T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/oct/24/ukraine-war-briefing-russian-diesel-tankers-headed-for-north-america-says-moscow-as-us-tries-to-revive-peace-talks"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Guardian staff"
        source_url: "https://www.theguardian.com/world/2026/oct/24/ukraine-war-briefing-russian-diesel-tankers-headed-for-north-america-says-moscow-as-us-tries-to-revive-peace-talks"
        retrieved_at: "2026-10-24T12:26:12+00:00"
  - type: "pm_response"
    notes: "Polymarket at 11% on a peace deal before 2027 is consistent with the 14% ceasefire-by-2026 contract, with both pricing suggesting the market treats ongoing diplomacy as insufficient evidence of imminent resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Guardian staff: Ukraine war briefing: Russian diesel tankers headed for North America,"
    url: "https://www.theguardian.com/world/2026/oct/24/ukraine-war-briefing-russian-diesel-tankers-headed-for-north-america-says-moscow-as-us-tries-to-revive-peace-talks"
    published_at: "2026-10-24T00:00:00.000Z"
    retrieved_at: "2026-10-24T12:26:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
