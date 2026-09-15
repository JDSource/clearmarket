---
signal_id: "CMSIG2026091403"
signal_slug: "fed-cut-greater-than-25-bps-in-2026-kalshi-4-2026-09-14"
headline: "Fed cut greater than 25 bps in 2026: Kalshi 4%"
semantic_title: "Odds on a large Fed cut this year stay near zero"
telemetry: "Kalshi 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-14T00:00:00.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.037
  volume_24h_usd: 9.04
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices a Fed cut greater than 25 basis points in 2026 at just 4%, resolving via Federal Reserve official decision."
  - "With Warsh widely expected to hike Wednesday, the Kalshi contract is consistent with the news, a large cut this year is a near-complete long shot."
  - "Polymarket's 2026 rate hike contract (CM-EVT-87QV1G78C4) at 93% and this 4% cut contract point in the same direction: the market has fully priced the hike and ruled out a pivot."
  - "Resolution requires Federal Reserve to announce a single cut exceeding 25 bps at any 2026 meeting, a bar that looks very high given Wednesday's expected move."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh is poised to raise rates by 25 basis points even as President Trump continues to demand a cut, according to The Business Times."
    publisher: "Rob Curran"
    published_at: "2026-09-14T00:00:00.000Z"
    source_url: "https://www.businesstimes.com.sg/companies-markets/feds-warsh-poised-pull-trigger-and-raise-rates-first-time-under-his-watch"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rob Curran"
        source_url: "https://www.businesstimes.com.sg/companies-markets/feds-warsh-poised-pull-trigger-and-raise-rates-first-time-under-his-watch"
        retrieved_at: "2026-09-15T13:05:57+00:00"
  - type: "pm_response"
    notes: "Kalshi's cut contract at 4% is the inverse confirmation of the hike consensus, with Federal Reserve announcement as the named resolution source."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rob Curran: Fed's Warsh poised to pull trigger and raise rates for the first time"
    url: "https://www.businesstimes.com.sg/companies-markets/feds-warsh-poised-pull-trigger-and-raise-rates-first-time-under-his-watch"
    published_at: "2026-09-14T00:00:00.000Z"
    retrieved_at: "2026-09-15T13:05:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
