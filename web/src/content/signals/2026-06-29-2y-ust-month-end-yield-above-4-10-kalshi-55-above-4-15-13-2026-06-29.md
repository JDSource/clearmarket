---
signal_id: "CMSIG2026062907"
signal_slug: "2y-ust-month-end-yield-above-4-10-kalshi-55-above-4-15-13-2026-06-29"
headline: "2Y UST month-end yield above 4.10%: Kalshi 55%, above 4.15% 13%"
semantic_title: "2Y Treasury month-end yield consensus anchors at 4.10-4.15 percent"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-06-29T08:27:25.000Z"
event_id: "CM-EVT-159R5BWD80"
event_slug: "kxustm-26jun30"
event_question: "2Y US Treasury month-end yield"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXUSTM-26JUN30-T4.15"
  question_raw: "Will 2Y US Treasury Yield for month-end be above 4.15%?"
  current_price: 0.13
  volume_24h_usd: 0.91
  arbitration_model: "kalshi_staff"
  resolution_source: "US Department of the Treasury"
  resolves_at: "2026-07-07T21:00:00Z"
bullets:
  - "Kalshi ladder prices 55% above 4.10% and only 13% above 4.15% for month-end 2Y Treasury yield, implying a modal range of 4.10-4.15%."
  - "A firm dollar into the jobs week is consistent with rates markets pricing the 2Y yield near current levels rather than moving sharply in either direction."
  - "The June Fed funds upper bound ladder (CM-EVT-PHWX2H6DM5) at 98% above 3.50% but only 18% above 3.75% anchors the short-rate context for the 2Y yield range."
  - "Resolves at month-end close today, June 30; the NFP print due imminently is the primary catalyst that could shift the 2Y yield toward or away from the 4.15% tail."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The dollar held firm ahead of a week featuring the June jobs report and other key US data, with currency markets on alert for potential volatility."
    publisher: "corpaycurrencyresearch.com"
    published_at: "2026-06-29T08:27:25.000Z"
    source_url: "https://corpaycurrencyresearch.com/dollar-holds-firm-ahead-of-potentially-dangerous-week/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "corpaycurrencyresearch.com"
        source_url: "https://corpaycurrencyresearch.com/dollar-holds-firm-ahead-of-potentially-dangerous-week/"
        retrieved_at: "2026-06-30T10:54:27+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves at month-end; with NFP data landing today, the 55%/13% split at 4.10%/4.15% reflects genuine two-sided risk around the jobs print."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "corpaycurrencyresearch.com: Dollar holds firm ahead of potentially-dangerous week, Corpay Currenc"
    url: "https://corpaycurrencyresearch.com/dollar-holds-firm-ahead-of-potentially-dangerous-week/"
    published_at: "2026-06-29T08:27:25.000Z"
    retrieved_at: "2026-06-30T10:54:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
