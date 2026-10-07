---
signal_id: "CMSIG2026100602"
signal_slug: "fed-funds-at-oct-meeting-kalshi-ladder-holds-4-0-ceiling-2026-10-06"
headline: "Fed funds at Oct meeting: Kalshi ladder holds 4.0% ceiling"
semantic_title: "October Fed hike stays a long shot near 4 percent ceiling"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-06T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Federal funds upper bound following October 2026 Fed meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.18
  volume_24h_usd: 3127.45
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi ladder shows 99% above 3.75% but only 18% above 4.00%, implying the market sees the upper bound firmly at 4.00% after October."
  - "Jefferson and Williams remarks aligning with a pause are consistent with the ladder heavily resisting a move above 4.00%."
  - "The post-next-meeting ladder (CM-EVT-MR57HVWJT3) prices 78% above 4.00%, showing the market is open to one more move later but not in October."
  - "Resolves via the Federal Reserve's official post-October meeting rate announcement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Vice Chair Philip Jefferson and New York Fed President John Williams signaled a pause, collapsing October hike odds from 70% to 25% according to news reports."
    publisher: "The Macro, Rates Desk"
    published_at: "2026-10-06T00:00:00.000Z"
    source_url: "https://gokhshtein.com/news/2026-10-06-october-hike-odds-collapse-to-25-as-fed-deputies-show-pause"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Macro, Rates Desk"
        source_url: "https://gokhshtein.com/news/2026-10-06-october-hike-odds-collapse-to-25-as-fed-deputies-show-pause"
        retrieved_at: "2026-10-07T07:47:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution provided; no confirmed intraday price shift, current distribution reflects post-remarks pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Macro, Rates Desk: October Hike Odds Fall to 25% After Fed Deputies Show Pause | Gokhshte"
    url: "https://gokhshtein.com/news/2026-10-06-october-hike-odds-collapse-to-25-as-fed-deputies-show-pause"
    published_at: "2026-10-06T00:00:00.000Z"
    retrieved_at: "2026-10-07T07:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
