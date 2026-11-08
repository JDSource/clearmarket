---
signal_id: "CMSIG2026110708"
signal_slug: "trump-national-bitcoin-reserve-in-2026-kalshi-5-2026-11-07"
headline: "Trump National Bitcoin Reserve in 2026: Kalshi 5%"
semantic_title: "National Bitcoin Reserve under Trump stays a long shot"
telemetry: "Kalshi 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-07T00:00:00.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.05
  volume_24h_usd: 8.49
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 5% on Trump creating a National Bitcoin Reserve in 2026, with trading volume up 3,486% day-over-day signaling sharp fresh interest."
  - "Treasury's crackdown on MEXC over alleged $16 billion in illicit flows points to a regulatory tightening posture that conflicts with a Bitcoin reserve move, market pricing reflects that tension."
  - "Bitcoin holding near $76K well below its post-election highs reduces political pressure for a reserve announcement in the near term."
  - "Resolves via The New York Times per the Kalshi contract; definitional scope of a 'National Bitcoin Reserve' may affect settlement if any partial or executive-order-based action is taken."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US Treasury moved to sanction MEXC Global over alleged illicit flows and crypto integration with 401(k) plans advanced, amid a broader week of crypto regulatory news."
    publisher: "theblock.co"
    published_at: "2026-11-07T00:00:00.000Z"
    source_url: "https://www.theblock.co/newsletters/the-daily/2026-11-07-treasury-mexc-crypto-401k-435962"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theblock.co"
        source_url: "https://www.theblock.co/newsletters/the-daily/2026-11-07-treasury-mexc-crypto-401k-435962"
        retrieved_at: "2026-11-08T07:47:56+00:00"
  - type: "pm_response"
    notes: "Kalshi at 5% with a 35.9x volume surge shows the Bitcoin reserve question is attracting substantial attention even as the probability remains low."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theblock.co: Treasury cuts off MEXC Global, crypto moves closer to 401(k) plans, an"
    url: "https://www.theblock.co/newsletters/the-daily/2026-11-07-treasury-mexc-crypto-401k-435962"
    published_at: "2026-11-07T00:00:00.000Z"
    retrieved_at: "2026-11-08T07:47:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
