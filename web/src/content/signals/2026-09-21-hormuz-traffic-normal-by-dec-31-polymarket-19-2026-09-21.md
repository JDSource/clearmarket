---
signal_id: "CMSIG2026092103"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-19-2026-09-21"
headline: "Hormuz traffic normal by Dec 31: Polymarket 19%"
semantic_title: "Strait of Hormuz back to normal by year-end stays long odds"
telemetry: "Polymarket 19%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-21T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.19
  volume_24h_usd: 118825.292209
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 19% on Strait of Hormuz traffic returning to normal by December 31, 2026, reflecting deep skepticism about a near-term resolution."
  - "Iran's explicit refusal to reopen the strait and its multi-condition demand list are consistent with the market's heavy lean against normalization this year."
  - "A Kalshi contract on the US reopening its embassy in Iran sits at just 4%, suggesting markets see diplomatic normalization as nearly off the table entirely."
  - "Resolution tracks whether Hormuz transit levels return to baseline as measured by the UMA oracle; Iran's stated conditions make near-term resolution structurally difficult."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran refused to reopen the Strait of Hormuz, setting seven conditions for resuming US talks including ending a naval blockade and releasing frozen funds."
    publisher: "zeenews.india.com"
    published_at: "2026-09-21T00:00:00.000Z"
    source_url: "https://zeenews.india.com/world/painful-attacks-without-consideration-as-trump-weighs-next-move-iran-threatens-us-bases-across-west-asia-3072531.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "zeenews.india.com"
        source_url: "https://zeenews.india.com/world/painful-attacks-without-consideration-as-trump-weighs-next-move-iran-threatens-us-bases-across-west-asia-3072531.html"
        retrieved_at: "2026-09-21T07:47:18+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 19% price aligns with the market treating Iran's conditions as a high bar unlikely to be cleared before year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "zeenews.india.com: ‘Painful attacks without consideration’: As Trump weighs next move, Ir"
    url: "https://zeenews.india.com/world/painful-attacks-without-consideration-as-trump-weighs-next-move-iran-threatens-us-bases-across-west-asia-3072531.html"
    published_at: "2026-09-21T00:00:00.000Z"
    retrieved_at: "2026-09-21T07:47:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
