---
signal_id: "CMSIG2026062402"
signal_slug: "hormuz-traffic-normal-by-june-30-polymarket-18-2026-06-24"
headline: "Hormuz traffic normal by June 30: Polymarket 18%"
semantic_title: "Hormuz normalcy by June 30 holds slim odds despite diplomacy"
telemetry: "Polymarket 18%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T14:27:55.000Z"
event_id: "CM-EVT-YPW93GCTK6"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-end-of-june"
event_question: "Will traffic through the Strait of Hormuz return to normal by the end of June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x348cd9adf4f6855f58bd9c6dbf9ff251c4142ef77233a5dc95c65b4b61cd2187"
  question_raw: "Strait of Hormuz traffic returns to normal by end of June?"
  current_price: 0.18
  volume_24h_usd: 2192769.440225002
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices Hormuz traffic returning to normal by June 30 at just 18%, reflecting deep skepticism about near-term resolution."
  - "Rubio's firm rejection of Iranian tolls and ongoing UAE anxiety show the market's low probability is consistent with real diplomatic friction."
  - "The year-end Polymarket contract on Hormuz normalcy sits at 78%, implying the market expects eventual resolution but not within days."
  - "Resolves via portwatch.imf.org traffic data; physical shipping flow, not a diplomatic statement, determines settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US Secretary of State Marco Rubio dismissed Iranian toll demands on the Strait of Hormuz as semantics, while the UAE raised concerns and active diplomacy continued."
    publisher: "Caolán Magee"
    published_at: "2026-06-24T14:27:55.000Z"
    source_url: "https://www.aljazeera.com/news/2026/6/24/rubio-says-iran-cannot-charge-tolls-in-hormuz-what-we-know"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Caolán Magee"
        source_url: "https://www.aljazeera.com/news/2026/6/24/rubio-says-iran-cannot-charge-tolls-in-hormuz-what-we-know"
        retrieved_at: "2026-06-25T10:38:54+00:00"
  - type: "pm_response"
    notes: "Polymarket prices only an 18% chance of June 30 normalcy, while the December contract at 78% reveals the market's longer-horizon optimism."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Caolán Magee: Rubio says Iran cannot charge tolls in Hormuz: What we know | US-Israe"
    url: "https://www.aljazeera.com/news/2026/6/24/rubio-says-iran-cannot-charge-tolls-in-hormuz-what-we-know"
    published_at: "2026-06-24T14:27:55.000Z"
    retrieved_at: "2026-06-25T10:38:54+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
