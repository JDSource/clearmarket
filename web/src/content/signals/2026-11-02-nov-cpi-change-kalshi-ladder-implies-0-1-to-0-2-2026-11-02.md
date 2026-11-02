---
signal_id: "CMSIG2026110204"
signal_slug: "nov-cpi-change-kalshi-ladder-implies-0-1-to-0-2-2026-11-02"
headline: "Nov CPI change: Kalshi ladder implies +0.1% to +0.2%"
semantic_title: "November CPI consensus leans mildly positive, below 0.2 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-02T00:00:00.000Z"
event_id: "CM-EVT-T57DHL6V48"
event_slug: "kxcpi-26nov"
event_question: "November 2026 CPI month-over-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26NOV-T0.2"
  question_raw: "Will CPI rise more than 0.2% in November 2026?"
  current_price: 0.48
  volume_24h_usd: 26.84
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-11T14:56:00Z"
bullets:
  - "Kalshi ladder prices November 2026 CPI in the +0.1% to +0.2% range: 63% above 0.1%, 48% above 0.2%, dropping to 22% above 0.3%."
  - "September PCE reacceleration to 3.6% is a hawkish backdrop, but the Kalshi distribution for November CPI does not price an outsized spike, suggesting the market is not yet pricing a second-order PCE-to-CPI spillover."
  - "The 84% probability above 0.0% means deflation or flat CPI is largely ruled out; only a modest positive print is the consensus expectation."
  - "The core CPI annual rate ladder (event CM-EVT-BXDL61HVR9 from story 6) puts 60% on year-over-year core CPI above 2.8%, offering a longer-horizon complement that confirms persistent above-target pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "PCE inflation accelerated to 3.6% in September from 3.4% in August, underscoring persistent price pressures in the US economy ahead of the midterms."
    publisher: "International Finance Business Desk"
    published_at: "2026-11-02T00:00:00.000Z"
    source_url: "https://internationalfinance.com/macroeconomy/midterms-2026-us-gdp-grows-3-4-but-inflation-keeps-pressure-on-economy/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "International Finance Business Desk"
        source_url: "https://internationalfinance.com/macroeconomy/midterms-2026-us-gdp-grows-3-4-but-inflation-keeps-pressure-on-economy/"
        retrieved_at: "2026-11-02T07:48:26+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder covers the November 2026 CPI month-over-month distribution; the market-implied range of 0.1-0.2% is a modest positive reading despite a hot PCE backdrop."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "International Finance Business Desk: Midterms 2026: US GDP grows 3.4%, but inflation keeps pressure on econ"
    url: "https://internationalfinance.com/macroeconomy/midterms-2026-us-gdp-grows-3-4-but-inflation-keeps-pressure-on-economy/"
    published_at: "2026-11-02T00:00:00.000Z"
    retrieved_at: "2026-11-02T07:48:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
