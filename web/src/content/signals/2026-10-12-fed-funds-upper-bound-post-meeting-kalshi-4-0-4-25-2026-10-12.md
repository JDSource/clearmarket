---
signal_id: "CMSIG2026101203"
signal_slug: "fed-funds-upper-bound-post-meeting-kalshi-4-0-4-25-2026-10-12"
headline: "Fed funds upper bound post-meeting: Kalshi 4.0-4.25%"
semantic_title: "Fed funds upper bound seen near 4 percent after next meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-12T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound after next FOMC meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.15
  volume_24h_usd: 1.65
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound in the 4.00-4.25% range: 83% above 4.00%, but only 15% above 4.25%."
  - "FOMC minutes signaled a hike lean, yet the market clusters near 4.00-4.25% rather than pricing a move well above 4.25%, suggesting the market is not fully buying the hawkish posture."
  - "A softer September jobs report, just 29,000 payrolls added versus 90,000 expected, is pulling against the hawkish minutes, keeping the implied endpoint near current levels."
  - "A companion Kalshi ladder (CM-EVT-6BS28TS762) pins an earlier meeting outcome below 4.00% with 99% confidence, consistent with a sequential hike path rather than a jump."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "FOMC minutes reaffirmed a rate hike bias while strong foreign demand at a 10-year Treasury auction pushed yields down 10 basis points ahead of CPI data."
    publisher: "chase-dream.cn"
    published_at: "2026-10-12T00:00:00.000Z"
    source_url: "https://chase-dream.cn/en/digests/fed_macro-20261012-am/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "chase-dream.cn"
        source_url: "https://chase-dream.cn/en/digests/fed_macro-20261012-am/"
        retrieved_at: "2026-10-12T17:17:25+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on the Fed funds upper bound; the 83%/15% split at 4.00%/4.25% shows the market treating a move past 4.25% as a tail risk despite hawkish Fed minutes."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "chase-dream.cn: Fed & Macro Overnight Brief October 12, 2026 | Fed Minutes Re-Affirm a"
    url: "https://chase-dream.cn/en/digests/fed_macro-20261012-am/"
    published_at: "2026-10-12T00:00:00.000Z"
    retrieved_at: "2026-10-12T17:17:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
