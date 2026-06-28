---
signal_id: "CMSIG2026062702"
signal_slug: "hormuz-normal-traffic-by-june-30-polymarket-2-2026-06-27"
headline: "Hormuz normal traffic by June 30: Polymarket 2%"
semantic_title: "Hormuz normal traffic by June 30 priced as near-impossible"
telemetry: "Polymarket 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-27T22:10:11.000Z"
event_id: "CM-EVT-YPW93GCTK6"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-end-of-june"
event_question: "Will traffic through the Strait of Hormuz return to normal by the end of June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x348cd9adf4f6855f58bd9c6dbf9ff251c4142ef77233a5dc95c65b4b61cd2187"
  question_raw: "Strait of Hormuz traffic returns to normal by end of June?"
  current_price: 0.015
  volume_24h_usd: 726088.84834
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices normal Hormuz traffic by end of June at just 2%, near-zero odds of rapid normalization."
  - "Mutual US-Iran strikes this week make imminent resumption of normal shipping implausible; the market is fully aligned with the news."
  - "The Polymarket contract on a US invasion of Iran before 2027 at 15% suggests markets see continued skirmishes, not full war, as the base case."
  - "Resolves via portwatch.imf.org shipping data; resolution requires measurable return to baseline transit volumes by June 30."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Escalating US-Iran strikes and counter-attacks in the Strait of Hormuz are threatening an already fragile ceasefire and disrupting commercial shipping."
    publisher: "straitstimes.com"
    published_at: "2026-06-27T22:10:11.000Z"
    source_url: "https://www.straitstimes.com/world/middle-east/us-conducts-further-strikes-on-iran"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "straitstimes.com"
        source_url: "https://www.straitstimes.com/world/middle-east/us-conducts-further-strikes-on-iran"
        retrieved_at: "2026-06-28T10:24:59+00:00"
  - type: "pm_response"
    notes: "Polymarket at 2% on June 30 normalization is consistent with ongoing mutual strikes reported through June 28."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "straitstimes.com: US strikes Iran after tanker attack | The Straits Times"
    url: "https://www.straitstimes.com/world/middle-east/us-conducts-further-strikes-on-iran"
    published_at: "2026-06-27T22:10:11.000Z"
    retrieved_at: "2026-06-28T10:24:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
