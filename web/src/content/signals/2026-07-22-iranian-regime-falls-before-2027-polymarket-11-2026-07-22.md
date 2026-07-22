---
signal_id: "CMSIG2026072203"
signal_slug: "iranian-regime-falls-before-2027-polymarket-11-2026-07-22"
headline: "Iranian regime falls before 2027: Polymarket 11%"
semantic_title: "Iranian regime survival stays heavily priced in despite US strikes"
telemetry: "Polymarket 11%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-22T00:00:00.000Z"
event_id: "CM-EVT-QNQ4VPVP80"
event_slug: "will-the-iranian-regime-fall-by-the-end-of-2026"
event_question: "Will the Iranian regime fall before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbb4d51e6364066d92eb6f9b8413dd7193de70966736044463b205834805a1f3b"
  question_raw: "Will the Iranian regime fall before 2027?"
  current_price: 0.11
  volume_24h_usd: 190639.32795500007
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 11% on the Iranian regime falling before 2027."
  - "Eleven consecutive nights of strikes have not moved regime-collapse odds into meaningful territory, with markets treating the current government as durable."
  - "The 22% Polymarket contract on Iran ending uranium enrichment by December 31 similarly reflects low confidence in a decisive outcome."
  - "Resolves via UMA oracle; regime survival definition and verification mechanism are the key settlement questions."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US launched its 11th consecutive night of strikes on Iran, hitting the Bidboland refinery and Bushehr military airport, with air defenses activated near Tehran."
    publisher: "aa.com.tr"
    published_at: "2026-07-22T00:00:00.000Z"
    source_url: "https://www.aa.com.tr/en/us-israel-iran-war/us-strikes-intensify-across-iran-as-air-defenses-activated-near-tehran/4005284"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aa.com.tr"
        source_url: "https://www.aa.com.tr/en/us-israel-iran-war/us-strikes-intensify-across-iran-as-air-defenses-activated-near-tehran/4005284"
        retrieved_at: "2026-07-22T10:22:09+00:00"
  - type: "pm_response"
    notes: "Polymarket's 11% regime-fall contract suggests the market is sharply discounting the operational impact of the current US air campaign on Iranian political stability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aa.com.tr: US strikes intensify across Iran as air defenses activated near Tehran"
    url: "https://www.aa.com.tr/en/us-israel-iran-war/us-strikes-intensify-across-iran-as-air-defenses-activated-near-tehran/4005284"
    published_at: "2026-07-22T00:00:00.000Z"
    retrieved_at: "2026-07-22T10:22:09+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
