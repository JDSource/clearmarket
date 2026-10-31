---
signal_id: "CMSIG2026103106"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-12-2026-10-31"
headline: "Hormuz traffic normal by Dec 31: Polymarket 12%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end stays a long shot"
telemetry: "Polymarket 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-31T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.12
  volume_24h_usd: 97443.39567
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 sits at just 12%, via UMA oracle."
  - "Fresh tanker strikes in the Strait are consistent with the market's heavy discount on near-term resolution, the price does not reflect Trump's optimistic framing."
  - "WSJ separately reported US and Israeli military preparations for possible post-midterm strikes, adding further downside risk to the resolution window."
  - "Resolution via UMA oracle; the December 31 deadline is tight given active military operations and ongoing Iranian threats."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran reported four tankers hit by mines in the Strait of Hormuz, with Trump saying the war on Iran will get wrapped up soon."
    publisher: "Heba Habib, Alex Milan Durie, Christine Maguire"
    published_at: "2026-10-31T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/liveblog/2026/10/31/iran-war-live-oil-tankers-hit-in-hormuz-trump-says-conflict-will-end-soon"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Heba Habib, Alex Milan Durie, Christine Maguire"
        source_url: "https://www.aljazeera.com/news/liveblog/2026/10/31/iran-war-live-oil-tankers-hit-in-hormuz-trump-says-conflict-will-end-soon"
        retrieved_at: "2026-10-31T07:48:23+00:00"
  - type: "pm_response"
    notes: "Polymarket at 12% on Hormuz normalization by year-end reflects a market that is firmly skeptical of Trump's 'wrapped up soon' characterization, with active hostilities ongoing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Heba Habib, Alex Milan Durie, Christine Maguire: Iran war live: 4 tankers hit in Hormuz; Trump says conflict will end s"
    url: "https://www.aljazeera.com/news/liveblog/2026/10/31/iran-war-live-oil-tankers-hit-in-hormuz-trump-says-conflict-will-end-soon"
    published_at: "2026-10-31T00:00:00.000Z"
    retrieved_at: "2026-10-31T07:48:23+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
