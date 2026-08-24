---
signal_id: "CMSIG2026082204"
signal_slug: "trump-2026-sector-tariffs-kalshi-34-2026-08-22"
headline: "Trump 2026 sector tariffs: Kalshi 34%"
semantic_title: "Broader 2026 tariff expansion holds below 50 percent"
telemetry: "Kalshi 34%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-22T00:00:00.000Z"
event_id: "CM-EVT-YH6B0KCSV8"
event_slug: "kxtariffsector-27jan01"
event_question: "Which sectors will Trump impose tariffs on in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTARIFFSECTOR-27JAN01-WIND"
  question_raw: "Will Trump issue any executive action on imposing tariffs specifically on wind turbines, where the executive action must explicitly reference wind turbines in its title, operative text, or fact sheet (not merely in an attached tariff schedule annex) during in 2026?"
  current_price: 0.34
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "the White House"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market puts 34% odds on Trump imposing sector-specific tariffs on additional categories in 2026, resolves via the White House."
  - "The Canada tariff action is concrete and enacted, yet the Kalshi contract for broader sector escalation sits well below 50%, suggesting markets are not pricing a generalized tariff wave."
  - "Canada's announced dollar-for-dollar retaliation beginning September 8 raises the stakes but has not shifted the sub-50% sector-tariff read."
  - "The Polymarket contract on U.S. debt downgrade before 2027 (CM-EVT-PG006HKDD7) sits at just 6%, indicating markets are not linking the trade escalation to a sovereign credit event."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The United States imposed 50% tariffs on roughly 20 billion dollars worth of Canadian products after last-ditch trade negotiations collapsed."
    publisher: "apnews.com"
    published_at: "2026-08-22T00:00:00.000Z"
    source_url: "https://apnews.com/article/canada-us-trade-tariffs-trump-857ef76b20a766e370d70176135b678e"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/canada-us-trade-tariffs-trump-857ef76b20a766e370d70176135b678e"
        retrieved_at: "2026-08-24T08:42:17+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via the White House on whether new sector-specific tariffs are imposed in 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: US imposes 50% tariffs on Canadian products | AP News"
    url: "https://apnews.com/article/canada-us-trade-tariffs-trump-857ef76b20a766e370d70176135b678e"
    published_at: "2026-08-22T00:00:00.000Z"
    retrieved_at: "2026-08-24T08:42:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
