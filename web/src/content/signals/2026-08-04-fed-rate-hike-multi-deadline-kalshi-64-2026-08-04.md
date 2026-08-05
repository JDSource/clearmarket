---
signal_id: "CMSIG2026080404"
signal_slug: "fed-rate-hike-multi-deadline-kalshi-64-2026-08-04"
headline: "Fed rate hike (multi-deadline): Kalshi 64%"
semantic_title: "Fed rate hike odds hold above 50% despite mixed labor data"
telemetry: "Kalshi 64%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-04T00:00:00.000Z"
event_id: "CM-EVT-P1KKDFWZ42"
event_slug: "fedhike"
event_question: "Will the Federal Reserve raise interest rates? (multi-deadline series, 2026-2028)"
primary_market:
  platform: "kalshi"
  platform_market_id: "FEDHIKE-26DEC31"
  question_raw: "Will the Federal Reserve hike rates by December 31, 2026?"
  current_price: 0.64
  volume_24h_usd: 28706.12
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi multi-deadline series prices a Fed rate hike at 64%, holding above the 50% threshold despite softer job openings data."
  - "Falling job openings are a mild disinflationary signal, but the market is not moving away from a hike majority, resilient hiring and low layoffs offset the headline decline."
  - "The labor market data alone does not resolve the rate question; the pricing reflects a balance of sticky inflation (ISM prices elevated) against modest labor softening."
  - "Resolution is via the Federal Reserve's actual policy decision; the multi-deadline structure means the contract covers any hike through 2028, giving it a longer runway than a single-meeting market."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US job openings dropped to 7.4 million in June, led by the largest healthcare vacancy decline in 11 months, while the broader labor market remained resilient."
    publisher: "Thomson Reuters"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://wimz.com/2026/08/04/declining-imports-compress-us-trade-deficit-in-june/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://wimz.com/2026/08/04/declining-imports-compress-us-trade-deficit-in-june/"
        retrieved_at: "2026-08-05T10:30:51+00:00"
  - type: "pm_response"
    notes: "Kalshi at 64% covers a multi-year window; Polymarket's single-year 2026 contract (CM-EVT-87QV1G78C4) at 62% suggests the bulk of the hike probability is front-loaded to 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: US job openings fall as healthcare vacancies post largest drop in 11 m"
    url: "https://wimz.com/2026/08/04/declining-imports-compress-us-trade-deficit-in-june/"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-05T10:30:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
