---
signal_id: "CMSIG2026102004"
signal_slug: "russia-ukraine-ceasefire-in-2026-polymarket-14-2026-10-20"
headline: "Russia-Ukraine ceasefire in 2026: Polymarket 14%"
semantic_title: "Russia-Ukraine ceasefire in 2026 stays near long-shot odds"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-20T00:00:00.000Z"
event_id: "CM-EVT-2089XJ01Y3"
event_slug: "russia-x-ukraine-ceasefire-by"
event_question: "Will Russia and Ukraine reach a ceasefire in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84c625fdccf5c5246a15e476361e4563033906ee225800e1136c0d737596a72f"
  question_raw: "Russia x Ukraine ceasefire by December 31, 2026?"
  current_price: 0.14
  volume_24h_usd: 169204.192466
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices the Russia-Ukraine ceasefire in 2026 at 14%, reflecting deep skepticism even as diplomatic channels reopen."
  - "Russia's readiness for mid-November talks and Trump pressure are incremental positives, but the market is not pricing a breakthrough, the gap between talk and ceasefire is wide."
  - "A companion Polymarket contract on Ukraine signing a full peace deal before 2027 (CM-EVT-DCQYWYX424) sits at 10%, implying the market sees a formal peace deal as slightly less likely than a ceasefire alone."
  - "Resolves via UMA oracle; a ceasefire requires documented cessation of hostilities, not merely resumed negotiations."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia signaled readiness to resume trilateral talks with the U.S. and Ukraine in mid-November, while the Trump administration repositioned nuclear submarines and pressured Moscow."
    publisher: "link.cfr.org"
    published_at: "2026-10-20T00:00:00.000Z"
    source_url: "https://link.cfr.org/public/40979402"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "link.cfr.org"
        source_url: "https://link.cfr.org/public/40979402"
        retrieved_at: "2026-10-22T07:47:56+00:00"
  - type: "pm_response"
    notes: "Polymarket multi-deadline ceasefire contract at 14%; peace deal contract at 10% reveals a narrow but meaningful spread between partial and full resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "link.cfr.org: Across the Globe"
    url: "https://link.cfr.org/public/40979402"
    published_at: "2026-10-20T00:00:00.000Z"
    retrieved_at: "2026-10-22T07:47:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
