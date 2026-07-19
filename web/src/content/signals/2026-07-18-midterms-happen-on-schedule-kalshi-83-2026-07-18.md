---
signal_id: "CMSIG2026071807"
signal_slug: "midterms-happen-on-schedule-kalshi-83-2026-07-18"
headline: "Midterms happen on schedule: Kalshi 83%"
semantic_title: "Midterm elections on schedule absorbs Trump integrity pressure"
telemetry: "Kalshi 83%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-18T00:00:00.000Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.83
  volume_24h_usd: 165.39
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi prices 83% on the midterm elections proceeding on schedule, despite sustained White House pressure on election administration."
  - "Trump's primetime address and Mullin's follow-on enforcement threats have not pushed the market below its current 83% on-schedule probability."
  - "The 17% residual off-schedule probability reflects non-trivial market concern that election administration disputes could delay or disrupt the November contests."
  - "Resolution is via The Washington Post reporting on whether elections proceed on their statutory date; legal or administrative disruption, not just political rhetoric, would be required for a NO resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump and allies escalated attacks on US election security ahead of the midterms, with Homeland Security Secretary Markwayne Mullin pushing states to comply with election demands after Trump's primetime address raising doubts about election integrity."
    publisher: "dnyuz.com"
    published_at: "2026-07-18T00:00:00.000Z"
    source_url: "https://dnyuz.com/2026/07/18/trump-allies-seek-to-sow-mistrust-about-election-security-ahead-of-midterms/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "dnyuz.com"
        source_url: "https://dnyuz.com/2026/07/18/trump-allies-seek-to-sow-mistrust-about-election-security-ahead-of-midterms/"
        retrieved_at: "2026-07-19T09:48:56+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolved via The Washington Post; 83% reflects broad but not universal confidence that institutions hold despite political pressure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "dnyuz.com: Trump, allies seek to sow mistrust about election security ahead of mi"
    url: "https://dnyuz.com/2026/07/18/trump-allies-seek-to-sow-mistrust-about-election-security-ahead-of-midterms/"
    published_at: "2026-07-18T00:00:00.000Z"
    retrieved_at: "2026-07-19T09:48:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
