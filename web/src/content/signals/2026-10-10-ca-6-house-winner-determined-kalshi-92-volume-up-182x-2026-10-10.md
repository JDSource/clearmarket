---
signal_id: "CMSIG2026101007"
signal_slug: "ca-6-house-winner-determined-kalshi-92-volume-up-182x-2026-10-10"
headline: "CA-6 House winner determined: Kalshi 92%, volume up 182x"
semantic_title: "California 6th District House winner odds attract heavy fresh attention"
telemetry: "Kalshi 92%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-10T00:00:00.000Z"
event_id: "CM-EVT-875HC8QSZ0"
event_slug: "kxhouserace-ca06-26"
event_question: "Will the winner of the California 6th Congressional District House election be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-CA06-26-D"
  question_raw: "Will Democratic win the House race for CA-06?"
  current_price: 0.925
  volume_24h_usd: 185.55
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "The Kalshi prediction market prices the CA-6 House race winner being determined by the settlement date at 92%, with trading volume up 18,098% day over day."
  - "The surge in volume, not just the probability level, signals this contract is drawing significant fresh attention as the midterm environment shifts."
  - "The nearby CA-15 Kalshi contract sits at 97% and the Iowa 4th at 96%, suggesting markets broadly expect most House races to be called on schedule."
  - "Resolution via Library of Congress; the contract requires an officially recorded winner, not a projection, which could lag if California counting is slow."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Nonpartisan forecasters have shifted multiple congressional contests toward Democrats as Trump campaigns to motivate low-propensity Republican voters before November 3."
    publisher: "Marianne LeVine, Meridith McGraw, Philip Wegmann"
    published_at: "2026-10-10T00:00:00.000Z"
    source_url: "https://www.wsj.com/politics/elections/trump-midterm-election-strategy-e4cfea75"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Marianne LeVine, Meridith McGraw, Philip Wegmann"
        source_url: "https://www.wsj.com/politics/elections/trump-midterm-election-strategy-e4cfea75"
        retrieved_at: "2026-10-10T07:47:51+00:00"
  - type: "pm_response"
    notes: "Kalshi at 92%; resolves via Library of Congress; volume spike of 182x day over day is a confirmed data point from provided marks."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Marianne LeVine, Meridith McGraw, Philip Wegmann: Trump’s Hit-the-Road Strategy Aims to Stave Off Republican Midterm Ele"
    url: "https://www.wsj.com/politics/elections/trump-midterm-election-strategy-e4cfea75"
    published_at: "2026-10-10T00:00:00.000Z"
    retrieved_at: "2026-10-10T07:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
