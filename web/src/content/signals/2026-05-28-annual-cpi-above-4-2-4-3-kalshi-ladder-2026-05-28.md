---
signal_id: "CMSIG2026052802"
signal_slug: "annual-cpi-above-4-2-4-3-kalshi-ladder-2026-05-28"
headline: "Annual CPI above 4.2-4.3%: Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-05-28T16:29:22.000Z"
event_id: "CM-EVT-5F0G9L6HV6"
event_slug: "kxcpiyoy-26may"
event_question: "Annual CPI rate ending May 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26MAY-T4.3"
  question_raw: "Will the rate of CPI inflation be above 4.3% for the year ending in May 2026?"
  current_price: 0.19
  volume_24h_usd: 1828.02
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-06-10T14:00:00Z"
bullets:
  - "The Kalshi annual CPI ladder implies a market-consensus range of 4.2-4.3% for the year ending in May 2026, with 91% probability above 4.1% collapsing sharply to 60% above 4.2% and only 19% above 4.3%, marking the distribution's inflection point."
  - "April's headline inflation print -- described across multiple reports as the highest in three years, with gasoline and food costs as primary drivers -- is consistent with the ladder's center of mass sitting well above 4%, though the market assigns only modest odds to readings above 4.3%."
  - "The sharp probability cliff between 4.2% (60%) and 4.3% (19%) signals the market sees the most likely outcome as a reading in the low 4.2% range, with tail risk fading quickly above that level."
  - "A companion Kalshi ladder (CM-EVT-CF4GQ5PDX0) for May core CPI monthly change shows 86% above 0.1% but only 45% above 0.2%, implying the market expects a modest monthly core print -- consistent with annual readings plateauing rather than accelerating sharply."
  - "The Kalshi annual CPI contract resolves via Bureau of Labor Statistics CPI release for the relevant 12-month period; revisions to prior months' data could affect final resolution if BLS issues corrections before the settlement window closes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Core inflation hit 3.3% and the Fed's preferred gauge rose to 3.8% in April, the highest in three years, as the Iran war drove up energy and food costs."
    publisher: "financialexpress.com"
    published_at: "2026-05-28T16:29:22.000Z"
    source_url: "https://www.financialexpress.com/market/global-markets/iran-conflict-adds-pressure-on-us-economy-as-core-inflation-hits-3-3-and-jobless-claims-climb/4253725/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "financialexpress.com"
        source_url: "https://www.financialexpress.com/market/global-markets/iran-conflict-adds-pressure-on-us-economy-as-core-inflation-hits-3-3-and-jobless-claims-climb/4253725/"
        retrieved_at: "2026-05-29T21:01:04+00:00"
  - type: "pm_response"
    notes: "Kalshi's annual ladder and the separate monthly core CPI ladder together paint a consistent picture: elevated annual inflation anchored near 4.2%, with monthly momentum seen as moderate."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "financialexpress.com: Iran war adds pressure on US economy as core inflation hits 3.3% and j"
    url: "https://www.financialexpress.com/market/global-markets/iran-conflict-adds-pressure-on-us-economy-as-core-inflation-hits-3-3-and-jobless-claims-climb/4253725/"
    published_at: "2026-05-28T16:29:22.000Z"
    retrieved_at: "2026-05-29T21:01:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
