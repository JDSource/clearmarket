---
signal_id: "CMSIG2026112003"
signal_slug: "nov-cpi-above-0-1-m-m-kalshi-ladder-36-2026-11-20"
headline: "Nov CPI above -0.1% m/m: Kalshi ladder 36%"
semantic_title: "November CPI month-over-month stays in deflationary range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-20T00:00:00.000Z"
event_id: "CM-EVT-T57DHL6V48"
event_slug: "kxcpi-26nov"
event_question: "November 2026 CPI month-over-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26NOV-T-0.1"
  question_raw: "Will CPI rise more than -0.1% in November 2026?"
  current_price: 0.36
  volume_24h_usd: 619.2
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-11T14:56:00Z"
bullets:
  - "Kalshi ladder implies November CPI is most likely below -0.1% month-over-month, with only 36% pricing a print at or above -0.1%."
  - "The distribution, 36% at -0.1%, 14% at 0.0%, rapidly tailing off above, reflects expectations for outright monthly price deflation."
  - "A negative monthly print would reinforce the 'cooler inflation' narrative while still leaving the year-over-year rate well above the Fed's 2% target."
  - "Resolves via the Bureau of Labor Statistics CPI release; the sharp drop above 0.0% (14%) to 0.1% (3%) signals near-zero chance of any meaningful positive print."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "U.S. Bank's weekly outlook flagged the Fed's difficult balance as spending data remained firm while tightening continued."
    publisher: "usbank.com"
    published_at: "2026-11-20T00:00:00.000Z"
    source_url: "https://www.usbank.com/corporate-and-commercial-banking/insights/economy/outlook/weekly.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "usbank.com"
        source_url: "https://www.usbank.com/corporate-and-commercial-banking/insights/economy/outlook/weekly.html"
        retrieved_at: "2026-11-22T07:47:40+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; distribution strongly skewed toward sub-zero monthly CPI, consistent with recent cooler PPI/CPI trend."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "usbank.com: Weekly Economic Outlook | U.S. Bank"
    url: "https://www.usbank.com/corporate-and-commercial-banking/insights/economy/outlook/weekly.html"
    published_at: "2026-11-20T00:00:00.000Z"
    retrieved_at: "2026-11-22T07:47:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
