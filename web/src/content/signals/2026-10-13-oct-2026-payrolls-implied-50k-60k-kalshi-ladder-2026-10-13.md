---
signal_id: "CMSIG2026101301"
signal_slug: "oct-2026-payrolls-implied-50k-60k-kalshi-ladder-2026-10-13"
headline: "Oct 2026 payrolls implied 50K-60K: Kalshi ladder"
semantic_title: "October payrolls seen well below 100K after September miss"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-13T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls added"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T60000"
  question_raw: "Will above 60000 jobs be added in October 2026?"
  current_price: 0.43
  volume_24h_usd: 3.56
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder puts the October 2026 payroll print in the 50K-60K implied range, with 69% pricing above 30K but only 27% above 100K."
  - "September's 29K print, well below the prior 12-month average of 45K, is consistent with the ladder's skew toward a weak-but-positive October outcome."
  - "Trading volume on this ladder surged 531x day over day, a strong signal the September miss is drawing heavy fresh attention to October's number."
  - "The Kalshi contract resolves on the official Bureau of Labor Statistics nonfarm payrolls release for October 2026; any benchmark revision could shift the implied range."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The U.S. economy added only 29,000 jobs in September, far below expectations, raising fears of a sustained labor market slowdown heading into October."
    publisher: "cnnbc.com"
    published_at: "2026-10-13T00:00:00.000Z"
    source_url: "https://cnnbc.com/u-s-economy-adds-just-29-000-jobs-in-september-as-labor-market-cools"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cnnbc.com"
        source_url: "https://cnnbc.com/u-s-economy-adds-just-29-000-jobs-in-september-as-labor-market-cools"
        retrieved_at: "2026-10-13T07:48:09+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on October 2026 payrolls saw a 531x volume surge after the weak September report, with market-implied central estimate near 50K-60K."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cnnbc.com: U.S. Economy Adds Just 29,000 Jobs in September as Labor Market Cools"
    url: "https://cnnbc.com/u-s-economy-adds-just-29-000-jobs-in-september-as-labor-market-cools"
    published_at: "2026-10-13T00:00:00.000Z"
    retrieved_at: "2026-10-13T07:48:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
