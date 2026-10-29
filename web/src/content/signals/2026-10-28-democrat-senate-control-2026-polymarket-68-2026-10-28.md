---
signal_id: "CMSIG2026102803"
signal_slug: "democrat-senate-control-2026-polymarket-68-2026-10-28"
headline: "Democrat Senate control 2026: Polymarket 68%"
semantic_title: "Democrats hold slim edge in Senate control odds"
telemetry: "Polymarket 68%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T00:00:00.000Z"
event_id: "CM-EVT-M9WJY06T90"
event_slug: "which-party-will-win-the-senate-in-2026"
event_question: "Which party will win control of the U.S. Senate in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x307a1ed89d60b61002dd5bbf00e1408c5ed2ab3fcdb056191ca7ef9bc34d38f3"
  question_raw: "Will the Democratic Party control the Senate after the 2026 Midterm elections?"
  current_price: 0.68
  volume_24h_usd: 180990.59895899997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democrats winning Senate control at 68%, a clear lean but not a near-certain outcome."
  - "Competing Kalshi contract (CM-EVT-YKHDL92349) puts Republicans winning the Senate at only 33%, consistent with the 68% Democratic read across venues."
  - "Kalshi separately prices Republican control of at least one chamber of Congress at 65% (CM-EVT-T5VXKJT451), implying the House remains the more likely GOP hold."
  - "Resolves via uma_oracle on Polymarket; the Kalshi Senate contract resolves via Library of Congress certification."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "With five days until the US midterm elections, Trump is campaigning to defend red-state Senate seats while Obama rallies for Democratic candidates in competitive states."
    publisher: "Elissa Fitzgerald"
    published_at: "2026-10-28T00:00:00.000Z"
    source_url: "https://www.abc.net.au/news/2026-10-29/us-midterms-daily-news-briefing-trump-obama/107318004"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Elissa Fitzgerald"
        source_url: "https://www.abc.net.au/news/2026-10-29/us-midterms-daily-news-briefing-trump-obama/107318004"
        retrieved_at: "2026-10-29T07:47:47+00:00"
  - type: "pm_response"
    notes: "Polymarket and Kalshi contracts are cross-venue consistent; no contradictory signals between venues on Senate direction."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Elissa Fitzgerald: US midterms briefing: Trump expands hunt for voter fraud ahead of midt"
    url: "https://www.abc.net.au/news/2026-10-29/us-midterms-daily-news-briefing-trump-obama/107318004"
    published_at: "2026-10-28T00:00:00.000Z"
    retrieved_at: "2026-10-29T07:47:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
