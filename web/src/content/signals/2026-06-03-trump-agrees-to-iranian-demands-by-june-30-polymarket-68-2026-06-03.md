---
signal_id: "CMSIG2026060306"
signal_slug: "trump-agrees-to-iranian-demands-by-june-30-polymarket-68-2026-06-03"
headline: "Trump agrees to Iranian demands by June 30: Polymarket 68%"
semantic_title: "Consensus tilts toward Trump unfreezing Iranian assets by June 30"
telemetry: "Polymarket 68%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-03T00:50:06.000Z"
event_id: "CM-EVT-1G2HVDCQG7"
event_slug: "what-iranian-demands-will-trump-agree-to-by-june-30"
event_question: "Will Trump agree to Iranian demands by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xed25d03a2589af03a7a603e7c07c36d53baf38c148e50cc1f5a6a6f285d68862"
  question_raw: "Will Trump agree to unfreeze Iranian assets by June 30?"
  current_price: 0.68
  volume_24h_usd: 5950.016447000012
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices 68% on Trump agreeing to Iranian demands by June 30, despite active military exchanges and stalled talks."
  - "Ongoing ballistic missile and drone attacks from Iran sit in tension with the 68% probability; the market is not treating the military escalation as a deal-breaker yet."
  - "Companion Polymarket contract CM-EVT-XYC4HDKBW3 prices 97% on the Iranian regime surviving US strikes, consistent with a negotiated rather than military resolution."
  - "Resolves via UMA oracle; resolution likely requires a publicly announced and verified agreement on Iranian nuclear or military demands before June 30."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US and Iran intensified attacks as the ceasefire frays and peace talks stall, with multiple Iranian ballistic missile and drone strikes repelled by US forces."
    publisher: "Anniek Bao"
    published_at: "2026-06-03T00:50:06.000Z"
    source_url: "https://www.cnbc.com/2026/06/03/us-iran-war-escalates-peace-talks-stalemate-.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Anniek Bao"
        source_url: "https://www.cnbc.com/2026/06/03/us-iran-war-escalates-peace-talks-stalemate-.html"
        retrieved_at: "2026-06-03T01:50:17+00:00"
  - type: "pm_response"
    notes: "Polymarket holds 68% on a near-term Iran deal even as ceasefire violations intensify, creating notable tension between the military news flow and the contract's optimistic pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Anniek Bao: U.S., Iran intensify attacks as ceasefire frays, peace talks stall"
    url: "https://www.cnbc.com/2026/06/03/us-iran-war-escalates-peace-talks-stalemate-.html"
    published_at: "2026-06-03T00:50:06.000Z"
    retrieved_at: "2026-06-03T01:50:17+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
