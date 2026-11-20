---
signal_id: "CMSIG2026111908"
signal_slug: "al-sharaa-no-longer-leads-syria-by-dec-31-polymarket-2-2026-11-19"
headline: "Al-Sharaa no longer leads Syria by Dec 31: Polymarket 2%"
semantic_title: "Ahmed al-Sharaa losing Syria leadership by year-end stays a long shot"
telemetry: "Polymarket 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-19T00:00:00.000Z"
event_id: "CM-EVT-F551BM8LB9"
event_slug: "ahmed-al-sharaa-out-as-leader-of-syria-before-2027"
event_question: "Will Ahmed al-Sharaa no longer be the leader of Syria by December 31, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x568d872051e7b699d8e056b76d470d3f8a0e423c7a79c7aace4dffb60bebfb27"
  question_raw: "Ahmed al-Sharaa out as leader of Syria by December 31, 2026?"
  current_price: 0.016
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 2% on Ahmed al-Sharaa no longer leading Syria by December 31, 2026."
  - "US sanctions relief and a Trump meeting with al-Sharaa signal Western diplomatic recognition, reducing the near-term threat to his leadership position."
  - "The companion Polymarket contract (CM-EVT-4KV364R788) prices 2% on Israel-Saudi normalization before 2027, suggesting the broader regional realignment is also heavily discounted."
  - "Resolves via UMA oracle; requires al-Sharaa to leave the leadership role by year-end, whether by removal, resignation, or death."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump met with Syrian interim President Ahmed al-Sharaa and announced sanctions relief, marking a major US policy shift toward normalizing relations with Syria."
    publisher: "link.cfr.org"
    published_at: "2026-11-19T00:00:00.000Z"
    source_url: "https://link.cfr.org/public/39859936"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "link.cfr.org"
        source_url: "https://link.cfr.org/public/39859936"
        retrieved_at: "2026-11-20T07:47:31+00:00"
  - type: "pm_response"
    notes: "Polymarket at 2% on al-Sharaa's removal; US engagement is directionally consistent with the market's view that his position is stable through year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "link.cfr.org: Across the Globe"
    url: "https://link.cfr.org/public/39859936"
    published_at: "2026-11-19T00:00:00.000Z"
    retrieved_at: "2026-11-20T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
