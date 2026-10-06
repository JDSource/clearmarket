---
signal_id: "CMSIG2026100608"
signal_slug: "trump-creates-national-bitcoin-reserve-in-2026-kalshi-5-2026-10-06"
headline: "Trump creates National Bitcoin Reserve in 2026: Kalshi 5%"
semantic_title: "National Bitcoin Reserve in 2026 stays a long shot on Kalshi"
telemetry: "Kalshi 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-06T00:00:00.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.05
  volume_24h_usd: 14.64
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract on Trump creating a National Bitcoin Reserve in 2026 sits at 5%."
  - "FinCEN's withdrawal of the private wallet reporting rule is a pro-crypto regulatory move, but the market does not treat it as a stepping stone toward a formal Bitcoin Reserve, the contract is near unchanged."
  - "A companion Polymarket contract on the Clarity Act being signed into law by 2026 (CM-EVT-ZXN47LV744) prices at 5%, suggesting the market sees incremental deregulation as distinct from landmark crypto legislation."
  - "Resolves via The New York Times per Kalshi contract terms; an executive order or legislation formally establishing a reserve would be required."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US Treasury's FinCEN withdrew two long-pending proposals that would have imposed reporting requirements on crypto sent to private wallets and crypto mixers."
    publisher: "Shaurya Malwa"
    published_at: "2026-10-06T00:00:00.000Z"
    source_url: "https://www.coindesk.com/policy/2026/10/06/u-s-scraps-proposed-usd10-000-reporting-rule-for-for-crypto-sent-to-private-wallets"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Shaurya Malwa"
        source_url: "https://www.coindesk.com/policy/2026/10/06/u-s-scraps-proposed-usd10-000-reporting-rule-for-for-crypto-sent-to-private-wallets"
        retrieved_at: "2026-10-06T07:48:15+00:00"
  - type: "pm_response"
    notes: "Kalshi holds the Bitcoin Reserve contract at 5% despite a string of pro-crypto regulatory actions, consistent with markets treating policy cleanup as separate from a strategic reserve commitment."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Shaurya Malwa: U.S. scraps proposed $10,000 reporting rule for for crypto sent to pri"
    url: "https://www.coindesk.com/policy/2026/10/06/u-s-scraps-proposed-usd10-000-reporting-rule-for-for-crypto-sent-to-private-wallets"
    published_at: "2026-10-06T00:00:00.000Z"
    retrieved_at: "2026-10-06T07:48:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
