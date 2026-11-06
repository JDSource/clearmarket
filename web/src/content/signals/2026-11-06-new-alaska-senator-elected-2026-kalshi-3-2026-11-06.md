---
signal_id: "CMSIG2026110604"
signal_slug: "new-alaska-senator-elected-2026-kalshi-3-2026-11-06"
headline: "New Alaska senator elected 2026: Kalshi 3%"
semantic_title: "New Alaska senator odds stay near the floor despite Democratic leads"
telemetry: "Kalshi 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-06T13:00:00.000Z"
event_id: "CM-EVT-KQWMXB6NX7"
event_slug: "senateak-26"
event_question: "Will a new senator be elected to represent Alaska in the U.S. Senate?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEAK-26-R"
  question_raw: "Will Republicans win the Senate race in Alaska?"
  current_price: 0.03
  volume_24h_usd: 69296.83
  arbitration_model: "kalshi_staff"
  resolution_source: "United States Congress"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi puts only 3% on a new senator being elected to represent Alaska, despite news reporting Democrats lead there."
  - "The contract framing and low price may reflect question-specific resolution criteria rather than a denial of the Democratic lead in the race itself."
  - "The broader Democratic wave is priced at 99% on the blue tsunami contract, making the Alaska contract's 3% a potential resolution-mechanics anomaly worth monitoring."
  - "Resolves via United States Congress certification; the gap between the 99% wave price and 3% Alaska-seat price warrants close attention to the question's exact resolution criteria."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Democrats are leading by thin margins in both the Alaska and Mississippi Senate races as vote counting continues after the midterm sweep."
    publisher: "democracynow.org"
    published_at: "2026-11-06T13:00:00.000Z"
    source_url: "https://www.democracynow.org/2026/11/6/headlines"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "democracynow.org"
        source_url: "https://www.democracynow.org/2026/11/6/headlines"
        retrieved_at: "2026-11-06T15:37:02+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 3%; the sharp divergence from the overall wave pricing signals this contract's resolution terms may differ from simple race outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "democracynow.org: Headlines for November 06, 2026 | Democracy Now!"
    url: "https://www.democracynow.org/2026/11/6/headlines"
    published_at: "2026-11-06T13:00:00.000Z"
    retrieved_at: "2026-11-06T15:37:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
