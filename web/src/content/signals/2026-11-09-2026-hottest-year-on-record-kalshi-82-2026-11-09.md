---
signal_id: "CMSIG2026110907"
signal_slug: "2026-hottest-year-on-record-kalshi-82-2026-11-09"
headline: "2026 hottest year on record: Kalshi 82%"
semantic_title: "2026 hottest year ever stays heavily favored at 82%"
telemetry: "Kalshi 82%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-09T08:52:03.000Z"
event_id: "CM-EVT-F7CHTL6JQ3"
event_slug: "kxgtemp-27"
event_question: "Will 2026 be the hottest year ever?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGTEMP-27-P0"
  question_raw: "Will 2026 be the hottest year on record?"
  current_price: 0.82
  volume_24h_usd: 22.44
  arbitration_model: "kalshi_staff"
  resolution_source: "NASA Goddard
Institute for Space Studies"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi puts 82% odds on 2026 being the hottest year ever recorded, resolving via NASA Goddard Institute for Space Studies data."
  - "COP31 convening under explicit climate-crisis pressure is consistent with the market's strong lean toward a record-setting year."
  - "A duplicate Kalshi contract (CM-EVT-MYCFX29QF6) also prices at 82%, confirming the consensus is stable across contract instances."
  - "Resolution depends on NASA GISS final annual temperature ranking; the contract requires 2026 to rank number one globally, not merely above a specific threshold."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "COP31 opened in Antalya with more than 100,000 attendees and leaders under pressure to accelerate climate action."
    publisher: "Yahoo News Singapore"
    published_at: "2026-11-09T08:52:03.000Z"
    source_url: "https://sg.news.yahoo.com/cop31-opens-climate-geopolitical-pressures-012632028.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yahoo News Singapore"
        source_url: "https://sg.news.yahoo.com/cop31-opens-climate-geopolitical-pressures-012632028.html"
        retrieved_at: "2026-11-10T07:47:48+00:00"
  - type: "pm_response"
    notes: "Kalshi binary at 82%; resolution via NASA Goddard Institute for Space Studies annual global temperature data; duplicate contract cross-checks confirm pricing consistency."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yahoo News Singapore: COP31 opens with leaders under pressure to tackle climate crisis"
    url: "https://sg.news.yahoo.com/cop31-opens-climate-geopolitical-pressures-012632028.html"
    published_at: "2026-11-09T08:52:03.000Z"
    retrieved_at: "2026-11-10T07:47:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
