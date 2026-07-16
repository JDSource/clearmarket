---
signal_id: "CMSIG2026071607"
signal_slug: "trump-imposes-new-sector-tariffs-in-2026-kalshi-28-2026-07-16"
headline: "Trump imposes new sector tariffs in 2026: Kalshi 28%"
semantic_title: "Tariff sector expansion pricing holds below majority"
telemetry: "Kalshi 28%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-07-16T03:30:57.000Z"
event_id: "CM-EVT-YH6B0KCSV8"
event_slug: "kxtariffsector-27jan01"
event_question: "Which sectors will Trump impose tariffs on in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTARIFFSECTOR-27JAN01-WIND"
  question_raw: "Will Trump issue any executive action on imposing tariffs specifically on wind turbines, where the executive action must explicitly reference wind turbines in its title, operative text, or fact sheet (not merely in an attached tariff schedule annex) during in 2026?"
  current_price: 0.28
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "the White House"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices 28% on Trump imposing tariffs on additional sectors in 2026, even after a concrete 25% Brazil tariff announcement."
  - "The Brazil tariff targets specific imports rather than a broad new sector, which may explain why the sector-expansion contract holds below 30%."
  - "The White House cited unfair trade practices as the trigger, a framework that could apply to other trading partners, though markets do not yet price that extension as likely."
  - "Kalshi resolves via White House official announcement; the contract language specifies sectors, so the Brazil action's scope relative to sector definitions is the key resolution edge case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US announced 25% tariffs on some Brazilian imports effective July 22, citing a range of unfair trade practices by the world's tenth-largest economy."
    publisher: "apnews.com"
    published_at: "2026-07-16T03:30:57.000Z"
    source_url: "https://apnews.com/article/us-brazil-trade-tariffs-99e8c52a44c75f31c343d7ebad41f614"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/us-brazil-trade-tariffs-99e8c52a44c75f31c343d7ebad41f614"
        retrieved_at: "2026-07-16T10:04:17+00:00"
  - type: "pm_response"
    notes: "Kalshi at 28% on new sector tariffs reflects market skepticism that the Brazil action signals broader sector-level tariff expansion beyond already-announced measures."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: US to impose 25% tariff on some Brazilian imports starting July 22 | A"
    url: "https://apnews.com/article/us-brazil-trade-tariffs-99e8c52a44c75f31c343d7ebad41f614"
    published_at: "2026-07-16T03:30:57.000Z"
    retrieved_at: "2026-07-16T10:04:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
