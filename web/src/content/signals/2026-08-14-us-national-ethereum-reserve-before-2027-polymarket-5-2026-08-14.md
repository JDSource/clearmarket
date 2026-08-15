---
signal_id: "CMSIG2026081408"
signal_slug: "us-national-ethereum-reserve-before-2027-polymarket-5-2026-08-14"
headline: "US national Ethereum reserve before 2027: Polymarket 5%"
semantic_title: "US national Ethereum reserve before 2027 stays a long shot"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-14T08:20:52.293Z"
event_id: "CM-EVT-MVF6TJRMS1"
event_slug: "us-national-ethereum-reserve-before-2027"
event_question: "Will the US establish a national Ethereum reserve before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3bdf487707735a1ca84079e6a4020147c5d865c4621b7a966ca2cdd0dd7ee5b0"
  question_raw: "US national Ethereum reserve before 2027?"
  current_price: 0.05
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on the US establishing a national Ethereum reserve before 2027 sits at 5%, a deep long-shot reading."
  - "The SEC's cancellation of Reg Crypto voting removes a near-term regulatory catalyst that could have clarified Ethereum's legal status and supported a reserve case."
  - "Companion Polymarket contract CM-EVT-0F2G0B8X49 prices a national Bitcoin reserve before 2027 at 10%, suggesting Bitcoin remains twice as likely as Ethereum to receive strategic reserve treatment."
  - "Resolves via UMA oracle on Polymarket; would require a formal US government announcement of an Ethereum reserve position before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The SEC abruptly canceled its first formal Reg Crypto rulemaking vote with no rescheduled date, signaling a shift of regulatory power toward the CFTC."
    publisher: "CoinDesk"
    published_at: "2026-08-14T08:20:52.293Z"
    source_url: "https://www.coindesk.com/policy/2026/08/13/sec-cancels-long-awaited-proposal-of-reg-crypto-postponing-meeting-without-new-date"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "CoinDesk"
        source_url: "https://www.coindesk.com/policy/2026/08/13/sec-cancels-long-awaited-proposal-of-reg-crypto-postponing-meeting-without-new-date"
        retrieved_at: "2026-08-15T08:21:50+00:00"
  - type: "pm_response"
    notes: "Polymarket pricing at 5% on an Ethereum reserve reflects limited expectation that regulatory uncertainty resolution will escalate to formal government accumulation within the year."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "CoinDesk: SEC cancels long-awaited proposal of Reg Crypto, postponing meeting wi"
    url: "https://www.coindesk.com/policy/2026/08/13/sec-cancels-long-awaited-proposal-of-reg-crypto-postponing-meeting-without-new-date"
    published_at: "2026-08-14T08:20:52.293Z"
    retrieved_at: "2026-08-15T08:21:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
