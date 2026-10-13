---
signal_id: "CMSIG2026101308"
signal_slug: "trump-removes-powell-as-fed-chair-kalshi-9-2026-10-13"
headline: "Trump removes Powell as Fed Chair: Kalshi 9%"
semantic_title: "Odds on Trump removing Fed Chair Powell remain low at 9 percent"
telemetry: "Kalshi 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-13T00:00:00.000Z"
event_id: "CM-EVT-TMHG8WLK69"
event_slug: "kxtryfirepowell-26may12"
event_question: "Will Trump attempt to remove Powell as Federal Reserve Chair or Governor?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRYFIREPOWELL-26MAY12-GOV2"
  question_raw: "Will the President try to fire the Jerome Powell as either Chair of the Board of Governors of the Federal Reserve System or Member of the Board of Governors of the Federal Reserve System before Jan 1, 2027?"
  current_price: 0.087
  volume_24h_usd: 6.35
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices a Trump attempt to remove Federal Reserve Chair Jerome Powell at 9%, with trading volume up 118x day over day."
  - "The Fed minutes showing internal divisions on inflation arrive alongside news that Kevin Warsh has already taken over as Fed Chair, making the specific Powell-removal question largely moot going forward."
  - "The 118x volume spike suggests traders are actively reassessing the contract's resolution mechanics now that Warsh leads the Fed."
  - "Resolves via ABC News reporting; if Powell has already been replaced by Warsh, the resolution definition of an 'attempt to remove' Powell becomes the critical interpretive question."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Federal Reserve minutes revealed sharp internal divisions over the inflation outlook, with energy shocks and AI infrastructure spending cited as key upside risks, amid the backdrop of new Fed Chairman Kevin Warsh's first policy meeting."
    publisher: "cnnbc.com"
    published_at: "2026-10-13T00:00:00.000Z"
    source_url: "https://cnnbc.com/federal-reserve-minutes-reveal-sharp-divisions-over-inflation-outlook"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cnnbc.com"
        source_url: "https://cnnbc.com/federal-reserve-minutes-reveal-sharp-divisions-over-inflation-outlook"
        retrieved_at: "2026-10-13T07:48:09+00:00"
  - type: "pm_response"
    notes: "Kalshi's Trump-removes-Powell contract spiked 118x in volume after the Warsh chairmanship confirmation, with the 9% price reflecting residual uncertainty around resolution mechanics."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cnnbc.com: Federal Reserve Minutes Reveal Sharp Divisions Over Inflation Outlook"
    url: "https://cnnbc.com/federal-reserve-minutes-reveal-sharp-divisions-over-inflation-outlook"
    published_at: "2026-10-13T00:00:00.000Z"
    retrieved_at: "2026-10-13T07:48:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
