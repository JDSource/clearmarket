---
signal_id: "CMSIG2026062606"
signal_slug: "june-unemployment-rate-u-3-kalshi-4-2-4-3-2026-06-26"
headline: "June unemployment rate (U-3): Kalshi 4.2-4.3%"
semantic_title: "June unemployment rate consensus anchors near 4.2 to 4.3 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-26T19:44:29.000Z"
event_id: "CM-EVT-FJGT56DTV2"
event_slug: "kxu3-26jun"
event_question: "June 2026 unemployment rate (U-3)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26JUN-T4.3"
  question_raw: "Will the unemployment rate (U-3) be above 4.3% in June?"
  current_price: 0.3
  volume_24h_usd: 243.64
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-02T14:00:00Z"
bullets:
  - "Kalshi ladder implies June unemployment in the 4.2-4.3% range: 72% above 4.2% but only 30% above 4.3%; trading volume up 808x day over day."
  - "Consumer-bruised-by-inflation narrative fits a softening labor market, and the ladder pricing is directionally consistent."
  - "Companion Kalshi ladder on June nonfarm payrolls implies 100K-125K jobs added; both reads point to a cooling but not collapsing labor market."
  - "Resolves via Bureau of Labor Statistics June 2026 jobs report; U-3 is the headline unemployment measure."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A June executive briefing flagged persistent inflation and eroding consumer ability to absorb higher prices."
    publisher: "chloetejada"
    published_at: "2026-06-26T19:44:29.000Z"
    source_url: "https://www.rbcwealthmanagement.com/en-us/insights/june-monthly-exec-briefing-us-consumer-bruised-by-persistent-inflation"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "chloetejada"
        source_url: "https://www.rbcwealthmanagement.com/en-us/insights/june-monthly-exec-briefing-us-consumer-bruised-by-persistent-inflation"
        retrieved_at: "2026-06-29T12:28:56+00:00"
  - type: "pm_response"
    notes: "The 808x surge in Kalshi ladder volume signals intense pre-release positioning ahead of the June jobs print."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "chloetejada: June Monthly Exec Briefing: U.S. consumer bruised by persistent inflat"
    url: "https://www.rbcwealthmanagement.com/en-us/insights/june-monthly-exec-briefing-us-consumer-bruised-by-persistent-inflation"
    published_at: "2026-06-26T19:44:29.000Z"
    retrieved_at: "2026-06-29T12:28:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
