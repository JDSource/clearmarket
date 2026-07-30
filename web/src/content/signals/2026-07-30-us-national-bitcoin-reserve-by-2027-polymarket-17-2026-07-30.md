---
signal_id: "CMSIG2026073008"
signal_slug: "us-national-bitcoin-reserve-by-2027-polymarket-17-2026-07-30"
headline: "US national Bitcoin reserve by 2027: Polymarket 17%"
semantic_title: "US national Bitcoin reserve by 2027 stays a long shot at 17 percent"
telemetry: "Polymarket 17%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-30T00:00:00.000Z"
event_id: "CM-EVT-0F2G0B8X49"
event_slug: "us-national-bitcoin-reserve-before-2027"
event_question: "Will the United States establish a national Bitcoin reserve before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x953b1439569eef0a0e639566acd35d32ebadee8ab70dbb2f8e00bb936a277aa2"
  question_raw: "US national Bitcoin reserve before 2027?"
  current_price: 0.17
  volume_24h_usd: 11.78
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market prices a 17% chance the United States establishes a national Bitcoin reserve before 2027."
  - "Moving seized crypto to Coinbase Prime raises fresh questions about liquidation intent, which is not consistent with a reserve-building narrative."
  - "The Kalshi contract on Trump creating a National Bitcoin Reserve in 2026 sits at 16%, closely mirroring the Polymarket reading across venues."
  - "Polymarket resolves via UMA oracle; establishing a reserve would require a formal executive or legislative action before the end of 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US government transferred nearly $300 million in seized Bitcoin and Ether to Coinbase Prime, reigniting debate over whether the administration intends to hold or liquidate the assets."
    publisher: "bitrss.com"
    published_at: "2026-07-30T00:00:00.000Z"
    source_url: "https://bitrss.com/us-govt-moves-244m-in-bitcoin-to-coinbase-did-trump-break-his-promise-231460"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bitrss.com"
        source_url: "https://bitrss.com/us-govt-moves-244m-in-bitcoin-to-coinbase-did-trump-break-his-promise-231460"
        retrieved_at: "2026-07-30T10:20:48+00:00"
  - type: "pm_response"
    notes: "Polymarket and Kalshi both price the reserve scenario near 16-17%, showing cross-venue agreement that the government transfer is not being read as a reserve-building signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bitrss.com: US Govt Moves $244M in Bitcoin to Coinbase: Did Trump Break His Promis"
    url: "https://bitrss.com/us-govt-moves-244m-in-bitcoin-to-coinbase-did-trump-break-his-promise-231460"
    published_at: "2026-07-30T00:00:00.000Z"
    retrieved_at: "2026-07-30T10:20:48+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
