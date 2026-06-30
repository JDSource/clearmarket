---
signal_id: "CMSIG2026063004"
signal_slug: "june-nfp-implied-100k-125k-kalshi-ladder-64-above-100k-42-ab-2026-06-30"
headline: "June NFP implied 100K-125K: Kalshi ladder 64% above 100K, 42% above 125K"
semantic_title: "June payrolls consensus anchors in 100K-125K implied range"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-06-30T10:00:41.000Z"
event_id: "CM-EVT-NHWMG744L8"
event_slug: "kxpayrolls-26jun"
event_question: "June 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26JUN-T125000"
  question_raw: "Will above 125000 jobs be added in June 2026?"
  current_price: 0.42
  volume_24h_usd: 439.28
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2026-07-02T14:00:00Z"
bullets:
  - "Kalshi ladder implies a June NFP modal range of 100K-125K, pricing 64% above 100K but only 42% above 125K."
  - "Brusuelas's 180K forecast sits well above the market-implied range, meaning the prediction market is pricing a more modest outcome than this analyst expects."
  - "A 180K print would resolve above the 125K ladder rung where the market assigns just 42% probability, implying the market is not fully crediting the bullish forecast."
  - "Resolves via BLS Employment Situation; the June unemployment rate printing at 4.3% (CM-EVT-FJGT56DTV2) is consistent with payrolls in the lower end of the ladder range, not a blowout 180K."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "RSM Chief Economist Joseph Brusuelas forecasts a gain of 180,000 jobs in June, above current consensus, as a preview of the upcoming BLS Employment Situation release."
    publisher: "Joseph Brusuelas"
    published_at: "2026-06-30T10:00:41.000Z"
    source_url: "https://realeconomy.rsmus.com/market-minute-we-expect-a-gain-of-180000-jobs-in-june/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Joseph Brusuelas"
        source_url: "https://realeconomy.rsmus.com/market-minute-we-expect-a-gain-of-180000-jobs-in-june/"
        retrieved_at: "2026-06-30T10:54:27+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via BLS Employment Situation; the gap between the 180K analyst forecast and the 100K-125K implied market range is the key tension in this wire."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Joseph Brusuelas: Market Minute: We expect a gain of 180,000 jobs in June"
    url: "https://realeconomy.rsmus.com/market-minute-we-expect-a-gain-of-180000-jobs-in-june/"
    published_at: "2026-06-30T10:00:41.000Z"
    retrieved_at: "2026-06-30T10:54:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
