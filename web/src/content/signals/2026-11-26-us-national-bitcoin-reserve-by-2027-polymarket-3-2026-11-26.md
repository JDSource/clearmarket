---
signal_id: "CMSIG2026112605"
signal_slug: "us-national-bitcoin-reserve-by-2027-polymarket-3-2026-11-26"
headline: "US national Bitcoin reserve by 2027: Polymarket 3%"
semantic_title: "US national Bitcoin reserve before 2027 stays a long shot at 3%"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-26T04:46:01.000Z"
event_id: "CM-EVT-0F2G0B8X49"
event_slug: "us-national-bitcoin-reserve-before-2027"
event_question: "Will the United States establish a national Bitcoin reserve before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x953b1439569eef0a0e639566acd35d32ebadee8ab70dbb2f8e00bb936a277aa2"
  question_raw: "US national Bitcoin reserve before 2027?"
  current_price: 0.032
  volume_24h_usd: 273.157423
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract 'Will the United States establish a national Bitcoin reserve before 2027?' prices the outcome at just 3%."
  - "Committee passage is a legislative milestone, but Polymarket is pricing the full chain, House floor vote, Senate passage, and presidential signature, as highly unlikely before 2027."
  - "Companion Polymarket contract 'Will the US establish a national Ethereum reserve before 2027?' sits at 1%, consistent with the Bitcoin market's skepticism on crypto reserve legislation."
  - "Resolution requires a signed law establishing a national Bitcoin reserve before January 1, 2027; the lame-duck session window is narrow."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A House committee advanced a bill to codify a Strategic Bitcoin Reserve locking up government-held bitcoin for 20 years, though the bill faces a tight legislative deadline before year-end."
    publisher: "Omkar Godbole"
    published_at: "2026-11-26T04:46:01.000Z"
    source_url: "https://www.coindesk.com/policy/2026/11/26/strategic-bitcoin-reserve-bill-to-lock-up-u-s-government-held-bitcoin-for-20-years-goes-to-full-house"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Omkar Godbole"
        source_url: "https://www.coindesk.com/policy/2026/11/26/strategic-bitcoin-reserve-bill-to-lock-up-u-s-government-held-bitcoin-for-20-years-goes-to-full-house"
        retrieved_at: "2026-11-26T07:47:38+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via UMA oracle; at 3%, the market is not moving on committee news alone."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Omkar Godbole: Bill to lock up U.S. government bitcoin for 20 years advances to full"
    url: "https://www.coindesk.com/policy/2026/11/26/strategic-bitcoin-reserve-bill-to-lock-up-u-s-government-held-bitcoin-for-20-years-goes-to-full-house"
    published_at: "2026-11-26T04:46:01.000Z"
    retrieved_at: "2026-11-26T07:47:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
