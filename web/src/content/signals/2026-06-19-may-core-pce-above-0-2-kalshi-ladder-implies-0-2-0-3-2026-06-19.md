---
signal_id: "CMSIG2026061904"
signal_slug: "may-core-pce-above-0-2-kalshi-ladder-implies-0-2-0-3-2026-06-19"
headline: "May core PCE above 0.2%: Kalshi ladder implies 0.2-0.3%"
semantic_title: "May core PCE above zero nears full pricing in the distribution"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-06-19T02:31:00.000Z"
event_id: "CM-EVT-PG9RLBJ7F1"
event_slug: "kxpcecore-26may"
event_question: "May 2026 core PCE monthly rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPCECORE-26MAY-T0.3"
  question_raw: "Will the rate of core PCE inflation be above 0.3% in May 2026?"
  current_price: 0.48
  volume_24h_usd: 46.28
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Economic Analysis"
  resolves_at: "2026-06-25T14:00:00Z"
bullets:
  - "Kalshi's ladder centers May core PCE in the 0.2-0.3% range: 89% above 0.2% but only 48% above 0.3%, with 99% above zero."
  - "The retail sales beat adds upside pressure on the 0.3% strike, which sits at near coin-flip odds, consistent with a market that had already anticipated firm consumption."
  - "A print above 0.3% would reinforce the hawkish Warsh FOMC narrative and lift the probability of the Fed funds hike scenario priced at 40% on Polymarket."
  - "Resolves via the Bureau of Economic Analysis PCE release for May 2026; core PCE month-over-month is the settlement metric."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May retail sales rose 0.9%, beating forecasts, complicating the Fed's rate path and raising near-term inflation expectations."
    publisher: "marketdaily.com"
    published_at: "2026-06-19T02:31:00.000Z"
    source_url: "https://marketdaily.com/may-retail-sales-2026-fed-rate-path/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "marketdaily.com"
        source_url: "https://marketdaily.com/may-retail-sales-2026-fed-rate-path/"
        retrieved_at: "2026-06-20T10:30:38+00:00"
  - type: "pm_response"
    notes: "Kalshi's distribution was positioned for firm inflation before the retail beat; the news is consistent with the existing pricing rather than a surprise."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "marketdaily.com: May Retail Sales Climb 0.9%, Beating Forecasts and Complicating Fed Ra"
    url: "https://marketdaily.com/may-retail-sales-2026-fed-rate-path/"
    published_at: "2026-06-19T02:31:00.000Z"
    retrieved_at: "2026-06-20T10:30:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
