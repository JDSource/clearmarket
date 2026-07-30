---
signal_id: "CMSIG2026073004"
signal_slug: "democrats-win-us-house-in-2026-kalshi-83-2026-07-30"
headline: "Democrats win US House in 2026: Kalshi 83%"
semantic_title: "Democrats firmly favored to win the US House in midterms"
telemetry: "Kalshi 83%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-30T10:00:26.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.83
  volume_24h_usd: 5436.52
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market prices an 83% chance Democrats win the US House in the next election."
  - "An 8-point Democratic generic ballot lead from CNN is broadly consistent with the high Kalshi probability on a House flip."
  - "The Kalshi contract on Republicans holding more governorships than Democrats after the midterms sits at 50%, suggesting a more mixed down-ballot picture."
  - "The Library of Congress is the named resolution source; the contract settles on official certified election results."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A CNN poll shows Democrats leading Republicans by 8 points on the generic congressional ballot less than 100 days before the 2026 midterms."
    publisher: "edition.cnn.com"
    published_at: "2026-07-30T10:00:26.000Z"
    source_url: "https://edition.cnn.com/2026/07/30/politics/cnn-poll-midterm-generic-ballot-democrats-republicans-change"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "edition.cnn.com"
        source_url: "https://edition.cnn.com/2026/07/30/politics/cnn-poll-midterm-generic-ballot-democrats-republicans-change"
        retrieved_at: "2026-07-30T10:20:48+00:00"
  - type: "pm_response"
    notes: "Kalshi resolves via Library of Congress official election records; the 83% price and the poll result are directionally aligned."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "edition.cnn.com: CNN Poll: Voters favor Democrats by an 8-point margin heading into the"
    url: "https://edition.cnn.com/2026/07/30/politics/cnn-poll-midterm-generic-ballot-democrats-republicans-change"
    published_at: "2026-07-30T10:00:26.000Z"
    retrieved_at: "2026-07-30T10:20:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
