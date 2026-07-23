---
signal_id: "CMSIG2026072302"
signal_slug: "hormuz-normal-by-july-31-polymarket-1-2026-07-23"
headline: "Hormuz normal by July 31: Polymarket 1%"
semantic_title: "Hormuz July normalization priced as near-certain no"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-23T00:00:00.000Z"
event_id: "CM-EVT-4J73Y3RD96"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-july-31"
event_question: "Will Strait of Hormuz traffic return to normal by July 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb8e6d129a06d0ccb21d7b32eb529ea455eddba3cf29bfa097112202cbdf5bf21"
  question_raw: "Strait of Hormuz traffic returns to normal by July 31?"
  current_price: 0.011
  volume_24h_usd: 348394.8282660002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-31T00:00:00Z"
bullets:
  - "Polymarket prices only 1% probability that Strait of Hormuz traffic returns to normal by July 31, 2026."
  - "An IRGC-confirmed tanker explosion and an explicit warning that no vessel will transit are fully consistent with this near-zero near-term probability."
  - "The December 31 Polymarket contract at 50% implies the market sees the second half of 2026 as the only realistic window for de-escalation."
  - "Resolves via UMA oracle; the definition of 'normal traffic', likely benchmarked against pre-conflict transit counts, is the critical settlement question."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's Revolutionary Guard reported an oil tanker hit by an explosion in the Strait of Hormuz, with two vessels turning back and IRGC warning no ships would be allowed to transit."
    publisher: "aa.com.tr"
    published_at: "2026-07-23T00:00:00.000Z"
    source_url: "https://www.aa.com.tr/en/middle-east/iran-s-revolutionary-guard-says-oil-tanker-hit-by-explosion-in-strait-of-hormuz-2-vessels-turn-back/4006383"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aa.com.tr"
        source_url: "https://www.aa.com.tr/en/middle-east/iran-s-revolutionary-guard-says-oil-tanker-hit-by-explosion-in-strait-of-hormuz-2-vessels-turn-back/4006383"
        retrieved_at: "2026-07-23T10:16:46+00:00"
  - type: "pm_response"
    notes: "Polymarket's 1% on July and 50% on December paint a clear term structure: the market assigns essentially zero chance of near-term resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aa.com.tr: Iran’s Revolutionary Guard says oil tanker hit by explosion in Strait"
    url: "https://www.aa.com.tr/en/middle-east/iran-s-revolutionary-guard-says-oil-tanker-hit-by-explosion-in-strait-of-hormuz-2-vessels-turn-back/4006383"
    published_at: "2026-07-23T00:00:00.000Z"
    retrieved_at: "2026-07-23T10:16:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
