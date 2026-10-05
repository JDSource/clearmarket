---
signal_id: "CMSIG2026100504"
signal_slug: "clarity-act-signed-into-law-by-2026-polymarket-5-2026-10-05"
headline: "Clarity Act signed into law by 2026: Polymarket 5%"
semantic_title: "Clarity Act signed into law stays a long shot"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-05T00:00:00.000Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act (H.R. 3633) be signed into law by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act (H.R.3633) signed into law in 2026?"
  current_price: 0.049
  volume_24h_usd: 295231.189378
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices the Clarity Act being signed into law by 2026 at just 5%, consistent with the Senate blocking it."
  - "The Senate vote against the CLARITY Act aligns with the market's near-zero probability; the pricing and the news are in agreement."
  - "Treasury's withdrawal of crypto surveillance rules is a separate regulatory concession that does not rescue the broader legislative framework."
  - "Resolution via Polymarket's uma_oracle; the contract requires a presidential signature by end of 2026, a bar the Senate block makes near-impossible this year."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US Senate blocked the CLARITY Act and the US Treasury separately withdrew proposed crypto surveillance rules on unhosted wallets and mixing."
    publisher: "John Chen"
    published_at: "2026-10-05T00:00:00.000Z"
    source_url: "https://cryptobriefing.com/us-treasury-withdraws-crypto-surveillance-rules/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "John Chen"
        source_url: "https://cryptobriefing.com/us-treasury-withdraws-crypto-surveillance-rules/"
        retrieved_at: "2026-10-05T16:44:30+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 5% is the only priced candidate; the companion Bitcoin-drop story (Story 32) provides corroborating market context."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "John Chen: US Treasury withdraws proposed crypto surveillance rules on unhosted w"
    url: "https://cryptobriefing.com/us-treasury-withdraws-crypto-surveillance-rules/"
    published_at: "2026-10-05T00:00:00.000Z"
    retrieved_at: "2026-10-05T16:44:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
