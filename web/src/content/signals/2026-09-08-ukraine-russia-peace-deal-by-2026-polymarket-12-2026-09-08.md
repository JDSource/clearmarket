---
signal_id: "CMSIG2026090806"
signal_slug: "ukraine-russia-peace-deal-by-2026-polymarket-12-2026-09-08"
headline: "Ukraine-Russia peace deal by 2026: Polymarket 12%"
semantic_title: "Ukraine peace deal before 2027 remains a long shot"
telemetry: "Polymarket 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-08T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.12
  volume_24h_usd: 5847.683777
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Ukraine signing a peace deal with Russia before 2027 sits at 12%."
  - "US envoys flagged diplomatic movement, yet markets price only a 12% chance of a formal deal, showing strong skepticism toward the diplomatic signals."
  - "Russia's missile strike on Kyiv immediately after envoys left is consistent with the market's low probability on a near-term agreement."
  - "A separate Polymarket contract on a Russia-Ukraine peace agreement by 2026 (CM-EVT-66S3LD3901) prices at 8%, suggesting the market sees even a loose accord as unlikely this calendar year."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US envoy Steve Witkoff reported movement toward three-way talks between the US, Russia, and Ukraine, but Russia struck Kyiv with missiles shortly after envoys departed."
    publisher: "channelnewsasia.com"
    published_at: "2026-09-08T00:00:00.000Z"
    source_url: "https://www.channelnewsasia.com/world/us-envoy-sees-movement-toward-three-way-talks-russia-ukraine-6368071"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "channelnewsasia.com"
        source_url: "https://www.channelnewsasia.com/world/us-envoy-sees-movement-toward-three-way-talks-russia-ukraine-6368071"
        retrieved_at: "2026-09-08T12:33:52+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the gap between envoy optimism and the 12% contract price is the key market-versus-news divergence here."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "channelnewsasia.com: US envoy sees 'movement' toward three-way talks with Russia, Ukraine -"
    url: "https://www.channelnewsasia.com/world/us-envoy-sees-movement-toward-three-way-talks-russia-ukraine-6368071"
    published_at: "2026-09-08T00:00:00.000Z"
    retrieved_at: "2026-09-08T12:33:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
