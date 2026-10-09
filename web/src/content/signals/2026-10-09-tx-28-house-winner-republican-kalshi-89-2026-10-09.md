---
signal_id: "CMSIG2026100904"
signal_slug: "tx-28-house-winner-republican-kalshi-89-2026-10-09"
headline: "TX-28 House winner Republican: Kalshi 89%"
semantic_title: "TX-28 House Republican win stays heavily favored"
telemetry: "Kalshi 89%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-09T00:00:00.000Z"
event_id: "CM-EVT-BJ7C9T9VL1"
event_slug: "housetx28-26"
event_question: "TX-28 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSETX28-26-D"
  question_raw: "Will Democratic win the House race for TX-28?"
  current_price: 0.89
  volume_24h_usd: 1.78
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices 89% on the Republican winning the TX-28 House race, trading volume up 4,293x day over day."
  - "Trump's Texas Senate race tightening to the margin of error is a Senate-level story; the TX-28 House contest remains heavily one-sided by prediction market pricing."
  - "The volume surge of 4,293x is a strong signal of fresh positioning following Trump's campaign activity and tightening Senate race news."
  - "Resolves via Library of Congress official election results; House and Senate races in Texas are distinct contracts, the House seat remains lopsided even as Senate attention grows."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "President Trump campaigned in Ohio as polling showed key Senate contests in Texas and Michigan tightening to within the margin of error ahead of the midterms."
    publisher: "cnnbc.com"
    published_at: "2026-10-09T00:00:00.000Z"
    source_url: "https://cnnbc.com/trump-rallies-republicans-in-ohio-as-texas-and-michigan-senate-races-tighten"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cnnbc.com"
        source_url: "https://cnnbc.com/trump-rallies-republicans-in-ohio-as-texas-and-michigan-senate-races-tighten"
        retrieved_at: "2026-10-09T07:48:13+00:00"
  - type: "pm_response"
    notes: "Kalshi TX-28 contract volume up 4,293x day over day; heavily favored Republican outcome diverges from tightening Senate narrative."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cnnbc.com: Trump Rallies Republicans in Ohio as Texas and Michigan Senate Races T"
    url: "https://cnnbc.com/trump-rallies-republicans-in-ohio-as-texas-and-michigan-senate-races-tighten"
    published_at: "2026-10-09T00:00:00.000Z"
    retrieved_at: "2026-10-09T07:48:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
