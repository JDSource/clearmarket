---
signal_id: "CMSIG2026110207"
signal_slug: "midterms-happen-on-schedule-kalshi-93-2026-11-02"
headline: "Midterms happen on schedule: Kalshi 93%"
semantic_title: "Midterm elections proceeding on schedule stays near certain"
telemetry: "Kalshi 93%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-02T16:58:00.000Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.93
  volume_24h_usd: 48090.78
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi prices the midterm elections proceeding on schedule at 93%, treating the California ballot dispute as unlikely to derail election day."
  - "The emergency Supreme Court appeal targets 20,000 California ballots; the Kalshi contract implies markets see this as a localized legal skirmish, not a systemic delay."
  - "The Polymarket CA-25 contract (CM-EVT-3DFWF9RX19 at 98%) pricing a November 3 California district winner determination is consistent with election day proceeding normally."
  - "Resolution via The Washington Post's certification of election-day execution; a Supreme Court intervention blocking the election outright would be the edge case invalidating the 93% consensus."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Trump administration asked the Supreme Court to set aside 20,000 disputed California mail ballots the day before the midterm elections."
    publisher: "Patrick Marley"
    published_at: "2026-11-02T16:58:00.000Z"
    source_url: "https://www.washingtonpost.com/politics/2026/11/02/trump-administration-asks-supreme-court-set-aside-20000-california-ballots-now/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Patrick Marley"
        source_url: "https://www.washingtonpost.com/politics/2026/11/02/trump-administration-asks-supreme-court-set-aside-20000-california-ballots-now/"
        retrieved_at: "2026-11-02T17:44:20+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via The Washington Post's confirmation that the 2026 midterm elections occurred on their scheduled date."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Patrick Marley: Trump administration asks Supreme Court to set aside 20,000 California"
    url: "https://www.washingtonpost.com/politics/2026/11/02/trump-administration-asks-supreme-court-set-aside-20000-california-ballots-now/"
    published_at: "2026-11-02T16:58:00.000Z"
    retrieved_at: "2026-11-02T17:44:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
