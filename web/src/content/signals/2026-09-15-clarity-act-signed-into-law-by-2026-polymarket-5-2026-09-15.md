---
signal_id: "CMSIG2026091508"
signal_slug: "clarity-act-signed-into-law-by-2026-polymarket-5-2026-09-15"
headline: "Clarity Act signed into law by 2026: Polymarket 5%"
semantic_title: "Clarity Act signed into law by 2026 stays a long shot"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-15T21:31:48.000Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act (H.R. 3633) be signed into law by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act (H.R.3633) signed into law in 2026?"
  current_price: 0.052
  volume_24h_usd: 3380295.477894998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "The Polymarket contract on the Clarity Act being signed into law by 2026 sits at just 5%, resolves via UMA oracle."
  - "The Senate's 49-50 procedural failure is consistent with the 5% pricing; the bill would need to clear the Senate and presidential signature before year-end."
  - "The Kalshi Senate Yea vote ladder confirms the market saw a sub-50 outcome as the most likely scenario before the vote was taken."
  - "The Polymarket contract resolves via UMA oracle on a signed-into-law outcome; Senate failure at the procedural stage makes House reconsideration or Senate reattempt the only remaining paths."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Clarity Act, the crypto industry's flagship market-structure bill, collapsed in a Senate procedural vote, failing to reach the 60-vote threshold needed to advance."
    publisher: "AFP  and  Reuters"
    published_at: "2026-09-15T21:31:48.000Z"
    source_url: "https://www.aljazeera.com/economy/2026/9/15/us-senate-crypto-bill-collapses-in-blow-to-industry"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AFP  and  Reuters"
        source_url: "https://www.aljazeera.com/economy/2026/9/15/us-senate-crypto-bill-collapses-in-blow-to-industry"
        retrieved_at: "2026-09-16T13:02:46+00:00"
  - type: "pm_response"
    notes: "Polymarket at 5% is consistent with the Senate failure; resolution requires the full legislative gauntlet, not just a Senate re-vote."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AFP  and  Reuters: US Senate crypto bill collapses in blow to industry | Crypto News | Al"
    url: "https://www.aljazeera.com/economy/2026/9/15/us-senate-crypto-bill-collapses-in-blow-to-industry"
    published_at: "2026-09-15T21:31:48.000Z"
    retrieved_at: "2026-09-16T13:02:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
