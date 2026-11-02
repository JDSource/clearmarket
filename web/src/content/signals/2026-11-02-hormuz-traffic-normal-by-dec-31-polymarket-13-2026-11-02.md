---
signal_id: "CMSIG2026110206"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-13-2026-11-02"
headline: "Hormuz traffic normal by Dec 31: Polymarket 13%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end stays a long shot"
telemetry: "Polymarket 13%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-02T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.13
  volume_24h_usd: 56480.436224
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by December 31 at just 13%, a strong long-shot read."
  - "Tehran's conditional offer via Qatar is a significant diplomatic signal, but the Polymarket contract shows markets are not treating it as a near-certain breakthrough."
  - "The gap between the headline optimism and the 13% contract price reflects skepticism about US acceptance and implementation speed."
  - "Iran nuclear test (CM-EVT-YQ6BFV3GX1 at 4%) and NPT withdrawal (CM-EVT-BR5SMCCW00 at 7%) contracts suggest markets see escalation as unlikely but not zero."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran passed a proposal through Qatari mediators promising restored Hormuz security if the US agrees to a two-day diplomatic plan."
    publisher: "Barbara Angopa, Usaid Siddiqui"
    published_at: "2026-11-02T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/liveblog/2026/11/2/iran-war-live-tankers-hit-in-hormuz-trump-again-says-conflict-to-end-soon"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Barbara Angopa, Usaid Siddiqui"
        source_url: "https://www.aljazeera.com/news/liveblog/2026/11/2/iran-war-live-tankers-hit-in-hormuz-trump-again-says-conflict-to-end-soon"
        retrieved_at: "2026-11-02T17:44:20+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle based on verified reports of normalized commercial shipping through the Strait of Hormuz by December 31."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Barbara Angopa, Usaid Siddiqui: Iran war live: Tehran says Hormuz ‘security restored’ if US agrees to"
    url: "https://www.aljazeera.com/news/liveblog/2026/11/2/iran-war-live-tankers-hit-in-hormuz-trump-again-says-conflict-to-end-soon"
    published_at: "2026-11-02T00:00:00.000Z"
    retrieved_at: "2026-11-02T17:44:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
