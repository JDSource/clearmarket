---
signal_id: "CMSIG2026071602"
signal_slug: "us-invades-iran-before-2027-polymarket-24-2026-07-16"
headline: "US invades Iran before 2027: Polymarket 24%"
semantic_title: "US invasion of Iran pricing holds well below median odds"
telemetry: "Polymarket 24%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-16T07:06:38.000Z"
event_id: "CM-EVT-WD982793G1"
event_slug: "will-the-us-invade-iran-before-2027"
event_question: "Will the U.S. invade Iran before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5db999fad322cea2914535aae5517060c3f80ad6d8c0231cde2124a434d16846"
  question_raw: "Will the U.S. invade Iran before 2027?"
  current_price: 0.24
  volume_24h_usd: 1565090.8409010004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 24% chance the US invades Iran before 2027, despite active and escalating bilateral strikes."
  - "News of US forces hitting deeper northern Iranian targets sits at odds with a market pricing invasion at only roughly one-in-four odds."
  - "Kalshi separately prices just 5% on the US reopening its embassy in Iran, consistent with no near-term diplomatic resolution."
  - "The gap between strike escalation and invasion pricing likely reflects markets distinguishing targeted air campaigns from a ground invasion."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran targeted US military bases in Kuwait, Bahrain, and Jordan as the US expanded strikes into northern Iran and enforced a naval blockade."
    publisher: "bbc.co.uk"
    published_at: "2026-07-16T07:06:38.000Z"
    source_url: "https://www.bbc.co.uk/news/articles/c2lq1ed28jxo?at_medium=RSS&at_campaign=rss"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.co.uk"
        source_url: "https://www.bbc.co.uk/news/articles/c2lq1ed28jxo?at_medium=RSS&at_campaign=rss"
        retrieved_at: "2026-07-16T17:20:43+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; definition of 'invade' versus sustained air campaign is the key resolution edge case."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.co.uk: Iran targets military bases as US launches wave of strikes - BBC News"
    url: "https://www.bbc.co.uk/news/articles/c2lq1ed28jxo?at_medium=RSS&at_campaign=rss"
    published_at: "2026-07-16T07:06:38.000Z"
    retrieved_at: "2026-07-16T17:20:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
