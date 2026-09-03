---
signal_id: "CMSIG2026090205"
signal_slug: "gop-house-control-2026-polymarket-90-2026-09-02"
headline: "GOP House control 2026: Polymarket 90%"
semantic_title: "Republicans heavily favored to win House control in 2026"
telemetry: "Polymarket 90%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-09-02T00:00:00.000Z"
event_id: "CM-EVT-2N6T7M0T15"
event_slug: "which-party-will-win-the-house-in-2026"
event_question: "Will the Republican Party win control of the House of Representatives in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd5d9fc47718bd553592d126b1fa5e87183d27f3936975b0c04cc0f2dec1f1bb4"
  question_raw: "Will the Democratic Party control the House after the 2026 Midterm elections?"
  current_price: 0.9
  volume_24h_usd: 24682.040352
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "The Polymarket contract on Republicans winning House control in 2026 is priced at 90%, a strongly favored outcome."
  - "Democrats blocking the Supreme Court cap amendment is a routine partisan vote consistent with the current Republican majority environment the 90% price implies."
  - "Trump vowing to campaign in 35 midterm races (Story 12) and the government funding bill passing bipartisanly (Story 13) add further midterm context without shifting this contract's direction."
  - "Resolution is tied to the official 2026 midterm election results and House seat counts, via an unspecified resolution source."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Democrats in the House defeated a Republican constitutional amendment to cap the Supreme Court at nine justices, with Democrats voting against the measure."
    publisher: "devdiscourse.com"
    published_at: "2026-09-02T00:00:00.000Z"
    source_url: "https://www.devdiscourse.com/article/international/3971707-democrats-sink-republican-bid-to-cap-supreme-court-at-nine-justices"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "devdiscourse.com"
        source_url: "https://www.devdiscourse.com/article/international/3971707-democrats-sink-republican-bid-to-cap-supreme-court-at-nine-justices"
        retrieved_at: "2026-09-03T12:30:58+00:00"
  - type: "pm_response"
    notes: "Polymarket at 90% is the only hard price among the midterm House control candidates; companion Senate and combined-chamber contracts carry no disclosed prices."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "devdiscourse.com: Democrats sink Republican bid to cap Supreme Court at nine justices |"
    url: "https://www.devdiscourse.com/article/international/3971707-democrats-sink-republican-bid-to-cap-supreme-court-at-nine-justices"
    published_at: "2026-09-02T00:00:00.000Z"
    retrieved_at: "2026-09-03T12:30:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
