---
signal_id: "CMSIG2026072704"
signal_slug: "us-effective-tariff-rate-seen-at-7-5-10-ladder-2026-07-27"
headline: "US effective tariff rate seen at 7.5-10%: ladder"
semantic_title: "US effective tariff rate holds near 7.5-10 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-27T00:00:00.000Z"
event_id: "CM-EVT-8P2Y9LGSL3"
event_slug: "kxefftariff-26jul30"
event_question: "US effective tariff rate (customs duties / nominal imports) 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXEFFTARIFF-26JUL30-T10"
  question_raw: "Will the US effective tariff rate (customs duties collected ÷ nominal imports of goods, represented by B235RC1Q027SBEA ÷ A255RC1Q027SBEA) for Q2 2026 be above 10%?"
  current_price: 0.14
  volume_24h_usd: 4.72
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics- Employment Situation"
  resolves_at: "2026-08-06T14:00:00Z"
bullets:
  - "The ladder prices the US effective tariff rate at 7.5-10%, with 63% above 7.5% but only 14% above 10%, implying exemptions and deals will cap the realized rate."
  - "New tariffs on 60-plus countries covering nearly all imports are consistent with the 7.5% floor being well-priced, but the sharp drop above 10% shows markets doubt full pass-through."
  - "Exclusions for oil, gas, fertilizer, and certain food items noted in the news are likely driving the ladder's skepticism above the 10% strike."
  - "Companion event CM-EVT-RJRTFQZDJ0 puts only 20% odds on the Supreme Court hearing a tariff case in 2026, suggesting markets do not expect a rapid legal check on the new duties."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Trump administration unveiled new double-digit tariffs on more than 60 trading partners covering 99.4% of US imports, escalating trade tensions in a different macro environment from last year's Liberation Day."
    publisher: "Hugh Leask"
    published_at: "2026-07-27T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/07/27/donald-trump-tariffs-trade-war-iran.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Hugh Leask"
        source_url: "https://www.cnbc.com/2026/07/27/donald-trump-tariffs-trade-war-iran.html"
        retrieved_at: "2026-07-27T11:15:45+00:00"
  - type: "pm_response"
    notes: "Ladder distribution from prediction markets (venue unspecified in data) reflects the gap between headline tariff rates and realized customs collections after exclusions."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Hugh Leask: Why Trump's new tariff blitz is different this time round"
    url: "https://www.cnbc.com/2026/07/27/donald-trump-tariffs-trade-war-iran.html"
    published_at: "2026-07-27T00:00:00.000Z"
    retrieved_at: "2026-07-27T11:15:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
