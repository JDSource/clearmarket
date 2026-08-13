---
signal_id: "CMSIG2026081208"
signal_slug: "zelenskyy-out-as-ukraine-president-by-2026-polymarket-8-2026-08-12"
headline: "Zelenskyy out as Ukraine president by 2026: Polymarket 8%"
semantic_title: "Zelenskyy out as Ukraine president by end of 2026 stays a long shot"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-12T00:00:00.000Z"
event_id: "CM-EVT-355Q75KD17"
event_slug: "zelenskyy-out-as-ukraine-president-before-2027"
event_question: "Will Zelenskyy be out as Ukraine president by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x51f624dbbf14f9edb575fef1be6f7a303751de70783fa144fce27b957452c803"
  question_raw: "Zelenskyy out as Ukraine president by end of 2026?"
  current_price: 0.08
  volume_24h_usd: 16069.8542
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 8% on Zelenskyy leaving the Ukrainian presidency by the end of 2026, a firm long-shot read."
  - "Zelenskyy's active diplomatic role, submitting peace proposals to Washington, is consistent with a market that does not see his departure as imminent."
  - "Ongoing Russian attacks and North Korean missile use raise conflict-escalation risks, but the market is not pricing political instability for Zelenskyy at this level."
  - "Resolves via UMA oracle; contract covers any departure mechanism including resignation, removal, or death, the resolution scope is broad."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukrainian President Volodymyr Zelenskyy said Kyiv has submitted peace proposals to the United States as Russia continued missile and drone attacks on Ukrainian cities."
    publisher: "Al Jazeera Staff"
    published_at: "2026-08-12T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/8/12/zelenskyy-says-ukraine-has-sent-proposals-to-us-to-end-war-with-russia"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/8/12/zelenskyy-says-ukraine-has-sent-proposals-to-us-to-end-war-with-russia"
        retrieved_at: "2026-08-13T09:07:47+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 8%; no companion contract with a nearer deadline carries a live price, limiting term-structure comparison."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Zelenskyy says Ukraine has sent proposals to US to end war with Russia"
    url: "https://www.aljazeera.com/news/2026/8/12/zelenskyy-says-ukraine-has-sent-proposals-to-us-to-end-war-with-russia"
    published_at: "2026-08-12T00:00:00.000Z"
    retrieved_at: "2026-08-13T09:07:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
