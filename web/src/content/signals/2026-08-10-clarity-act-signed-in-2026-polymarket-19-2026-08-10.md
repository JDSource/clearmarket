---
signal_id: "CMSIG2026081006"
signal_slug: "clarity-act-signed-in-2026-polymarket-19-2026-08-10"
headline: "CLARITY Act signed in 2026: Polymarket 19%"
semantic_title: "CLARITY Act signed into law in 2026 stays a long shot"
telemetry: "Polymarket 19%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-10T12:48:25.168Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act (H.R. 3633) be signed into law by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act (H.R.3633) signed into law in 2026?"
  current_price: 0.19
  volume_24h_usd: 856676.9097640001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices the CLARITY Act being signed into law in 2026 at 19%, a clear long-shot read."
  - "Trading volume on this Polymarket contract surged 1,787% day over day, reflecting a flood of fresh activity after the Senate delay announcement."
  - "The Kalshi Senate vote-count ladder (CM-EVT-CSYS5KPXK6) implies fewer than 50 Yea votes, consistent with passage risk: 37% at 50 votes, falling sharply above."
  - "The September 15 procedural vote is a hard gate; failure there would almost certainly push the probability to single digits for the 2026 deadline."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Senate Majority Leader John Thune pushed the CLARITY Act Senate vote to September 15, dimming hopes for 2026 passage."
    publisher: "Yuri Molchan"
    published_at: "2026-08-10T12:48:25.168Z"
    source_url: "https://bitcoinfoundation.org/news/regulation/congress-crypto-bill-delay-clarity-act-vote-pushed-to-september-as-2026-passage-hopes-fade/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yuri Molchan"
        source_url: "https://bitcoinfoundation.org/news/regulation/congress-crypto-bill-delay-clarity-act-vote-pushed-to-september-as-2026-passage-hopes-fade/"
        retrieved_at: "2026-08-11T08:49:29+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 1,787% volume surge confirms the delay news drove sharp new attention to this contract."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yuri Molchan: Congress Crypto Bill Delay: CLARITY Act Vote Pushed to September as 20"
    url: "https://bitcoinfoundation.org/news/regulation/congress-crypto-bill-delay-clarity-act-vote-pushed-to-september-as-2026-passage-hopes-fade/"
    published_at: "2026-08-10T12:48:25.168Z"
    retrieved_at: "2026-08-11T08:49:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
