---
signal_id: "CMSIG2026081507"
signal_slug: "2028-dem-primary-first-state-kalshi-56-2026-08-15"
headline: "2028 Dem primary first state: Kalshi 56%"
semantic_title: "Which state votes first in 2028 Democratic primary stays near 50%"
telemetry: "Kalshi 56%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-15T22:22:09.496Z"
event_id: "CM-EVT-71JN7R5VC6"
event_slug: "kxdemfirstcontest-28"
event_question: "Which state will vote first in the 2028 Democratic presidential primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXDEMFIRSTCONTEST-28-NH"
  question_raw: "Will it be reported by any of the Source Agencies that New Hampshire holds the earliest 2028 Democratic presidential contest administered by its election officials or the Democratic Party among the 50 states before Apr 1, 2028?"
  current_price: 0.56
  volume_24h_usd: 5903.78
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2028-04-08T14:00:00Z"
bullets:
  - "Kalshi prices the question of which state will vote first in the 2028 Democratic presidential primary at 56% for the leading option, resolved via The Washington Post."
  - "The DNC's formal calendar approval is a direct catalyst for this contract, though the 56% price indicates the market is not treating the outcome as a certainty."
  - "At 56%, roughly four-in-ten probability remains on an alternative first-voting state, suggesting market participants see room for further procedural challenge or court intervention."
  - "Resolves via The Washington Post's coverage of the certified 2028 Democratic primary calendar order."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Democrats approved a shakeup to the 2028 presidential primary calendar at a DNC meeting in Austin, reshuffling state ordering."
    publisher: "Evan Semones"
    published_at: "2026-08-15T22:22:09.496Z"
    source_url: "https://www.aljazeera.com/news/2026/8/15/us-democrats-finalise-major-shakeup-to-2028-presidential-primary-calendar"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Evan Semones"
        source_url: "https://www.aljazeera.com/news/2026/8/15/us-democrats-finalise-major-shakeup-to-2028-presidential-primary-calendar"
        retrieved_at: "2026-08-16T08:23:09+00:00"
  - type: "pm_response"
    notes: "Kalshi's 56% on the 2028 Democratic primary first-state question reflects residual uncertainty even after the DNC's formal calendar vote, with The Washington Post as the named resolution source."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Evan Semones: US Democrats finalise major shakeup to 2028 presidential primary calen"
    url: "https://www.aljazeera.com/news/2026/8/15/us-democrats-finalise-major-shakeup-to-2028-presidential-primary-calendar"
    published_at: "2026-08-15T22:22:09.496Z"
    retrieved_at: "2026-08-16T08:23:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
