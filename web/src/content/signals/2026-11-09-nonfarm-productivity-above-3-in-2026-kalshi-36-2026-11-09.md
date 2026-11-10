---
signal_id: "CMSIG2026110904"
signal_slug: "nonfarm-productivity-above-3-in-2026-kalshi-36-2026-11-09"
headline: "Nonfarm productivity above 3% in 2026: Kalshi 36%"
semantic_title: "Productivity above 3 percent stays a long shot at 36%"
telemetry: "Kalshi 36%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-09T07:54:32.000Z"
event_id: "CM-EVT-99JZRM47M6"
event_slug: "kxnfprod-27mar04"
event_question: "Will U.S. nonfarm productivity year-over-year growth exceed 3% in any quarter of 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXNFPROD-27MAR04-T3"
  question_raw: "Will U.S. nonfarm productivity YoY in any quarter for 2026 be above 3%?"
  current_price: 0.36
  volume_24h_usd: 0.72
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics- Employment Situation"
  resolves_at: "2027-06-02T15:30:00Z"
bullets:
  - "Kalshi puts 36% odds on US nonfarm productivity year-over-year growth exceeding 3% in any quarter of 2026, resolving via BLS Employment Situation."
  - "The analyst thesis that productivity could neutralize inflationary pressure from payroll gains is a minority view: the market assigns it less than 4-in-10 odds."
  - "If productivity fails to exceed 3%, the Fed's case for hiking based on labor market strength alone becomes more straightforward."
  - "Resolution requires BLS to report a single quarter of productivity growth above 3% year-over-year before year-end; partial quarters do not qualify."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "An independent analyst argued the strong October jobs surprise may be less inflationary than markets think if productivity gains absorb labor cost pressure."
    publisher: "Nikolaos Akkizidis"
    published_at: "2026-11-09T07:54:32.000Z"
    source_url: "https://www.fxstreet.com/analysis/the-us-jobs-surprise-may-be-less-inflationary-than-markets-think-202611090754"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Nikolaos Akkizidis"
        source_url: "https://www.fxstreet.com/analysis/the-us-jobs-surprise-may-be-less-inflationary-than-markets-think-202611090754"
        retrieved_at: "2026-11-10T07:47:48+00:00"
  - type: "pm_response"
    notes: "Kalshi binary contract; resolves via Bureau of Labor Statistics Employment Situation report; 36% reflects a meaningful but sub-consensus probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Nikolaos Akkizidis: The US jobs surprise may be less inflationary than markets think"
    url: "https://www.fxstreet.com/analysis/the-us-jobs-surprise-may-be-less-inflationary-than-markets-think-202611090754"
    published_at: "2026-11-09T07:54:32.000Z"
    retrieved_at: "2026-11-10T07:47:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
