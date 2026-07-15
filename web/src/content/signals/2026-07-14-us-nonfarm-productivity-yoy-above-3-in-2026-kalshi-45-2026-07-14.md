---
signal_id: "CMSIG2026071403"
signal_slug: "us-nonfarm-productivity-yoy-above-3-in-2026-kalshi-45-2026-07-14"
headline: "US nonfarm productivity YoY above 3% in 2026: Kalshi 45%"
semantic_title: "Nonfarm productivity above 3 percent in 2026 anchors near even odds"
telemetry: "Kalshi 45%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-14T13:13:22.000Z"
event_id: "CM-EVT-99JZRM47M6"
event_slug: "kxnfprod-27mar04"
event_question: "Will U.S. nonfarm productivity year-over-year growth exceed 3% in any quarter of 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXNFPROD-27MAR04-T3"
  question_raw: "Will U.S. nonfarm productivity YoY in any quarter for 2026 be above 3%?"
  current_price: 0.45
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics- Employment Situation"
  resolves_at: "2027-06-02T15:30:00Z"
bullets:
  - "Kalshi prices the US nonfarm productivity YoY above 3% in any 2026 quarter at 45%, near even odds."
  - "Cooling inflation reduces nominal output distortion, but does not directly confirm real productivity gains above 3%."
  - "The Fed holding rates steady despite softer CPI keeps financing costs elevated, which could compress capital investment and weigh on productivity."
  - "Resolves via Bureau of Labor Statistics Employment Situation releases; quarterly data cadence means multiple resolution windows remain in 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "June CPI cooled sharply to 3.5% annual, with core inflation also slowing, giving the Fed breathing room without triggering imminent rate cuts."
    publisher: "americanbanker.com"
    published_at: "2026-07-14T13:13:22.000Z"
    source_url: "https://www.americanbanker.com/news/inflation-slowed-to-3-5-in-june-giving-fed-breathing-room"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "americanbanker.com"
        source_url: "https://www.americanbanker.com/news/inflation-slowed-to-3-5-in-june-giving-fed-breathing-room"
        retrieved_at: "2026-07-15T10:00:10+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 45% reflects genuine uncertainty; the CPI print is an indirect catalyst, not a direct productivity signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "americanbanker.com: Inflation slowed to 3.5% in June, giving Fed breathing room | American"
    url: "https://www.americanbanker.com/news/inflation-slowed-to-3-5-in-june-giving-fed-breathing-room"
    published_at: "2026-07-14T13:13:22.000Z"
    retrieved_at: "2026-07-15T10:00:10+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
