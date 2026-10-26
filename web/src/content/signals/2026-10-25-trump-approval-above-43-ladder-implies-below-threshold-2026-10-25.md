---
signal_id: "CMSIG2026102505"
signal_slug: "trump-approval-above-43-ladder-implies-below-threshold-2026-10-25"
headline: "Trump approval above 43%: ladder implies below threshold"
semantic_title: "Trump approval rating stays below 43 percent on prediction market ladder"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-25T00:00:00.000Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating, December 31 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.084
  volume_24h_usd: 2.52
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Prediction market ladder prices only 8% on Trump's approval rating finishing above 43% by December 31, 2026."
  - "The ABC/WaPo/Ipsos poll finding two-thirds wrong-track sentiment is directionally consistent with the market keeping approval well below the 43% threshold."
  - "The steep drop-off, 8% at 43%, 6% at 44%, then fading, suggests the market sees upside past 43% as a tail risk."
  - "A companion Kalshi contract (CM-EVT-0DMSQTKVX3) also sits at 16% on a separate below-threshold approval test, both pointing to a bearish approval outlook through year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "An ABC News/Washington Post/Ipsos poll shows two-thirds of Americans say the country is headed in the wrong direction, weighing on Trump's approval ratings."
    publisher: "Emily Guskin"
    published_at: "2026-10-25T00:00:00.000Z"
    source_url: "https://abcnews.com/Politics/thirds-americans-country-headed-wrong-direction-abc-newswashington/story?id=132583099"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Emily Guskin"
        source_url: "https://abcnews.com/Politics/thirds-americans-country-headed-wrong-direction-abc-newswashington/story?id=132583099"
        retrieved_at: "2026-10-26T07:47:50+00:00"
  - type: "pm_response"
    notes: "Ladder contract (unspecified venue); distribution collapses rapidly above 43%, implying the market is firmly below that level."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Emily Guskin: Two-thirds of Americans say country is headed in the wrong direction:"
    url: "https://abcnews.com/Politics/thirds-americans-country-headed-wrong-direction-abc-newswashington/story?id=132583099"
    published_at: "2026-10-25T00:00:00.000Z"
    retrieved_at: "2026-10-26T07:47:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
