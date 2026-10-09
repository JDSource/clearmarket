---
signal_id: "CMSIG2026100902"
signal_slug: "oct-payrolls-seen-60k-70k-kalshi-ladder-surges-2026-10-09"
headline: "Oct payrolls seen 60K-70K: Kalshi ladder surges"
semantic_title: "October payrolls odds build around 60K to 70K range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-09T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "Nonfarm payrolls added, October 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T70000"
  question_raw: "Will above 70000 jobs be added in October 2026?"
  current_price: 0.47
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "The Kalshi payrolls ladder puts the implied range for October at 60,000-70,000: 59% above 60K but only 47% above 70K."
  - "September's 29,000 print shocked to the downside, and trading volume on this contract exploded 1,045x day over day, the labor market outlook is drawing heavy fresh positioning."
  - "The ladder shows 86% above zero and 92% above negative 25,000, so the market is not pricing an outright contraction, just a soft trend month."
  - "The Kalshi contract on a Fed cut greater than 25 basis points this year holds at 3%, suggesting soft payrolls alone are not enough to shift the market toward aggressive easing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A soft September jobs print of just 29,000 nonfarm payrolls cooled October Fed rate-hike expectations and triggered broad cross-asset repricing."
    publisher: "blog.e8markets.com"
    published_at: "2026-10-09T00:00:00.000Z"
    source_url: "https://blog.e8markets.com/article/soft-us-jobs-report-tilts-october-fed-odds-toward-a-pause"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "blog.e8markets.com"
        source_url: "https://blog.e8markets.com/article/soft-us-jobs-report-tilts-october-fed-odds-toward-a-pause"
        retrieved_at: "2026-10-09T14:55:32+00:00"
  - type: "pm_response"
    notes: "The Kalshi payrolls ladder volume surged over 1,000x day over day alongside the September miss, with October implied range clustering at 60K-70K."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "blog.e8markets.com: Soft U.S. Jobs Report Tilts October Fed Odds Toward a Pause | E8 Marke"
    url: "https://blog.e8markets.com/article/soft-us-jobs-report-tilts-october-fed-odds-toward-a-pause"
    published_at: "2026-10-09T00:00:00.000Z"
    retrieved_at: "2026-10-09T14:55:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
