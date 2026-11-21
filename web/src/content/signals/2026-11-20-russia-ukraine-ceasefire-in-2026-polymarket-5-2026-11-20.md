---
signal_id: "CMSIG2026112004"
signal_slug: "russia-ukraine-ceasefire-in-2026-polymarket-5-2026-11-20"
headline: "Russia-Ukraine ceasefire in 2026: Polymarket 5%"
semantic_title: "Russia-Ukraine ceasefire in 2026 stays near long-shot odds at 5 percent"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-20T00:00:00.000Z"
event_id: "CM-EVT-2089XJ01Y3"
event_slug: "russia-x-ukraine-ceasefire-by"
event_question: "Will Russia and Ukraine reach a ceasefire in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84c625fdccf5c5246a15e476361e4563033906ee225800e1136c0d737596a72f"
  question_raw: "Russia x Ukraine ceasefire by December 31, 2026?"
  current_price: 0.051
  volume_24h_usd: 4489.765714
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only a 5% probability on a Russia-Ukraine ceasefire occurring in 2026, resolves via UMA oracle."
  - "Despite the joint Trump-Putin-Xi peace declaration and U.S. military repositioning as leverage, the market is not pricing a near-term ceasefire as likely."
  - "Ukraine agreeing to cede territory (Polymarket CM-EVT-XP7FFT2MC9, 3%) is priced even lower, suggesting markets see no imminent deal on either process or terms."
  - "Iran agreeing to end uranium enrichment by year-end (Polymarket CM-EVT-4CKJ2D3T77) also sits at 3%, reflecting broad market skepticism across multiple parallel geopolitical negotiating tracks."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump repositioned nuclear submarines and pressured Moscow while the Trump-Putin-Xi joint peace declaration produced no concrete ceasefire framework."
    publisher: "link.cfr.org"
    published_at: "2026-11-20T00:00:00.000Z"
    source_url: "https://link.cfr.org/public/40979402"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "link.cfr.org"
        source_url: "https://link.cfr.org/public/40979402"
        retrieved_at: "2026-11-21T07:47:41+00:00"
  - type: "pm_response"
    notes: "Polymarket contract on the ceasefire is a multi-deadline series; UMA oracle resolution means any verified ceasefire agreement would trigger settlement."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "link.cfr.org: Across the Globe"
    url: "https://link.cfr.org/public/40979402"
    published_at: "2026-11-20T00:00:00.000Z"
    retrieved_at: "2026-11-21T07:47:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
