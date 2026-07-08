---
signal_id: "CMSIG2026070707"
signal_slug: "trump-creates-national-bitcoin-reserve-by-2027-kalshi-14-2026-07-07"
headline: "Trump creates National Bitcoin Reserve by 2027: Kalshi 14%"
semantic_title: "National Bitcoin Reserve creation before 2027 holds at long odds"
telemetry: "Kalshi 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-07T05:34:22.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve before 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.14
  volume_24h_usd: 128.79
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only a 14% probability that Trump formally creates a National Bitcoin Reserve before 2027, resolving via The New York Times."
  - "Despite executive order reporting, the market assigns low probability to formal reserve creation, consistent with a concurrent story that the initiative has stalled in an interdepartmental dispute between Treasury and Commerce."
  - "Bitcoin dropped below $73,000 amid Iran-US military escalation (Story 32), adding geopolitical risk-off pressure to an already uncertain crypto policy environment."
  - "Kalshi prices only a 10% chance Trump attempts to fire Federal Reserve Chair Jerome Powell (CM-EVT-TMHG8WLK69), suggesting the market does not see broader institutional disruption as the base case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A news report described a US Strategic Bitcoin Reserve established via executive order, treating seized Bitcoin as a long-term national asset, while a separate report said the initiative has stalled due to a Treasury-Commerce turf dispute."
    publisher: "Editorial Team"
    published_at: "2026-07-07T05:34:22.000Z"
    source_url: "https://cryptobriefing.com/us-strategic-bitcoin-reserve-established/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Editorial Team"
        source_url: "https://cryptobriefing.com/us-strategic-bitcoin-reserve-established/"
        retrieved_at: "2026-07-08T10:13:38+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via New York Times reporting; the 14% price reflects market skepticism that an executive order translates into formal reserve status given the reported bureaucratic stall."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Editorial Team: US Strategic Bitcoin Reserve established as long-term national asset u"
    url: "https://cryptobriefing.com/us-strategic-bitcoin-reserve-established/"
    published_at: "2026-07-07T05:34:22.000Z"
    retrieved_at: "2026-07-08T10:13:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
