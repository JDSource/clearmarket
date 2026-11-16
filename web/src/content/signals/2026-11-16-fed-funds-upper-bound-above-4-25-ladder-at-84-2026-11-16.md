---
signal_id: "CMSIG2026111604"
signal_slug: "fed-funds-upper-bound-above-4-25-ladder-at-84-2026-11-16"
headline: "Fed funds upper bound above 4.25%: ladder at 84%"
semantic_title: "Fed funds above 4.25% nears heavy pricing consensus"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-16T05:10:00.000Z"
event_id: "CM-EVT-KWX3HB7XG9"
event_slug: "kxfed-27apr"
event_question: "Fed funds upper bound (following meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-27APR-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Apr 28, 2027 meeting?"
  current_price: 0.84
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2027-05-05T18:05:00Z"
bullets:
  - "Kalshi ladder puts 84% odds on the Fed funds upper bound exceeding 4.25%, with 95% above 4.0% and 98% above 3.75%."
  - "Boston Fed President Susan Collins' call for gradual hikes is consistent with the ladder pricing a move above 4.25% as the heavy-favorite outcome."
  - "The jump from 95% above 4.0% to 84% above 4.25% marks the key uncertainty band the market is pricing around Collins' gradualist framing."
  - "Cross-referencing the near-meeting Kalshi ladder (CM-EVT-MR57HVWJT3), which sees only 10% above 4.25% for the next meeting, suggests this ladder may reflect a later meeting horizon where the cumulative path completes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Boston Fed President Susan Collins backed gradual rate hikes, citing persistent inflation and a tight labor market."
    publisher: "Anupam Nagar"
    published_at: "2026-11-16T05:10:00.000Z"
    source_url: "https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/feds-collins-backs-gradual-rate-hikes-says-inflation-and-jobs-data-warrant-tighter-policy/articleshow/135873746.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Anupam Nagar"
        source_url: "https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/feds-collins-backs-gradual-rate-hikes-says-inflation-and-jobs-data-warrant-tighter-policy/articleshow/135873746.cms"
        retrieved_at: "2026-11-16T07:48:02+00:00"
  - type: "pm_response"
    notes: "Resolution source unspecified; the ladder's 84% above 4.25% read is internally consistent with the near-meeting ladder assuming a step-by-step tightening path."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Anupam Nagar: Fed's Collins backs gradual rate hikes, says inflation and jobs data w"
    url: "https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/feds-collins-backs-gradual-rate-hikes-says-inflation-and-jobs-data-warrant-tighter-policy/articleshow/135873746.cms"
    published_at: "2026-11-16T05:10:00.000Z"
    retrieved_at: "2026-11-16T07:48:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
