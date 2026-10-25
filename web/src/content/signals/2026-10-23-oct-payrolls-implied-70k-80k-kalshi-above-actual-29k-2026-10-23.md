---
signal_id: "CMSIG2026102301"
signal_slug: "oct-payrolls-implied-70k-80k-kalshi-above-actual-29k-2026-10-23"
headline: "Oct payrolls implied 70K-80K: Kalshi above actual 29K"
semantic_title: "October payrolls market stays well above the weak print"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-10-23T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.45
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder pins October payrolls in the 70K-80K implied range, with 51% above 70K and 45% above 80K."
  - "Actual print of 29K is well below the market-implied midpoint, trading volume surged 172x day-over-day, signaling rapid fresh attention on this claim."
  - "At 29K, the realized number sits near the 0-30K range where Kalshi assigns 15-21% cumulative probability, market was clearly not pricing this outcome."
  - "The Fed funds rate ladder (CM-EVT-MR57HVWJT3) still prices 80% odds the upper bound stays above 4.0%, suggesting weak jobs alone has not fully repriced the rate path."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "October US payrolls came in at just 29,000 jobs added, sharply below expectations, with unemployment ticking higher."
    publisher: "Amelia Northam"
    published_at: "2026-10-23T00:00:00.000Z"
    source_url: "https://quantumnova.tech/news/us-job-growth-slowed-sharply-in-october-as-unemployment-ticked-up-weighing-on-markets-and-fed-outlook"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Amelia Northam"
        source_url: "https://quantumnova.tech/news/us-job-growth-slowed-sharply-in-october-as-unemployment-ticked-up-weighing-on-markets-and-fed-outlook"
        retrieved_at: "2026-10-25T07:48:12+00:00"
  - type: "pm_response"
    notes: "Kalshi contract on October 2026 payrolls saw a 172x day-over-day volume surge, consistent with the surprise miss drawing heavy fresh positioning."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Amelia Northam: Weak October US payrolls (+29,000) and rising unemployment reshape mar"
    url: "https://quantumnova.tech/news/us-job-growth-slowed-sharply-in-october-as-unemployment-ticked-up-weighing-on-markets-and-fed-outlook"
    published_at: "2026-10-23T00:00:00.000Z"
    retrieved_at: "2026-10-25T07:48:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
