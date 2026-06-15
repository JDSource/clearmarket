---
signal_id: "CMSIG2026061504"
signal_slug: "hormuz-transit-calls-implied-20-25-kalshi-ladder-2026-06-15"
headline: "Hormuz transit calls implied 20-25: Kalshi ladder"
semantic_title: "Hormuz transit calls consensus anchors in the 20 to 25 range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-15T09:16:44.000Z"
event_id: "CM-EVT-YGPLR2RJZ6"
event_slug: "kxhormuzweekly-26jun14"
event_question: "Strait of Hormuz transit calls (count)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHORMUZWEEKLY-26JUN14-T25"
  question_raw: "Will there be more than 25 transit calls through the Strait of Hormuz from Jun 8, 2026 to Jun 14, 2026?"
  current_price: 0.48
  volume_24h_usd: 2024.23
  arbitration_model: "kalshi_staff"
  resolution_source: "IMF PortWatch"
  resolves_at: "2026-06-16T14:00:00Z"
bullets:
  - "Kalshi ladder prices Hormuz transit calls with 77% above 20 but only 48% above 25, implying a market consensus range of 20 to 25 calls."
  - "The Iran deal and announced June 19 reopening support a recovery in transits, but the ladder's sharp drop above 25 signals limited confidence in a full pre-war traffic restoration."
  - "The year-end Hormuz normalization Polymarket contract at 78% is broadly consistent with this range, both pricing partial rather than full recovery."
  - "Resolution depends on measured transit data through the Strait; the contract source and counting methodology determine whether partial reopening counts."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Congress is reviewing the new Iran deal as Trump departed for the G7, with Hormuz reopening tied to deal ratification."
    publisher: "punchbowl.news"
    published_at: "2026-06-15T09:16:44.000Z"
    source_url: "https://punchbowl.news/article/defense/new-iran-deal/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "punchbowl.news"
        source_url: "https://punchbowl.news/article/defense/new-iran-deal/"
        retrieved_at: "2026-06-15T13:51:44+00:00"
  - type: "pm_response"
    notes: "Kalshi's distribution anchors expected Hormuz transits in the 20-25 range, pricing a meaningful but incomplete recovery consistent with cautious diplomatic optimism."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "punchbowl.news: Congress and the new Iran deal"
    url: "https://punchbowl.news/article/defense/new-iran-deal/"
    published_at: "2026-06-15T09:16:44.000Z"
    retrieved_at: "2026-06-15T13:51:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
