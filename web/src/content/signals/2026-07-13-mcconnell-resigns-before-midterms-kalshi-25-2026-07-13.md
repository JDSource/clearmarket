---
signal_id: "CMSIG2026071307"
signal_slug: "mcconnell-resigns-before-midterms-kalshi-25-2026-07-13"
headline: "McConnell resigns before midterms: Kalshi 25%"
semantic_title: "McConnell Senate resignation before midterms holds as a quarter-odds bet"
telemetry: "Kalshi 25%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-13T00:00:00.000Z"
event_id: "CM-EVT-DF795XDRC0"
event_slug: "kxretiremm-26"
event_question: "Will Mitch McConnell resign his office before the midterms?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRETIREMM-26"
  question_raw: "Will Mitch McConnell resign his office early?"
  current_price: 0.25
  volume_24h_usd: 20206.94
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices 25% on Mitch McConnell resigning his Senate office before the midterms, resolving via Library of Congress."
  - "McConnell's unexplained absence since June 14 hospitalization and Graham's death simultaneously thin the Senate Republican leadership bench, lending the 25% reading context."
  - "The 94% Kalshi reading on CM-EVT-RSPZ64CMS2 for Senate Republicans losing primaries in 2026 reflects a separate but related Senate-volatility signal."
  - "Resolves via Library of Congress confirmation of a formal resignation; absence from public view alone does not trigger resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Senate returned to Washington with an uncertain agenda after Senator Lindsey Graham's sudden death, with Mitch McConnell also absent since his June 14 hospitalization."
    publisher: "ABC News"
    published_at: "2026-07-13T00:00:00.000Z"
    source_url: "https://abcnews.com/US/wireStory/senate-returns-washington-after-sen-lindsey-grahams-death-134703677"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/US/wireStory/senate-returns-washington-after-sen-lindsey-grahams-death-134703677"
        retrieved_at: "2026-07-13T10:56:18+00:00"
  - type: "pm_response"
    notes: "Kalshi at 25% treats McConnell's resignation as a meaningful tail risk given his hospitalization, but well short of a base-case outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: Senate returns to Washington after Sen. Lindsey Graham's death with un"
    url: "https://abcnews.com/US/wireStory/senate-returns-washington-after-sen-lindsey-grahams-death-134703677"
    published_at: "2026-07-13T00:00:00.000Z"
    retrieved_at: "2026-07-13T10:56:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
