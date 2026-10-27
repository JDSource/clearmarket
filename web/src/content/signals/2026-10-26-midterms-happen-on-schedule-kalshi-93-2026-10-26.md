---
signal_id: "CMSIG2026102606"
signal_slug: "midterms-happen-on-schedule-kalshi-93-2026-10-26"
headline: "Midterms happen on schedule: Kalshi 93%"
semantic_title: "Midterm elections on schedule stays firmly priced near certainty"
telemetry: "Kalshi 93%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-26T22:00:00.000Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.93
  volume_24h_usd: 19674.81
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi prices the midterm elections proceeding on schedule at 93%, treating legal challenges like the California ballot dispute as unlikely to derail the November 3 date."
  - "The DOJ ballot challenge being rejected by an appeals court is consistent with the market's near-certainty; legal friction is not moving the probability toward disruption."
  - "A companion Polymarket contract on the California 25th District winner (CM-EVT-3DFWF9RX19) sits at 94%, showing district-level markets also pricing normal resolution timelines."
  - "Resolves via The Washington Post; Kalshi will look for independent reporting confirming elections occurred as scheduled on November 3."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "An appeals court rejected the Trump DOJ's demand to set aside 20,000 California mail ballots, adding to election-integrity friction ahead of November 3."
    publisher: "Jeremy Herb, Tierney Sneed"
    published_at: "2026-10-26T22:00:00.000Z"
    source_url: "https://www.cnn.com/2026/10/26/politics/california-mail-ballot-noncitizen-appeals-court-rejects"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeremy Herb, Tierney Sneed"
        source_url: "https://www.cnn.com/2026/10/26/politics/california-mail-ballot-noncitizen-appeals-court-rejects"
        retrieved_at: "2026-10-27T07:48:12+00:00"
  - type: "pm_response"
    notes: "Kalshi's 93% on-schedule probability absorbs the California mail-ballot court fight without repricing, indicating the market treats it as a local dispute rather than a systemic threat."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeremy Herb, Tierney Sneed: Appeals court rejects Trump DOJ demand to set aside 20,000 California"
    url: "https://www.cnn.com/2026/10/26/politics/california-mail-ballot-noncitizen-appeals-court-rejects"
    published_at: "2026-10-26T22:00:00.000Z"
    retrieved_at: "2026-10-27T07:48:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
