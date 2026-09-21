---
signal_id: "CMSIG2026092008"
signal_slug: "clarity-act-signed-into-law-by-2026-polymarket-8-2026-09-20"
headline: "CLARITY Act signed into law by 2026: Polymarket 8%"
semantic_title: "CLARITY Act signed into law in 2026 stays long odds at 8 percent"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-09-20T00:00:00.000Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act (H.R. 3633) be signed into law by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act (H.R.3633) signed into law in 2026?"
  current_price: 0.077
  volume_24h_usd: 188430.307224
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices only 8% on the CLARITY Act being signed into law by 2026, consistent with its Senate failure and no clear path to revival before year-end."
  - "The bill's collapse in a 49-50 cloture vote is a hard structural barrier; the market's 8% reflects near-zero legislative runway in the remaining 2026 calendar."
  - "The CFTC's pivot to rulemaking via existing authority signals regulators do not expect legislative rescue, reinforcing the market's lean against passage."
  - "Resolution requires the bill to be signed into law by end of 2026; the Senate cloture failure makes that mechanically very difficult without a new vote and a changed coalition."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The CLARITY Act failed a 49-50 Senate cloture vote on September 15, 2026, with Democrats withdrawing support, after which the CFTC filed two new crypto rulemakings through existing statutory authority."
    publisher: "startupfortune.com"
    published_at: "2026-09-20T00:00:00.000Z"
    source_url: "https://startupfortune.com/the-cftc-is-writing-crypto-rules-the-senate-just-refused-to-pass/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "startupfortune.com"
        source_url: "https://startupfortune.com/the-cftc-is-writing-crypto-rules-the-senate-just-refused-to-pass/"
        retrieved_at: "2026-09-21T07:47:18+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on enacted law; the 8% price is directionally consistent with the bill's confirmed Senate defeat on September 15."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "startupfortune.com: The CFTC Is Writing Crypto Rules the Senate Just Refused to Pass - Sta"
    url: "https://startupfortune.com/the-cftc-is-writing-crypto-rules-the-senate-just-refused-to-pass/"
    published_at: "2026-09-20T00:00:00.000Z"
    retrieved_at: "2026-09-21T07:47:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
