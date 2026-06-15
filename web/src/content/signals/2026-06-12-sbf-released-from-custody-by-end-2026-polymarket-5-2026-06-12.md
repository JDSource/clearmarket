---
signal_id: "CMSIG2026061208"
signal_slug: "sbf-released-from-custody-by-end-2026-polymarket-5-2026-06-12"
headline: "SBF released from custody by end 2026: Polymarket 5%"
semantic_title: "SBF release from custody by year-end wavers near floor pricing"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-12T14:13:40.000Z"
event_id: "CM-EVT-TYKMHKW302"
event_slug: "sbf-released-from-custody-in-2026"
event_question: "Will Sam Bankman-Fried be released from custody by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5f18a2399d214215045b9e9e9ae2b565c00dd6313a2b853999aaad2dc9fbf85e"
  question_raw: "SBF released from custody in 2026?"
  current_price: 0.047
  volume_24h_usd: 3384.449031
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices SBF's release from custody by end of 2026 at 5%, near the floor even before the appeals loss."
  - "The failed appeal removes the primary legal pathway to release, making the 5% consistent with only residual pardon or extraordinary relief scenarios."
  - "The companion Trump pardon by July 31 contract on Polymarket sits at 3%, suggesting markets see presidential intervention as the main remaining release mechanism."
  - "Resolution is via UMA oracle; release by any mechanism, including pardon, commutation, or bond, would likely resolve the contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Sam Bankman-Fried lost his appeal of criminal fraud and conspiracy convictions at the appellate court."
    publisher: "coindesk.com"
    published_at: "2026-06-12T14:13:40.000Z"
    source_url: "https://www.coindesk.com/policy/2026/06/12/ftx-s-sam-bankman-fried-loses-appeal-of-criminal-conviction-on-fraud-conspiracy-charges"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/policy/2026/06/12/ftx-s-sam-bankman-fried-loses-appeal-of-criminal-conviction-on-fraud-conspiracy-charges"
        retrieved_at: "2026-06-15T13:51:44+00:00"
  - type: "pm_response"
    notes: "Polymarket at 5% was already pricing near-zero before the appeal loss; the ruling closes the legal route and leaves only executive clemency as a residual path."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: FTX's Sam Bankman-Fried loses appeal of criminal conviction on fraud,"
    url: "https://www.coindesk.com/policy/2026/06/12/ftx-s-sam-bankman-fried-loses-appeal-of-criminal-conviction-on-fraud-conspiracy-charges"
    published_at: "2026-06-12T14:13:40.000Z"
    retrieved_at: "2026-06-15T13:51:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
