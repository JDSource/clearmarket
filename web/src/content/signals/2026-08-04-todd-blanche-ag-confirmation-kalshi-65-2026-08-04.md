---
signal_id: "CMSIG2026080407"
signal_slug: "todd-blanche-ag-confirmation-kalshi-65-2026-08-04"
headline: "Todd Blanche AG confirmation: Kalshi 65%"
semantic_title: "Todd Blanche Senate confirmation stays near 65%"
telemetry: "Kalshi 65%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-04T00:00:00.000Z"
event_id: "CM-EVT-NY76DC3G68"
event_slug: "kxagconf-26"
event_question: "Will Todd Blanche be confirmed?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAGCONF-26JUN05-SEP01"
  question_raw: "Will Trump's first announced Attorney General pick be confirmed as Attorney General before Sep 1, 2026?"
  current_price: 0.65
  volume_24h_usd: 13119.07
  arbitration_model: "kalshi_staff"
  resolution_source: "U.S. Senate"
  resolves_at: "2026-09-08T14:00:00Z"
bullets:
  - "The Kalshi contract on Todd Blanche being confirmed as Attorney General is priced at 65%, reflecting a favored but uncertain outcome."
  - "Committee advancement is the key threshold news, but the 'hanging by a thread' framing in CNN's reporting is consistent with the 35% probability of failure still priced in."
  - "A companion Kalshi ladder (CM-EVT-GMWVVJJ4S2) implies a final vote count in the 49-50 range, with only 47% above 50 votes, underscoring how tight the floor count appears."
  - "Resolves via U.S. Senate vote; the ladder's implied margin of 49-50 votes explains why the confirmation contract has not moved to the high 70s or above despite committee passage."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Acting Attorney General Todd Blanche advanced out of the Senate Judiciary Committee, though his nomination was described as hanging by a thread."
    publisher: "Hannah Rabinowitz"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/08/04/politics/todd-blanches-confirmation-expected-revitalize-doj-investigations"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Hannah Rabinowitz"
        source_url: "https://www.cnn.com/2026/08/04/politics/todd-blanches-confirmation-expected-revitalize-doj-investigations"
        retrieved_at: "2026-08-07T08:53:43+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 65% resolves via U.S. Senate confirmation vote; companion vote-count ladder reinforces thin-majority scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Hannah Rabinowitz: Todd Blanche advances toward confirmation, paving way for reenergized"
    url: "https://www.cnn.com/2026/08/04/politics/todd-blanches-confirmation-expected-revitalize-doj-investigations"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-07T08:53:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
