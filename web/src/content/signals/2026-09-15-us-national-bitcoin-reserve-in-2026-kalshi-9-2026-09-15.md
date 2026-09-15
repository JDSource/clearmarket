---
signal_id: "CMSIG2026091505"
signal_slug: "us-national-bitcoin-reserve-in-2026-kalshi-9-2026-09-15"
headline: "US national Bitcoin reserve in 2026: Kalshi 9%"
semantic_title: "National Bitcoin Reserve odds stay in long-shot range"
telemetry: "Kalshi 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-15T07:26:38.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.094
  volume_24h_usd: 0.94
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices Trump creating a National Bitcoin Reserve in 2026 at 9%, resolving via The New York Times."
  - "A House committee vote is a very early legislative step, the market at 9% reflects that committee passage does not guarantee floor votes, Senate action, or signing before year-end."
  - "Polymarket's US national Bitcoin reserve contract (CM-EVT-0F2G0B8X49) sits at 7%, a tight cross-venue gap confirming both platforms view this as a long shot for 2026."
  - "Resolution on Kalshi requires New York Times confirmation of actual reserve creation, committee action alone does not settle this contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Strategic Bitcoin Reserve bill is set for a House committee vote Wednesday, advancing the legislative process for a government Bitcoin holding."
    publisher: "Rony Roy"
    published_at: "2026-09-15T07:26:38.000Z"
    source_url: "https://crypto.news/strategic-bitcoin-reserve-bill-set-for-house-committee-vote-wednesday/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rony Roy"
        source_url: "https://crypto.news/strategic-bitcoin-reserve-bill-set-for-house-committee-vote-wednesday/"
        retrieved_at: "2026-09-15T13:05:57+00:00"
  - type: "pm_response"
    notes: "Kalshi at 9% and Polymarket at 7% are closely aligned, with both markets treating Wednesday's committee vote as an early procedural milestone, not a decisive catalyst."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rony Roy: Strategic Bitcoin Reserve bill set for House committee vote Wednesday"
    url: "https://crypto.news/strategic-bitcoin-reserve-bill-set-for-house-committee-vote-wednesday/"
    published_at: "2026-09-15T07:26:38.000Z"
    retrieved_at: "2026-09-15T13:05:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
