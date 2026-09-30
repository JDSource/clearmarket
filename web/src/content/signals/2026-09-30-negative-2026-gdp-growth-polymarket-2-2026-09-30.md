---
signal_id: "CMSIG2026093002"
signal_slug: "negative-2026-gdp-growth-polymarket-2-2026-09-30"
headline: "Negative 2026 GDP growth: Polymarket 2%"
semantic_title: "Negative US GDP growth in 2026 stays a long shot at 2 percent"
telemetry: "Polymarket 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-30T00:00:00.000Z"
event_id: "CM-EVT-36YHF72CQ8"
event_slug: "negative-gdp-growth-in-2026"
event_question: "Will there be negative GDP growth in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd8c1b0a73653b1fb4fb6e8d13d0063d25810870d7ddf83e61fffb4de4522edf1"
  question_raw: "Negative GDP growth in 2026?"
  current_price: 0.02
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-29T00:00:00Z"
bullets:
  - "Polymarket puts only 2% odds on negative U.S. GDP growth in 2026, a near-certainty of continued positive annual growth."
  - "The 2.2% Q2 upward revision is fully consistent with this pricing; the market shows no disagreement with the official data."
  - "With Q2 revised higher and August PCE inflation coming in softer than expected, the stagflation risk narrative finds little support in current prices."
  - "Resolves via UMA oracle; a full-year negative print would require a severe second-half contraction from a 2.2% Q2 baseline, which the market sees as remote."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The BEA revised U.S. Q2 2026 GDP growth up to 2.2%, beating the prior estimate and signaling continued economic resilience."
    publisher: "Paul Wiseman, Associated Press"
    published_at: "2026-09-30T00:00:00.000Z"
    source_url: "https://www.pbs.org/newshour/economy/u-s-economy-grew-a-solid-2-2-in-the-second-quarter-government-says-upgrading-previous-estimate"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Paul Wiseman, Associated Press"
        source_url: "https://www.pbs.org/newshour/economy/u-s-economy-grew-a-solid-2-2-in-the-second-quarter-government-says-upgrading-previous-estimate"
        retrieved_at: "2026-09-30T14:32:59+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on full-year 2026 real GDP; the 2% price leaves little ambiguity about market consensus."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Paul Wiseman, Associated Press: U.S. economy grew a solid 2.2% in the second quarter, government says,"
    url: "https://www.pbs.org/newshour/economy/u-s-economy-grew-a-solid-2-2-in-the-second-quarter-government-says-upgrading-previous-estimate"
    published_at: "2026-09-30T00:00:00.000Z"
    retrieved_at: "2026-09-30T14:32:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
