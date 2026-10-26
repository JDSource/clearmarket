---
signal_id: "CMSIG2026102507"
signal_slug: "us-russia-military-clash-by-2026-polymarket-4-2026-10-25"
headline: "US-Russia military clash by 2026: Polymarket 4%"
semantic_title: "US-Russia military clash by 2026 stays near long-shot pricing"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-25T00:00:00.000Z"
event_id: "CM-EVT-207L4994P4"
event_slug: "us-x-russia-military-clash-by"
event_question: "Will there be a military clash between the US and Russia by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3373d3750e99d0fd60da842e688d89b71ad92d6bdd42c329f199add1c5bacb06"
  question_raw: "US x Russia military clash by December 31, 2026?"
  current_price: 0.035
  volume_24h_usd: 41.981577
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T12:00:00Z"
bullets:
  - "Polymarket puts 4% on a military clash between the U.S. and Russia occurring before end of 2026."
  - "The New START expiration is a flashpoint headline, but the market is treating an actual military confrontation as a remote tail risk, not a directional shift."
  - "A companion Polymarket contract (CM-EVT-MSK2LZ3W00) prices only 3% on Ukraine limiting its armed forces before 2027, suggesting the market sees the treaty moment as low-escalation."
  - "Resolves via UMA oracle; a verified direct military engagement between U.S. and Russian forces would settle the contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The last nuclear arms control deal between the United States and Russia is set to expire today, with eleventh-hour talks reportedly exploring an extension."
    publisher: "link.cfr.org"
    published_at: "2026-10-25T00:00:00.000Z"
    source_url: "https://link.cfr.org/public/43958089"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "link.cfr.org"
        source_url: "https://link.cfr.org/public/43958089"
        retrieved_at: "2026-10-26T07:47:50+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 4%; no volume signal provided, so no day-over-day activity to report."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "link.cfr.org: Across the Globe"
    url: "https://link.cfr.org/public/43958089"
    published_at: "2026-10-25T00:00:00.000Z"
    retrieved_at: "2026-10-26T07:47:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
