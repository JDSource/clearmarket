---
signal_id: "CMSIG2026062703"
signal_slug: "june-2026-payrolls-above-125k-ladder-implied-37-2026-06-27"
headline: "June 2026 payrolls above 125K: ladder-implied 37%"
semantic_title: "June payrolls above 125K fractures from base-case pricing"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-06-27T03:01:18.953Z"
event_id: "CM-EVT-NHWMG744L8"
event_slug: "kxpayrolls-26jun"
event_question: "June 2026 US nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26JUN-T125000"
  question_raw: "Will above 125000 jobs be added in June 2026?"
  current_price: 0.37
  volume_24h_usd: 720.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2026-07-02T14:00:00Z"
bullets:
  - "Kalshi ladder prices 58% above 100K jobs and 37% above 125K, implying the market sees a decent but not blowout June payroll print as the base case."
  - "The jobs report is not yet released; the market is positioned ahead of the July 3 print with the bulk of probability mass between 60K and 125K."
  - "The distribution shows 95% above negative 25K, meaning the market assigns near-zero odds to an outright contraction in payrolls."
  - "Resolves via the Bureau of Labor Statistics Employment Situation report; the implied central range of 100K-125K would likely support the Fed's hold posture."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Kiplinger previews the June 29-July 3 economic data week, with the June jobs report (due July 3) expected to reinforce the Fed's inflation-first stance."
    publisher: "By
 Karee Venema   
 
 
 
last updated
 
26 June 2026
 
 
 
 
 
 
 in  News"
    published_at: "2026-06-27T03:01:18.953Z"
    source_url: "https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "By
 Karee Venema   
 
 
 
last updated
 
26 June 2026
 
 
 
 
 
 
 in  News"
        source_url: "https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar"
        retrieved_at: "2026-06-27T10:02:20+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract on June 2026 nonfarm payrolls; pre-report positioning clusters between 60K and 125K with a sharp drop-off above that level."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "By
 Karee Venema   
 
 
 
last updated
 
26 June 2026
 
 
 
 
 
 
 in  News: What to Look Out for in Economic Data This Week (June 29-July 3)"
    url: "https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar"
    published_at: "2026-06-27T03:01:18.953Z"
    retrieved_at: "2026-06-27T10:02:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
