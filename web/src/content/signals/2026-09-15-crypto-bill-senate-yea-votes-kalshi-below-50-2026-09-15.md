---
signal_id: "CMSIG2026091503"
signal_slug: "crypto-bill-senate-yea-votes-kalshi-below-50-2026-09-15"
headline: "Crypto bill Senate Yea votes: Kalshi below 50"
semantic_title: "Senate Yea votes on crypto bill priced well below 50"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-15T19:01:42.078Z"
event_id: "CM-EVT-CSYS5KPXK6"
event_slug: "kxvoteclarity-26may16"
event_question: "Senate Yea votes on crypto market structure bill"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTECLARITY-26MAY16-T50"
  question_raw: "How many Senate members will vote Yea on a crypto market structure bill (as defined in KXCRYPTOSTRUCTURE)?"
  current_price: 0.1
  volume_24h_usd: 4196.95
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi ladder on Senate Yea votes prices 50 votes at just 10% and every higher strike at 8% or below, fully consistent with the 49-50 failure."
  - "The 49-50 procedural vote confirms the ladder's distribution: the market was pricing a sub-50 outcome as the modal scenario before the vote."
  - "The Polymarket contract on the Clarity Act becoming law by 2026 sits at 5%, suggesting markets see little chance of a reattempt clearing both chambers this year."
  - "The Kalshi contract resolves on the recorded Senate vote count; the Polymarket signing-into-law contract resolves via UMA oracle and requires full legislative passage."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Clarity Act, crypto's flagship market-structure bill, failed a 60-vote Senate procedural threshold on a 49-50 vote, dealing a major blow to the industry."
    publisher: "CoinDesk"
    published_at: "2026-09-15T19:01:42.078Z"
    source_url: "https://www.coindesk.com/policy/2026/09/15/crypto-clarity-act-flames-out-in-failed-u-s-senate-vote"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "CoinDesk"
        source_url: "https://www.coindesk.com/policy/2026/09/15/crypto-clarity-act-flames-out-in-failed-u-s-senate-vote"
        retrieved_at: "2026-09-16T13:02:46+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder had already priced a sub-50 Yea outcome as most likely; the 49-50 result confirms the market read ahead of the vote."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "CoinDesk: Crypto’s biggest Senate push falls flat as the Clarity Act fails to cl"
    url: "https://www.coindesk.com/policy/2026/09/15/crypto-clarity-act-flames-out-in-failed-u-s-senate-vote"
    published_at: "2026-09-15T19:01:42.078Z"
    retrieved_at: "2026-09-16T13:02:46+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
