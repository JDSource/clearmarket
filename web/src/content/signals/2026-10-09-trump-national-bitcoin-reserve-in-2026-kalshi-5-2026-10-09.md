---
signal_id: "CMSIG2026100907"
signal_slug: "trump-national-bitcoin-reserve-in-2026-kalshi-5-2026-10-09"
headline: "Trump National Bitcoin Reserve in 2026: Kalshi 5%"
semantic_title: "Trump National Bitcoin Reserve in 2026 stays a long shot on Kalshi"
telemetry: "Kalshi 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-09T00:00:00.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.05
  volume_24h_usd: 0.06
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices a 5% chance Trump formally creates a National Bitcoin Reserve in 2026, keeping the claim a long shot despite the government transfer."
  - "The Coinbase Prime movement is a custody transfer, not a confirmed sale or reserve establishment; the low Kalshi probability is consistent with no policy announcement."
  - "A companion Polymarket contract on the US establishing a national Bitcoin reserve before 2027 sits at 3%, slightly below the Kalshi read but directionally aligned."
  - "Resolution via The New York Times as the named source on Kalshi; a formal executive or legislative action establishing the reserve is the qualifying trigger."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US government moved roughly 1.5 billion dollars in Bitcoin to Coinbase Prime, though on-chain data does not confirm a sale."
    publisher: "Tim Baker"
    published_at: "2026-10-09T00:00:00.000Z"
    source_url: "https://tokenist.com/bitcoin-transfer-new-addresses/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Tim Baker"
        source_url: "https://tokenist.com/bitcoin-transfer-new-addresses/"
        retrieved_at: "2026-10-10T14:11:44+00:00"
  - type: "pm_response"
    notes: "Kalshi and Polymarket both price this outcome as a long shot; the cross-venue gap of 2 percentage points is narrow and within normal spread."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Tim Baker: US Government Moves $1.5B in Bitcoin to Coinbase Prime"
    url: "https://tokenist.com/bitcoin-transfer-new-addresses/"
    published_at: "2026-10-09T00:00:00.000Z"
    retrieved_at: "2026-10-10T14:11:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
