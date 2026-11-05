---
signal_id: "CMSIG2026110505"
signal_slug: "clarity-act-signed-by-2026-polymarket-3-2026-11-05"
headline: "Clarity Act signed by 2026: Polymarket 3%"
semantic_title: "Clarity Act passage by 2026 stays a long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-05T14:24:41.000Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act (H.R. 3633) be signed into law by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act (H.R.3633) signed into law in 2026?"
  current_price: 0.031
  volume_24h_usd: 60578.864046
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "The Polymarket contract on the Clarity Act being signed into law by 2026 sits at 3%, pricing the bill as a near-certain failure under the new Democratic Congress."
  - "The news is fully consistent with the market: Democrats historically favor crypto oversight over deregulation, and the new majority is expected to deprioritize the bill."
  - "The companion Kalshi ladder on Senate Yea votes for a crypto market structure bill implies fewer than 50 votes, reinforcing the low-passage read."
  - "Resolves via Polymarket's UMA oracle; the question requires the bill to be signed into law, not merely passed one chamber, raising the resolution bar further."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Democratic sweep of the 2026 midterms is expected to shift Congress toward scrutinizing Trump's crypto dealings rather than advancing industry-friendly legislation like the Clarity Act."
    publisher: "Tanaya Macheel"
    published_at: "2026-11-05T14:24:41.000Z"
    source_url: "https://www.cnbc.com/2026/11/05/crypto-midterms-democrats-clarity-act.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Tanaya Macheel"
        source_url: "https://www.cnbc.com/2026/11/05/crypto-midterms-democrats-clarity-act.html"
        retrieved_at: "2026-11-05T16:02:36+00:00"
  - type: "pm_response"
    notes: "Polymarket at 3% is directionally aligned with the Democratic sweep narrative; the companion Senate vote ladder adds structural corroboration."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Tanaya Macheel: Crypto policy after Democrats sweep 2026 midterms"
    url: "https://www.cnbc.com/2026/11/05/crypto-midterms-democrats-clarity-act.html"
    published_at: "2026-11-05T14:24:41.000Z"
    retrieved_at: "2026-11-05T16:02:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
