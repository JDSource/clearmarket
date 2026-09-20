---
signal_id: "CMSIG2026092006"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-16-2026-09-20"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 16%"
semantic_title: "Hormuz traffic returning to normal by year-end priced well below 25 percent"
telemetry: "Polymarket 16%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-20T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.16
  volume_24h_usd: 28995.661866
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only a 16% chance Strait of Hormuz traffic returns to normal by December 31."
  - "Iran's seven-condition ultimatum and 'decisive war' rhetoric are consistent with a market assigning long-shot odds to a near-term resolution."
  - "A companion Kalshi contract on the US reopening its embassy in Iran sits at 3%, signaling markets see diplomatic normalization as even more distant."
  - "Resolves via Polymarket's UMA oracle; the definition of 'normal' traffic is the key settlement edge case given partial disruptions may not trigger resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran set seven conditions for restarting talks with the United States as oil prices crossed $100 per barrel amid growing regional escalation."
    publisher: "Urooba Jamal"
    published_at: "2026-09-20T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/9/20/what-are-irans-new-conditions-to-end-its-war-with-the-us"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Urooba Jamal"
        source_url: "https://www.aljazeera.com/news/2026/9/20/what-are-irans-new-conditions-to-end-its-war-with-the-us"
        retrieved_at: "2026-09-20T12:50:04+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 16% reflects a market that is far more skeptical of a Hormuz resolution by year-end than the current diplomatic activity might suggest."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Urooba Jamal: What are Iran’s latest conditions to end its war with the US? | US-Isr"
    url: "https://www.aljazeera.com/news/2026/9/20/what-are-irans-new-conditions-to-end-its-war-with-the-us"
    published_at: "2026-09-20T00:00:00.000Z"
    retrieved_at: "2026-09-20T12:50:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
