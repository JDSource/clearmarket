---
signal_id: "CMSIG2026110602"
signal_slug: "nov-2026-cpi-m-m-kalshi-ladder-centered-near-0-1-to-0-0-2026-11-06"
headline: "Nov 2026 CPI m/m: Kalshi ladder centered near -0.1 to 0.0%"
semantic_title: "November CPI month-over-month stays near flat to slightly negative"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-06T00:00:00.000Z"
event_id: "CM-EVT-T57DHL6V48"
event_slug: "kxcpi-26nov"
event_question: "November 2026 CPI month-over-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26NOV-T0.0"
  question_raw: "Will CPI rise more than 0.0% in November 2026?"
  current_price: 0.34
  volume_24h_usd: 756.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-11T14:56:00Z"
bullets:
  - "Kalshi ladder puts November 2026 CPI month-over-month in the -0.1% to 0.0% range: 70% above -0.1% but only 34% above 0.0%."
  - "The U.S. Bank outlook flags persistent inflation eroding spending power even as the labor market stays resilient, the near-flat CPI pricing suggests markets see inflation cooling modestly on a monthly basis."
  - "Only 10% probability above 0.2% and 7% above 0.3% indicates very little expectation of a renewed monthly surge in consumer prices."
  - "The Fed funds ladder (see wire above) prices one more hike, if November CPI prints flat or negative, that could be the last catalyst needed to pause."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The U.S. Bank weekly outlook notes hiring strengthened in October while layoffs remain unusually low, keeping the economy on a steady but inflation-pressured path."
    publisher: "usbank.com"
    published_at: "2026-11-06T00:00:00.000Z"
    source_url: "https://www.usbank.com/corporate-and-commercial-banking/insights/economy/outlook/weekly.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "usbank.com"
        source_url: "https://www.usbank.com/corporate-and-commercial-banking/insights/economy/outlook/weekly.html"
        retrieved_at: "2026-11-07T14:38:54+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution implies the monthly CPI print for November 2026 is most likely near flat, with the sharp drop in probability above 0.0% reflecting market skepticism about a renewed monthly acceleration."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "usbank.com: Weekly Economic Outlook | U.S. Bank"
    url: "https://www.usbank.com/corporate-and-commercial-banking/insights/economy/outlook/weekly.html"
    published_at: "2026-11-06T00:00:00.000Z"
    retrieved_at: "2026-11-07T14:38:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
