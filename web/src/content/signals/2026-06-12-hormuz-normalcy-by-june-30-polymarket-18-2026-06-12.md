---
signal_id: "CMSIG2026061202"
signal_slug: "hormuz-normalcy-by-june-30-polymarket-18-2026-06-12"
headline: "Hormuz normalcy by June 30: Polymarket 18%"
semantic_title: "Hormuz normal traffic by end of June anchors below 20 percent"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-12T05:28:35.000Z"
event_id: "CM-EVT-YPW93GCTK6"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-end-of-june"
event_question: "Strait of Hormuz traffic normal by June 30"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x348cd9adf4f6855f58bd9c6dbf9ff251c4142ef77233a5dc95c65b4b61cd2187"
  question_raw: "Strait of Hormuz traffic returns to normal by end of June?"
  current_price: 0.18
  volume_24h_usd: 2192769.440225002
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices Hormuz traffic returning to normal by end of June at just 18%, despite deal optimism."
  - "Trump's weekend signing signal and Hormuz reopening rhetoric are not consistent with the market's skeptical near-term read."
  - "The December 31 Polymarket contract on the same question sits at 78%, showing markets price eventual normalization but not on Trump's timeline."
  - "A separate ladder contract implies roughly 20-25 transit calls through Hormuz, well below historical norms, reinforcing the timeline doubt."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump signaled Iran war deal could close imminently, raising hopes for Strait of Hormuz reopening, but tensions lingered."
    publisher: "al-monitor.com"
    published_at: "2026-06-12T05:28:35.000Z"
    source_url: "https://www.al-monitor.com/originals/2026/06/trump-says-iran-war-deal-close-strait-hormuz-tensions-linger"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "al-monitor.com"
        source_url: "https://www.al-monitor.com/originals/2026/06/trump-says-iran-war-deal-close-strait-hormuz-tensions-linger"
        retrieved_at: "2026-06-14T10:47:32+00:00"
  - type: "pm_response"
    notes: "Both contracts resolve via portwatch.imf.org traffic data; the wide June-to-December spread is the key term-structure signal here."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "al-monitor.com: Trump says Iran war deal close as Strait of Hormuz tensions linger - A"
    url: "https://www.al-monitor.com/originals/2026/06/trump-says-iran-war-deal-close-strait-hormuz-tensions-linger"
    published_at: "2026-06-12T05:28:35.000Z"
    retrieved_at: "2026-06-14T10:47:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
