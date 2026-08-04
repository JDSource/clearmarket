---
signal_id: "CMSIG2026080304"
signal_slug: "july-nonfarm-payrolls-kalshi-ladder-implies-90k-100k-2026-08-03"
headline: "July nonfarm payrolls: Kalshi ladder implies ~90K-100K"
semantic_title: "July jobs report odds sit near 50-50 at 90,000-100,000 range"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-08-03T10:32:12.393Z"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "Nonfarm payrolls added (September 2026 reference month)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T100000"
  question_raw: "Will above 100000 jobs be added in September 2026?"
  current_price: 0.49
  volume_24h_usd: 1.96
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Kalshi ladder implies roughly 90,000-100,000 jobs added, with 51% above 90K and 49% above 100K, a near-coin-flip at that boundary."
  - "The jobs report is the key near-term catalyst; the market is straddling the 90K-100K line with no strong directional lean."
  - "The 30-40% range above 125K suggests the market is assigning limited probability to an upside surprise that would sharpen Fed hike expectations."
  - "Resolution: Bureau of Labor Statistics official nonfarm payrolls release settles each strike on this Kalshi ladder."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Wall Street is bracing for Friday's July jobs report as a key directional signal for equities and Fed policy."
    publisher: "Investing.com"
    published_at: "2026-08-03T10:32:12.393Z"
    source_url: "https://www.investing.com/news/economy-news/teetering-us-stock-market-faces-jobs-report-big-earnings-week-4829696"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Investing.com"
        source_url: "https://www.investing.com/news/economy-news/teetering-us-stock-market-faces-jobs-report-big-earnings-week-4829696"
        retrieved_at: "2026-08-04T10:33:12+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows maximum uncertainty near the 90K-100K payroll boundary ahead of the report."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Investing.com: Teetering US stock market faces jobs report, big earnings week By Reut"
    url: "https://www.investing.com/news/economy-news/teetering-us-stock-market-faces-jobs-report-big-earnings-week-4829696"
    published_at: "2026-08-03T10:32:12.393Z"
    retrieved_at: "2026-08-04T10:33:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
