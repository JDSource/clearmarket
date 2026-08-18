---
signal_id: "CMSIG2026081702"
signal_slug: "fed-cut-above-25bp-this-year-kalshi-5-2026-08-17"
headline: "Fed cut above 25bp this year: Kalshi 5%"
semantic_title: "Odds on an outsized Fed cut stay near the floor"
telemetry: "Kalshi 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-17T00:00:00.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.05
  volume_24h_usd: 3.39
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi contract on a Fed cut greater than 25 basis points in 2026 sits at just 5%."
  - "Business Insider's hike-fade narrative is consistent with no large cut either, the market is pricing a firm hold, not a pivot."
  - "PCE inflation at 3.7% in June, still well above the 2% target, gives the Fed little cover for aggressive easing."
  - "The companion Polymarket hike contract at 47% (CM-EVT-87QV1G78C4) creates an asymmetric picture: roughly even chance of a hike, near-zero chance of a big cut."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Wall Street is souring on a September rate hike, with four cited reasons pointing to a prolonged pause rather than any near-term policy move in either direction."
    publisher: "William Edwards"
    published_at: "2026-08-17T00:00:00.000Z"
    source_url: "https://www.businessinsider.com/why-wall-street-is-abandoning-higher-interest-rates-federal-reserve-2026-8"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "William Edwards"
        source_url: "https://www.businessinsider.com/why-wall-street-is-abandoning-higher-interest-rates-federal-reserve-2026-8"
        retrieved_at: "2026-08-18T08:30:34+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Federal Reserve official decision; the 5% price reflects the wide gap between current inflation and any conditions that would justify an emergency-sized cut."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "William Edwards: Rate Hike Forecast: 4 Reasons Why Wall Street Is Souring on a Sept. Mo"
    url: "https://www.businessinsider.com/why-wall-street-is-abandoning-higher-interest-rates-federal-reserve-2026-8"
    published_at: "2026-08-17T00:00:00.000Z"
    retrieved_at: "2026-08-18T08:30:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
