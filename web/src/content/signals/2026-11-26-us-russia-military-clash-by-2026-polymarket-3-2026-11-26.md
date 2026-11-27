---
signal_id: "CMSIG2026112605"
signal_slug: "us-russia-military-clash-by-2026-polymarket-3-2026-11-26"
headline: "US-Russia military clash by 2026: Polymarket 3%"
semantic_title: "US-Russia military clash by 2026 remains a long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-26T00:00:00.000Z"
event_id: "CM-EVT-207L4994P4"
event_slug: "us-x-russia-military-clash-by"
event_question: "Will there be a military clash between the US and Russia by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3373d3750e99d0fd60da842e688d89b71ad92d6bdd42c329f199add1c5bacb06"
  question_raw: "US x Russia military clash by December 31, 2026?"
  current_price: 0.026
  volume_24h_usd: 34.61
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T12:00:00Z"
bullets:
  - "Polymarket prices a 3% chance of a direct US-Russia military clash before end of 2026, via UMA oracle."
  - "New START expiry removes a key guardrail in US-Russia relations, but the market treats armed conflict as a remote tail risk."
  - "Companion Polymarket contract CM-EVT-MSK2LZ3W00 on Ukraine limiting its armed forces sits at 3%, both contracts signal the market sees diplomacy, not escalation, as the base case."
  - "Resolution requires a confirmed direct military engagement between US and Russian forces before December 31, 2026, per UMA oracle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The last US-Russia nuclear arms control treaty, New START, is set to expire today with eleventh-hour talks reportedly weighing a short extension."
    publisher: "link.cfr.org"
    published_at: "2026-11-26T00:00:00.000Z"
    source_url: "https://link.cfr.org/public/43958089"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "link.cfr.org"
        source_url: "https://link.cfr.org/public/43958089"
        retrieved_at: "2026-11-27T07:47:43+00:00"
  - type: "pm_response"
    notes: "Polymarket holds the military-clash contract at 3%, dismissing treaty expiry as an imminent escalation trigger."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "link.cfr.org: Across the Globe"
    url: "https://link.cfr.org/public/43958089"
    published_at: "2026-11-26T00:00:00.000Z"
    retrieved_at: "2026-11-27T07:47:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
