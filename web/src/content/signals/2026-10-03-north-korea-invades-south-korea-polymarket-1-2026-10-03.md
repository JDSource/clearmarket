---
signal_id: "CMSIG2026100307"
signal_slug: "north-korea-invades-south-korea-polymarket-1-2026-10-03"
headline: "North Korea invades South Korea: Polymarket 1%"
semantic_title: "North Korea invading South Korea stays near zero odds"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-03T00:00:00.000Z"
event_id: "CM-EVT-GGMF8V7JH2"
event_slug: "will-north-korea-invade-south-korea-before-2027"
event_question: "Will North Korea invade South Korea before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84dc47b1dd9cd99a9217b92a95690729334b647650bb6bf676bb31c3db0d7f79"
  question_raw: "Will North Korea invade South Korea before 2027?"
  current_price: 0.014
  volume_24h_usd: 5.045872
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only a 1% chance North Korea invades South Korea before 2027."
  - "The missile launch and border mine incidents are escalatory signals, yet the Polymarket contract is consistent with viewing this as provocation, not invasion precursor."
  - "Kim Jong Un remaining Supreme Leader through year-end sits at 96% implied (4% on exit), a stable leadership picture that reduces invasion scenario odds."
  - "Resolution via UMA oracle; a confirmed cross-border military invasion, not a missile test or skirmish, is required."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "North Korea launched a ballistic missile into the Sea of Japan amid renewed border tensions with South Korea following mine blasts."
    publisher: "By: FRANCE 24"
    published_at: "2026-10-03T00:00:00.000Z"
    source_url: "https://www.france24.com/en/asia-pacific/20261003-north-korea-fires-ballistic-missile-after-seoul-s-apology-demand"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "By: FRANCE 24"
        source_url: "https://www.france24.com/en/asia-pacific/20261003-north-korea-fires-ballistic-missile-after-seoul-s-apology-demand"
        retrieved_at: "2026-10-03T12:59:34+00:00"
  - type: "pm_response"
    notes: "Polymarket's 1% on invasion versus 4% on Kim Jong Un exit shows the market is more uncertain about North Korean leadership than about all-out war."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "By: FRANCE 24: North Korea launches ballistic missile as tensions with Seoul grow ove"
    url: "https://www.france24.com/en/asia-pacific/20261003-north-korea-fires-ballistic-missile-after-seoul-s-apology-demand"
    published_at: "2026-10-03T00:00:00.000Z"
    retrieved_at: "2026-10-03T12:59:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
