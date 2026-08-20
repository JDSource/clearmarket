---
signal_id: "CMSIG2026081905"
signal_slug: "us-aug-unemployment-rate-seen-4-1-4-2-kalshi-ladder-2026-08-19"
headline: "US Aug unemployment rate seen 4.1-4.2%: Kalshi ladder"
semantic_title: "Unemployment rate in August prices in near 4.1 to 4.2 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-19T00:00:00.000Z"
event_id: "CM-EVT-CN1M891289"
event_slug: "kxu3-26aug"
event_question: "US unemployment rate (U-3), August 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26AUG-T4.2"
  question_raw: "Will the unemployment rate (U-3) be above 4.2% in August?"
  current_price: 0.31
  volume_24h_usd: 2258.84
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-04T14:00:00Z"
bullets:
  - "Kalshi ladder implies August unemployment near 4.1%-4.2%, with 55% above 4.1% but only 31% above 4.2%, a narrow central range."
  - "Disappointing August data is consistent with the ladder's pricing above 4.0%, where 86% of weight sits, well above the sub-4% territory."
  - "The separate peak unemployment ladder prices only 27% above 4.5% before 2027, suggesting markets do not see a sharp labor market deterioration ahead."
  - "White House characterization of an upward trajectory is at odds with market pricing that puts the rate solidly above 4.0% through August."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "August economic data has disappointed, with July hiring and other indicators undermining the narrative of a strong US economy."
    publisher: "Kevin Smith"
    published_at: "2026-08-19T00:00:00.000Z"
    source_url: "https://www.marketscreener.com/news/should-we-be-worried-about-the-us-economy-ce7859dcd989fe2c"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kevin Smith"
        source_url: "https://www.marketscreener.com/news/should-we-be-worried-about-the-us-economy-ce7859dcd989fe2c"
        retrieved_at: "2026-08-20T08:32:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Bureau of Labor Statistics Employment Situation report; 96% above 3.7% reflects virtually no chance of a return to prior lows."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kevin Smith: Should we be worried about the US economy? | MarketScreener"
    url: "https://www.marketscreener.com/news/should-we-be-worried-about-the-us-economy-ce7859dcd989fe2c"
    published_at: "2026-08-19T00:00:00.000Z"
    retrieved_at: "2026-08-20T08:32:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
