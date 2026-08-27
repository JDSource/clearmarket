---
signal_id: "CMSIG2026082504"
signal_slug: "dems-sweep-core-four-senate-races-by-2026-kalshi-55-2026-08-25"
headline: "Dems sweep core four Senate races by 2026: Kalshi 55%"
semantic_title: "Democrats sweeping four core Senate races sits near 50%"
telemetry: "Kalshi 55%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-25T00:00:00.000Z"
event_id: "CM-EVT-QH62PP4D92"
event_slug: "kxdemcorefoursenatesweep-26nov03"
event_question: "Will Democrats sweep the core four Senate races by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXDEMCOREFOURSENATESWEEP-26NOV03"
  question_raw: "Will Democrats win the 2026 senate elections in Georgia, Michigan, North Carolina, AND Maine?"
  current_price: 0.55
  volume_24h_usd: 2979.32
  arbitration_model: "kalshi_staff"
  resolution_source: "Bloomberg"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi prices a 55% chance Democrats sweep the four core Senate races, resolves via Bloomberg."
  - "Canada trade war escalation in border-state Senate battlegrounds is consistent with the market tilting just above 50% toward a Democratic sweep."
  - "The broader House majority market (CM-EVT-FV8MR86S63) at 84% on Kalshi shows higher Democratic confidence in the House than in the Senate sweep."
  - "Resolves via Bloomberg's official call of the four designated Senate race outcomes after the November 2026 elections."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump's escalating trade war with Canada is threatening Republican Senate candidates in border states, with control of the U.S. Senate potentially hinging on affected races."
    publisher: "The Associated Press"
    published_at: "2026-08-25T00:00:00.000Z"
    source_url: "https://www.wndu.com/2026/08/25/trumps-trade-war-with-canada-could-rattle-economies-states-with-key-senate-races/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Associated Press"
        source_url: "https://www.wndu.com/2026/08/25/trumps-trade-war-with-canada-could-rattle-economies-states-with-key-senate-races/"
        retrieved_at: "2026-08-27T18:46:25+00:00"
  - type: "pm_response"
    notes: "Kalshi at 55% for a Senate sweep reflects genuine uncertainty; the gap to 84% House odds implies the Senate path is meaningfully harder for Democrats."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Associated Press: Trump’s trade war with Canada could rattle economies in states with ke"
    url: "https://www.wndu.com/2026/08/25/trumps-trade-war-with-canada-could-rattle-economies-states-with-key-senate-races/"
    published_at: "2026-08-25T00:00:00.000Z"
    retrieved_at: "2026-08-27T18:46:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
