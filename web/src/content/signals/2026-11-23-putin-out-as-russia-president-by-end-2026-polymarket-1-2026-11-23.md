---
signal_id: "CMSIG2026112306"
signal_slug: "putin-out-as-russia-president-by-end-2026-polymarket-1-2026-11-23"
headline: "Putin out as Russia president by end-2026: Polymarket 1%"
semantic_title: "Putin leaving Russian presidency by year-end stays a long shot"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-23T06:53:00.000Z"
event_id: "CM-EVT-5WJSMVBVS7"
event_slug: "putin-out-before-2027"
event_question: "Will Vladimir Putin no longer be President of Russia by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6bd56627aa21311850825edb27e53434a0e17a4f782be0086bc07f71eee00d0d"
  question_raw: "Putin out as President of Russia by December 31, 2026?"
  current_price: 0.013
  volume_24h_usd: 29599.019233
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T18:30:00Z"
bullets:
  - "The Polymarket prediction market puts just 1% odds on Putin no longer serving as Russian president by end of 2026."
  - "U.S. intelligence officials publicly endorsing Trump's warm rhetoric toward Putin reinforces political continuity in Moscow; the market's near-zero pricing is consistent with that signal."
  - "Trading volume on this contract rose roughly 64x day-over-day, suggesting the Trump-Putin friendship framing drew fresh scrutiny without shifting the odds."
  - "The Trump-Putin-Zelensky trilateral meeting contracts (Polymarket CM-EVT-FNBRJ6KY59 at 3%, CM-EVT-QP1YL1BSS0 at 5%) show a similarly skeptical market on diplomatic breakthroughs before year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "U.S. intelligence chief said Trump's description of Vladimir Putin as a friend is entirely appropriate, underscoring continued diplomatic engagement between Washington and Moscow."
    publisher: "Bridget Brown"
    published_at: "2026-11-23T06:53:00.000Z"
    source_url: "https://apnews.com/live/donald-trump-politics-news-updates-11-23-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Bridget Brown"
        source_url: "https://apnews.com/live/donald-trump-politics-news-updates-11-23-2026"
        retrieved_at: "2026-11-25T07:47:45+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the volume spike flags renewed attention after the intelligence chief's remarks, but odds remain near zero."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Bridget Brown: Live updates: Trump’s calling Putin a ‘friend’ is ‘entirely appropriat"
    url: "https://apnews.com/live/donald-trump-politics-news-updates-11-23-2026"
    published_at: "2026-11-23T06:53:00.000Z"
    retrieved_at: "2026-11-25T07:47:45+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
