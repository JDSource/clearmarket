---
signal_id: "CMSIG2026102008"
signal_slug: "trump-approval-above-43-during-window-ladder-implies-below-4-2026-10-20"
headline: "Trump approval above 43% during window: ladder implies below 43%"
semantic_title: "Trump approval above 43 percent priced as a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-20T10:00:00.000Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating during measurement window"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.031
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Prediction market ladder prices only 3% that Trump's approval rating exceeds 43% during the measured window, implying consensus well below that level."
  - "The ABC/WaPo/Ipsos poll showing two-thirds wrong-track sentiment is fully consistent with sub-43% approval pricing."
  - "Kalshi separately prices only 11% that Trump's approval falls below a lower threshold by December 31, 2026, suggesting markets see approval as low but not collapsing further."
  - "Ladder resolution depends on a named polling organization; the exact polling source and date window determine which strike settles."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "An ABC News/Washington Post/Ipsos poll found two-thirds of Americans say the country is headed in the wrong direction, citing the economy and the Iran war as key drags on Trump's approval."
    publisher: "Emily Guskin"
    published_at: "2026-10-20T10:00:00.000Z"
    source_url: "https://abcnews.com/Politics/thirds-americans-country-headed-wrong-direction-abc-newswashington/story?id=132583099"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Emily Guskin"
        source_url: "https://abcnews.com/Politics/thirds-americans-country-headed-wrong-direction-abc-newswashington/story?id=132583099"
        retrieved_at: "2026-10-20T13:15:16+00:00"
  - type: "pm_response"
    notes: "Prediction market ladder and Kalshi binary together bracket Trump approval as likely stuck in a narrow low range through year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Emily Guskin: Two-thirds of Americans say country is headed in the wrong direction:"
    url: "https://abcnews.com/Politics/thirds-americans-country-headed-wrong-direction-abc-newswashington/story?id=132583099"
    published_at: "2026-10-20T10:00:00.000Z"
    retrieved_at: "2026-10-20T13:15:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
