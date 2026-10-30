---
signal_id: "CMSIG2026102907"
signal_slug: "texas-senate-democrat-win-kalshi-30-2026-10-29"
headline: "Texas Senate Democrat win: Kalshi 30%"
semantic_title: "Texas Senate Democratic win holds near 30% odds"
telemetry: "Kalshi 30%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-29T20:00:00.000Z"
event_id: "CM-EVT-G8PMBQ1FF1"
event_slug: "senatetx-26"
event_question: "Texas Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATETX-26-R"
  question_raw: "Will Republicans win the Senate race in Texas?"
  current_price: 0.3
  volume_24h_usd: 814824.45
  arbitration_model: "kalshi_staff"
  resolution_source: "United States Congress"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "The Kalshi contract on a Democratic Texas Senate win sits at 30%, resolved by the United States Congress."
  - "A two-point Talarico lead in the TSU poll is directionally consistent with the 30% probability, the market sees Texas as competitive but still favors Paxton."
  - "The market is not fully pricing the poll result; a 49-47 Democratic lead would imply closer to 50% odds if taken at face value."
  - "The Mississippi Senate race (CM-EVT-6R8L57X0Y4) is 89% likely to be decided by January 4, 2027, while the Georgia race (CM-EVT-1S96Y2D1N4) sits at 96%, both suggest the broader Senate map resolves cleanly, putting Texas in focus as a live contest."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A Texas Southern University poll of 2,000 likely voters shows Democrat James Talarico leading Republican Ken Paxton by two points, 49% to 47%, in the US Senate race."
    publisher: "Orko Manna"
    published_at: "2026-10-29T20:00:00.000Z"
    source_url: "https://www.khou.com/article/news/politics/elections/texas-poll-talarico-paxton-abbott-hinojosa-2026/285-a6400c96-b327-4979-92ba-bc222c1f12c4"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Orko Manna"
        source_url: "https://www.khou.com/article/news/politics/elections/texas-poll-talarico-paxton-abbott-hinojosa-2026/285-a6400c96-b327-4979-92ba-bc222c1f12c4"
        retrieved_at: "2026-10-30T07:48:00+00:00"
  - type: "pm_response"
    notes: "Kalshi prices Texas Democratic Senate odds at 30%, below what a two-point poll lead might imply, reflecting the market's structural lean toward Paxton in a red-leaning state."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Orko Manna: New TSU poll shows tight U.S. Senate and Texas Governor races ahead of"
    url: "https://www.khou.com/article/news/politics/elections/texas-poll-talarico-paxton-abbott-hinojosa-2026/285-a6400c96-b327-4979-92ba-bc222c1f12c4"
    published_at: "2026-10-29T20:00:00.000Z"
    retrieved_at: "2026-10-30T07:48:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
