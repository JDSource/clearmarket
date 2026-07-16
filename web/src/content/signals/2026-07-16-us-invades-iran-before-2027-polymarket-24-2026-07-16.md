---
signal_id: "CMSIG2026071601"
signal_slug: "us-invades-iran-before-2027-polymarket-24-2026-07-16"
headline: "US invades Iran before 2027: Polymarket 24%"
semantic_title: "US invasion of Iran pricing holds below consensus fear"
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
  volume_24h_usd: 1416506.412836001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 24% on a full US invasion of Iran before 2027, despite active US strikes expanding into northern Iran."
  - "Iran declared the peace deal voided and launched retaliatory strikes on US bases across the region, yet prediction markets hold the invasion threshold well below 50%."
  - "The gap suggests markets distinguish ongoing air campaign and blockade from a ground invasion scenario, pricing escalation risk but not full-scale land war."
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 sits at 57%, implying markets see a path to de-escalation even as strikes broaden."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran targeted US military bases in Kuwait, Bahrain, and Jordan with retaliatory strikes after the US expanded airstrikes into northern Iran, with Tehran declaring an existential war."
    publisher: "bbc.co.uk"
    published_at: "2026-07-16T07:06:38.000Z"
    source_url: "https://www.bbc.co.uk/news/articles/c2lq1ed28jxo?at_medium=RSS&at_campaign=rss"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.co.uk"
        source_url: "https://www.bbc.co.uk/news/articles/c2lq1ed28jxo?at_medium=RSS&at_campaign=rss"
        retrieved_at: "2026-07-16T10:04:17+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 24% invasion price and 57% Hormuz normalization are directionally consistent, implying markets embed a contained-strikes scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.co.uk: Iran targets military bases as US launches wave of strikes - BBC News"
    url: "https://www.bbc.co.uk/news/articles/c2lq1ed28jxo?at_medium=RSS&at_campaign=rss"
    published_at: "2026-07-16T07:06:38.000Z"
    retrieved_at: "2026-07-16T10:04:17+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
