---
signal_id: "CMSIG2026110503"
signal_slug: "oct-payrolls-implied-60k-70k-kalshi-ladder-58-48-2026-11-05"
headline: "Oct payrolls implied 60K-70K: Kalshi ladder 58%/48%"
semantic_title: "October payrolls consensus sits near 60K to 70K"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-11-05T09:38:43.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T70000"
  question_raw: "Will above 70000 jobs be added in October 2026?"
  current_price: 0.48
  volume_24h_usd: 576.97
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder puts 58% above 60K and 48% above 70K, pinning the market's central estimate in the 60K-70K range for October payrolls."
  - "The economist consensus of roughly 59K is consistent with the ladder's modal range, leaving the market neither materially optimistic nor pessimistic relative to the street."
  - "The 89% above zero confirms near-zero risk of an outright job loss print, but the 29% above 100K shows meaningful upside tail risk remains."
  - "Resolves via the Bureau of Labor Statistics Employment Situation report; hurricane or strike-related distortions to October data are a known settlement edge case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Treasury yields were little changed Thursday as traders positioned ahead of Friday's October jobs report, with economists forecasting roughly 59,000 jobs added."
    publisher: "Sean Conlon, Chloe Taylor"
    published_at: "2026-11-05T09:38:43.000Z"
    source_url: "https://www.cnbc.com/2026/11/05/treasury-yields-bonds-interest-rates.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Sean Conlon, Chloe Taylor"
        source_url: "https://www.cnbc.com/2026/11/05/treasury-yields-bonds-interest-rates.html"
        retrieved_at: "2026-11-05T16:02:36+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder provided; distribution spans a wide range, reflecting genuine uncertainty ahead of the release."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Sean Conlon, Chloe Taylor: Treasury yields: traders look ahead to jobs data"
    url: "https://www.cnbc.com/2026/11/05/treasury-yields-bonds-interest-rates.html"
    published_at: "2026-11-05T09:38:43.000Z"
    retrieved_at: "2026-11-05T16:02:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
