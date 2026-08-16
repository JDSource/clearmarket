---
signal_id: "CMSIG2026081404"
signal_slug: "hormuz-7-day-transit-avg-below-40-calls-kalshi-ladder-41-2026-08-14"
headline: "Hormuz 7-day transit avg below 40 calls: Kalshi ladder 41%"
semantic_title: "Strait of Hormuz transit traffic stays heavily discounted below 40 calls"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-14T00:00:00.000Z"
event_id: "CM-EVT-JR1WTQ5JH0"
event_slug: "kxhormuzavg-27jan01"
event_question: "7-day moving average of transit calls through the Strait of Hormuz"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHORMUZAVG-27JAN01-A40"
  question_raw: "Will the 7-day moving average of transit calls through the Strait of Hormuz as reported by the IMF PortWatch be above 40 after July 6, 2026 and before Jan 1, 2027?"
  current_price: 0.41
  volume_24h_usd: 0.41
  arbitration_model: "kalshi_staff"
  resolution_source: "the Statistical Review of World Energy"
  resolves_at: "2027-04-05T14:00:00Z"
bullets:
  - "Kalshi ladder prices a 41% chance the 7-day moving average of Hormuz transit calls stays at or below 40; probability rises sharply through lower thresholds, implying severe disruption is already the base case."
  - "Iran's halt of tanker traffic and flat-out rejection of US negotiations align with a market distribution heavily weighted toward continued low transit activity."
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 sits at 44%, suggesting even a year-end recovery is seen as a coin flip."
  - "Resolution tracks the 7-day moving average of transit calls through the Strait of Hormuz using shipping data."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Iran halted oil tanker traffic through the Strait of Hormuz and rebuffed US peace overtures, with Trump telling Americans to accept higher gasoline prices."
    publisher: "Eman Abouhassira"
    published_at: "2026-08-14T00:00:00.000Z"
    source_url: "https://www.reuters.com/world/us/trump-urges-americans-accept-higher-gas-prices-he-escalates-iran-rhetoric-2026-08-14/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Eman Abouhassira"
        source_url: "https://www.reuters.com/world/us/trump-urges-americans-accept-higher-gas-prices-he-escalates-iran-rhetoric-2026-08-14/"
        retrieved_at: "2026-08-16T08:23:09+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder and the Polymarket year-end normalization contract at 44% together paint a picture of a market expecting prolonged Hormuz disruption with no clear resolution path priced in."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Eman Abouhassira: Iran defiant on strait as Trump tells Americans to accept high gasolin"
    url: "https://www.reuters.com/world/us/trump-urges-americans-accept-higher-gas-prices-he-escalates-iran-rhetoric-2026-08-14/"
    published_at: "2026-08-14T00:00:00.000Z"
    retrieved_at: "2026-08-16T08:23:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
