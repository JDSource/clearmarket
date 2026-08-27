---
signal_id: "CMSIG2026082603"
signal_slug: "democrats-win-u-s-house-in-2026-kalshi-84-2026-08-26"
headline: "Democrats win U.S. House in 2026: Kalshi 84%"
semantic_title: "Democrats favored to retake the House, odds stay high"
telemetry: "Kalshi 84%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-26T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.84
  volume_24h_usd: 53153.36
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi puts 84% odds on Democrats winning the U.S. House in the 2026 midterms, resolves via Library of Congress."
  - "Intra-party Republican anger over new tariffs, combined with voters ranking affordability as the top concern, is consistent with the strong Democratic pricing."
  - "Separately, the Kalshi 'blue tsunami' contract (CM-EVT-6CY3Y4C610) sits at only 39%, suggesting markets see a Democratic House win as likely but not a sweep scenario."
  - "Resolves via Library of Congress certification of House majority composition after November 2026 elections."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Republican lawmakers are openly furious that Trump has revived tariff drama just months before the 2026 midterm elections, amid voter concerns about affordability."
    publisher: "Adam Cancryn"
    published_at: "2026-08-26T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/08/26/politics/republicans-trump-tariffs-midterms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Adam Cancryn"
        source_url: "https://www.cnn.com/2026/08/26/politics/republicans-trump-tariffs-midterms"
        retrieved_at: "2026-08-27T18:46:25+00:00"
  - type: "pm_response"
    notes: "Kalshi at 84% shows strong conviction for a Democratic House flip, well above the 'blue tsunami' threshold that markets assign only 39%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Adam Cancryn: Republicans furious with Trump over more tariffs ahead of the midterms"
    url: "https://www.cnn.com/2026/08/26/politics/republicans-trump-tariffs-midterms"
    published_at: "2026-08-26T00:00:00.000Z"
    retrieved_at: "2026-08-27T18:46:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
