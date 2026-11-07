---
signal_id: "CMSIG2026110608"
signal_slug: "nov-2026-cpi-monthly-change-seen-near-0-1-to-0-0-kalshi-2026-11-06"
headline: "Nov 2026 CPI monthly change seen near -0.1 to 0.0%: Kalshi"
semantic_title: "November CPI monthly change seen slightly negative on Kalshi"
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
  current_price: 0.22
  volume_24h_usd: 346.66
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-11T14:56:00Z"
bullets:
  - "Kalshi ladder puts 70% odds on November 2026 CPI rising more than -0.1%, and 22% on clearing 0.0%, implying the market-implied center is in the -0.1% to 0.0% range."
  - "The weak CPI distribution sits in tension with Fed hawkishness: Daly and other officials signal more hikes, but the Kalshi CPI ladder does not price an inflationary surge."
  - "The implied flat-to-slightly-negative monthly print, if realized, could complicate the case for a December rate hike despite strong jobs data."
  - "Resolves via the official CPI release from the Bureau of Labor Statistics; the ladder uses a greater-than framing, so each strike is an independent binary."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US Bank's weekly outlook notes October hiring strengthened and layoffs remain unusually low, keeping the Fed's inflation-versus-growth balancing act in focus."
    publisher: "usbank.com"
    published_at: "2026-11-06T00:00:00.000Z"
    source_url: "https://www.usbank.com/corporate-and-commercial-banking/insights/economy/outlook/weekly.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "usbank.com"
        source_url: "https://www.usbank.com/corporate-and-commercial-banking/insights/economy/outlook/weekly.html"
        retrieved_at: "2026-11-07T07:48:17+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder is the sole priced source; no intraday price movement data is available."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "usbank.com: Weekly Economic Outlook | U.S. Bank"
    url: "https://www.usbank.com/corporate-and-commercial-banking/insights/economy/outlook/weekly.html"
    published_at: "2026-11-06T00:00:00.000Z"
    retrieved_at: "2026-11-07T07:48:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
