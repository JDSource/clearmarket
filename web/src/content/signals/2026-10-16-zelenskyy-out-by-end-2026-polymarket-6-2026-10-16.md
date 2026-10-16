---
signal_id: "CMSIG2026101608"
signal_slug: "zelenskyy-out-by-end-2026-polymarket-6-2026-10-16"
headline: "Zelenskyy out by end-2026: Polymarket 6%"
semantic_title: "Zelenskyy out as Ukraine president by year-end stays a long shot"
telemetry: "Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-16T00:00:00.000Z"
event_id: "CM-EVT-355Q75KD17"
event_slug: "zelenskyy-out-as-ukraine-president-before-2027"
event_question: "Will Zelenskyy be out as Ukraine president by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x51f624dbbf14f9edb575fef1be6f7a303751de70783fa144fce27b957452c803"
  question_raw: "Zelenskyy out as Ukraine president by end of 2026?"
  current_price: 0.06
  volume_24h_usd: 2192.221126
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 6% on Zelenskyy leaving the Ukrainian presidency by the end of 2026."
  - "Despite Guardian reporting of a worsening U.S.-Ukraine relationship and diplomatic uncertainty, the market is not pricing leadership instability in Kyiv."
  - "Zelenskyy's active engagement with EU leaders on security guarantees, reported within the same 24-hour window, is consistent with a market that sees him as firmly in power for the remainder of the year."
  - "Resolves via UMA oracle; the peace deal suite (CM-EVT-DCQYWYX424 at 6%) and this contract at 6% are co-consistent: markets price Zelenskyy staying put and no deal getting done."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukrainian President Volodymyr Zelenskyy held talks with EU leaders about post-war security guarantees amid a reported breakdown in the U.S.-Ukraine relationship."
    publisher: "Jakub Krupa"
    published_at: "2026-10-16T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/live/2026/oct/16/eu-von-der-leyen-russia-sanctions-diesel-fuel-zelenskyy-donald-trump-membership-migration-latest-news-updates"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jakub Krupa"
        source_url: "https://www.theguardian.com/world/live/2026/oct/16/eu-von-der-leyen-russia-sanctions-diesel-fuel-zelenskyy-donald-trump-membership-migration-latest-news-updates"
        retrieved_at: "2026-10-16T12:59:00+00:00"
  - type: "pm_response"
    notes: "Polymarket contract via UMA oracle; at 6%, well below any threshold of political instability concern."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jakub Krupa: Zelenskyy holds press conference after talks with EU leaders over brea"
    url: "https://www.theguardian.com/world/live/2026/oct/16/eu-von-der-leyen-russia-sanctions-diesel-fuel-zelenskyy-donald-trump-membership-migration-latest-news-updates"
    published_at: "2026-10-16T00:00:00.000Z"
    retrieved_at: "2026-10-16T12:59:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
