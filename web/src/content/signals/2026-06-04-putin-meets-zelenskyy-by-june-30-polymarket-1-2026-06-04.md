---
signal_id: "CMSIG2026060407"
signal_slug: "putin-meets-zelenskyy-by-june-30-polymarket-1-2026-06-04"
headline: "Putin meets Zelenskyy by June 30: Polymarket 1%"
semantic_title: "Putin-Zelenskyy direct meeting by June 30 priced near zero"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-06-04T00:00:00.000Z"
event_id: "CM-EVT-2DR1P4YZ13"
event_slug: "will-putin-meet-with-zelenskyy-by-june-30-2026"
event_question: "Will Putin meet with Zelenskyy by June 30, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc5ab3fb332af0bebf7ed6df1b1d5e1cc32a91e960c57d7602a5224830cf0084b"
  question_raw: "Will Putin meet with Zelenskyy by June 30, 2026?"
  current_price: 0.011
  volume_24h_usd: 535.846363
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices just 1% probability that Putin meets Zelenskyy before June 30."
  - "Putin's public rejection of Zelenskyy's open letter is consistent with the near-zero pricing on an imminent summit."
  - "The December 2026 ceasefire agreement contract at 49% shows the market treats eventual negotiation as roughly a coin flip, but not near-term."
  - "Resolves via UMA oracle; requires confirmed in-person meeting between the two leaders before the deadline."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukrainian President Volodymyr Zelenskyy wrote an open letter proposing direct face-to-face talks with Russian President Vladimir Putin, who subsequently rejected the offer."
    publisher: "bbc.co.uk"
    published_at: "2026-06-04T00:00:00.000Z"
    source_url: "https://www.bbc.co.uk/news/articles/cwy2ypyp4x4o"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.co.uk"
        source_url: "https://www.bbc.co.uk/news/articles/cwy2ypyp4x4o"
        retrieved_at: "2026-06-07T10:26:16+00:00"
  - type: "pm_response"
    notes: "Polymarket's 1% on a June meeting versus 49% on a year-end ceasefire captures the market's view that diplomacy, if it comes, is months away."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.co.uk: Zelensky proposes face-to-face talks in open letter to Putin - BBC New"
    url: "https://www.bbc.co.uk/news/articles/cwy2ypyp4x4o"
    published_at: "2026-06-04T00:00:00.000Z"
    retrieved_at: "2026-06-07T10:26:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
