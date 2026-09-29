---
signal_id: "CMSIG2026092801"
signal_slug: "sept-nfp-implied-90k-100k-kalshi-ladder-volume-up-739x-2026-09-28"
headline: "Sept NFP implied 90K-100K: Kalshi ladder, volume up 739x"
semantic_title: "September payrolls seen landing near 90K to 100K"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-09-28T06:22:53.000Z"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "September 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T100000"
  question_raw: "Will above 100000 jobs be added in September 2026?"
  current_price: 0.46
  volume_24h_usd: 2471.6
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Kalshi ladder puts the September 2026 payrolls implied range at roughly 90K-100K, with 59% pricing above 90K but only 46% above 100K."
  - "Trading volume on the Kalshi payrolls ladder surged 739x day-over-day, signaling intense fresh positioning ahead of Friday's release."
  - "The wide sell-side estimate range (35K-180K) matches the ladder's fat distribution tails, with 83% still pricing above 30K."
  - "The 125K strike commands only 28% odds, suggesting markets are not pricing a strong beat versus the 84K street consensus."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "FXStreet reports Friday's September jobs report is the week's key macro event, with consensus at 84,000 and a wide estimate range of 35,000-180,000."
    publisher: "fxstreet.com"
    published_at: "2026-09-28T06:22:53.000Z"
    source_url: "https://www.fxstreet.com/analysis/yields-rip-higher-as-focus-shifts-to-jobs-data-202609280622"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "fxstreet.com"
        source_url: "https://www.fxstreet.com/analysis/yields-rip-higher-as-focus-shifts-to-jobs-data-202609280622"
        retrieved_at: "2026-09-29T14:34:30+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on September 2026 nonfarm payrolls; day-over-day volume surge of 738.8x confirms high pre-release attention."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "fxstreet.com: Yields rip higher as focus shifts to jobs data"
    url: "https://www.fxstreet.com/analysis/yields-rip-higher-as-focus-shifts-to-jobs-data-202609280622"
    published_at: "2026-09-28T06:22:53.000Z"
    retrieved_at: "2026-09-29T14:34:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
