---
signal_id: "CMSIG2026080507"
signal_slug: "co-05-house-seat-for-republicans-in-2026-polymarket-34-2026-08-05"
headline: "CO-05 House seat for Republicans in 2026: Polymarket 34%"
semantic_title: "CO-05 Republican hold odds slip below 50 percent"
telemetry: "Polymarket 34%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-05T00:00:00.000Z"
event_id: "CM-EVT-FMXJH0P4G0"
event_slug: "co-05-house-election-winner"
event_question: "Will the CO-05 House seat be won by a Republican in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbc533740775ffabd04d60009b45332c2a6f8cba43813bdf7b9577c5d0196a25d"
  question_raw: "Will the Democratic Party win the CO-05 House seat?"
  current_price: 0.34
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "The Polymarket contract puts only 34% on Republicans holding CO-05 in 2026, making it a lean-Democratic seat on the prediction market."
  - "Democrats formally adding CO-05 to their targeting list is consistent with the below-50% Republican pricing."
  - "Companion contracts show GOP holding IN-08 at 94% and OK-03 at 94%, illustrating CO-05 is an outlier among Republican-held seats."
  - "Resolves via UMA oracle based on official 2026 election results for Colorado's 5th congressional district."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "House Democrats expanded their targeting map to 12 new GOP-held districts including Colorado's 5th, held by Lauren Boebert."
    publisher: "new admin"
    published_at: "2026-08-05T00:00:00.000Z"
    source_url: "https://associattedpress.com/house-democrats-targeting-12-new-gop-held-districts-including-lauren-boebert-and-nrcc-chair-richard-hudsons-seats/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "new admin"
        source_url: "https://associattedpress.com/house-democrats-targeting-12-new-gop-held-districts-including-lauren-boebert-and-nrcc-chair-richard-hudsons-seats/"
        retrieved_at: "2026-08-08T08:35:11+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 34% for Republican win; among the lowest GOP-hold probabilities across targeted districts in the data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "new admin: House Democrats targeting 12 new GOP-held districts, including Lauren"
    url: "https://associattedpress.com/house-democrats-targeting-12-new-gop-held-districts-including-lauren-boebert-and-nrcc-chair-richard-hudsons-seats/"
    published_at: "2026-08-05T00:00:00.000Z"
    retrieved_at: "2026-08-08T08:35:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
