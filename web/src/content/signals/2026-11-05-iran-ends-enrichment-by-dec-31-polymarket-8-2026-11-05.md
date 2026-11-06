---
signal_id: "CMSIG2026110507"
signal_slug: "iran-ends-enrichment-by-dec-31-polymarket-8-2026-11-05"
headline: "Iran ends enrichment by Dec 31: Polymarket 8%"
semantic_title: "Iran agrees to end uranium enrichment by year-end stays a long shot"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-05T19:23:16.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end enrichment of uranium by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.076
  volume_24h_usd: 2173.11275
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 8% on Iran agreeing to end uranium enrichment by December 31, 2026, a long-shot outcome."
  - "Active Gulf diplomacy and Iranian outreach to neighbors are consistent with de-escalation signaling, but the market assigns very low probability to a binding enrichment halt by year-end."
  - "Kalshi prices 2% on the US reopening its embassy in Iran (CM-EVT-34SYT4T2T1), consistent with the Polymarket enrichment contract in framing any near-term normalization as remote."
  - "Polymarket resolves via UMA oracle; the enrichment-halt question likely requires a formal documented Iranian commitment, not a unilateral pause or ceasefire."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's top diplomat held calls with Persian Gulf leaders amid fears of a renewed US military strike, with regional diplomacy intensifying."
    publisher: "Matthew Hoare"
    published_at: "2026-11-05T19:23:16.000Z"
    source_url: "https://www.newarab.com/news/flurry-regional-diplomacy-amid-fears-us-attack"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Matthew Hoare"
        source_url: "https://www.newarab.com/news/flurry-regional-diplomacy-amid-fears-us-attack"
        retrieved_at: "2026-11-06T07:48:14+00:00"
  - type: "pm_response"
    notes: "Polymarket at 8% via UMA oracle; companion Kalshi embassy contract at 2% confirms markets see near-term US-Iran normalization as highly unlikely."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Matthew Hoare: Flurry of regional diplomacy amid fears of US attack"
    url: "https://www.newarab.com/news/flurry-regional-diplomacy-amid-fears-us-attack"
    published_at: "2026-11-05T19:23:16.000Z"
    retrieved_at: "2026-11-06T07:48:14+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
