---
signal_id: "CMSIG2026072201"
signal_slug: "hormuz-back-to-normal-by-july-31-polymarket-1-2026-07-22"
headline: "Hormuz back to normal by July 31: Polymarket 1%"
semantic_title: "Hormuz reopening by July 31 stays a near-certain long shot"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-22T00:00:00.000Z"
event_id: "CM-EVT-4J73Y3RD96"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-july-31"
event_question: "Will Strait of Hormuz traffic return to normal by July 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb8e6d129a06d0ccb21d7b32eb529ea455eddba3cf29bfa097112202cbdf5bf21"
  question_raw: "Strait of Hormuz traffic returns to normal by July 31?"
  current_price: 0.011
  volume_24h_usd: 335555.37619299995
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-31T00:00:00Z"
bullets:
  - "Polymarket prices only 1% on Strait of Hormuz traffic returning to normal by July 31."
  - "Rubio's statement that Iran is not serious about talks is fully consistent with the near-zero July probability."
  - "The December 31 Polymarket contract sits at 54%, implying markets see a resolution window opening only after summer."
  - "Resolves via UMA oracle; any ambiguity over what constitutes 'normal' traffic levels is the key settlement edge."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Secretary of State Marco Rubio said the US will intensify strikes until Iran reopens the Strait of Hormuz, while accusing Tehran of failing to engage seriously in diplomacy."
    publisher: "irishtimes.com"
    published_at: "2026-07-22T00:00:00.000Z"
    source_url: "https://www.irishtimes.com/world/middle-east/2026/07/22/us-secretary-of-state-marco-rubio-claims-iran-not-serious-about-peace-talks/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "irishtimes.com"
        source_url: "https://www.irishtimes.com/world/middle-east/2026/07/22/us-secretary-of-state-marco-rubio-claims-iran-not-serious-about-peace-talks/"
        retrieved_at: "2026-07-22T10:22:09+00:00"
  - type: "pm_response"
    notes: "Polymarket's 1% July contract versus 54% December contract shows the market assigns essentially zero chance of near-term resolution but leaves the year-end outcome genuinely open."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "irishtimes.com: US secretary of state Marco Rubio claims Iran not serious about peace"
    url: "https://www.irishtimes.com/world/middle-east/2026/07/22/us-secretary-of-state-marco-rubio-claims-iran-not-serious-about-peace-talks/"
    published_at: "2026-07-22T00:00:00.000Z"
    retrieved_at: "2026-07-22T10:22:09+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
