---
signal_id: "CMSIG2026081203"
signal_slug: "fed-rate-move-june-sept-window-polymarket-35-2026-08-12"
headline: "Fed rate move June-Sept window: Polymarket 35%"
semantic_title: "Fed action between June and September stays below 50% odds"
telemetry: "Polymarket 35%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-12T00:00:00.000Z"
event_id: "CM-EVT-4G3H125S53"
event_slug: "fed-decisions-jun-sep"
event_question: "Will the Federal Reserve make a decision regarding interest rates between June and September?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1b56e46dba9e7b2bf93db18e7a79de3f97037314a46f8ebc93b541ae5f396200"
  question_raw: "Will the Fed decide differently in the next three decisions (Jun–Jul–Sep)?"
  current_price: 0.35
  volume_24h_usd: 5918.769063
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-16T00:00:00Z"
bullets:
  - "Polymarket prices 35% on the Fed making a rate decision between June and September, implying a hold is the majority expectation for that window."
  - "Headline and core CPI rising in line with expectations reduces urgency to act; the market pricing is consistent with the 'Fed on hold' narrative dominating coverage."
  - "Atlanta Fed interim President Cheryl Venable's hawkish commentary on inflation being too high has not pushed this contract above 50%, suggesting the market is not fully endorsing her posture."
  - "Resolves via UMA oracle based on an official Federal Reserve announcement of a rate change within the specified window."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "After soft July CPI came in as expected, analysts and officials increasingly expect the Fed to leave rates unchanged at its next meeting."
    publisher: "koreatimes.co.kr"
    published_at: "2026-08-12T00:00:00.000Z"
    source_url: "https://www.koreatimes.co.kr/world/20260813/fed-expected-to-leave-rates-unchanged-next-month-after-soft-inflation-data"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "koreatimes.co.kr"
        source_url: "https://www.koreatimes.co.kr/world/20260813/fed-expected-to-leave-rates-unchanged-next-month-after-soft-inflation-data"
        retrieved_at: "2026-08-13T09:07:47+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 35% implies the hold camp leads comfortably; volume spike of 9,733% day-over-day on related CM-EVT-VZKJ3PV470 signals sharply rising attention on Fed rate action contracts."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "koreatimes.co.kr: Fed expected to leave rates unchanged next month after soft inflation"
    url: "https://www.koreatimes.co.kr/world/20260813/fed-expected-to-leave-rates-unchanged-next-month-after-soft-inflation-data"
    published_at: "2026-08-12T00:00:00.000Z"
    retrieved_at: "2026-08-13T09:07:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
