---
signal_id: "CMSIG2026081107"
signal_slug: "clarity-act-signed-by-2026-polymarket-17-2026-08-11"
headline: "Clarity Act signed by 2026: Polymarket 17%"
semantic_title: "Clarity Act signed into law in 2026 stays a long shot"
telemetry: "Polymarket 17%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-11T09:06:42.685Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act (H.R. 3633) be signed into law by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act (H.R.3633) signed into law in 2026?"
  current_price: 0.17
  volume_24h_usd: 340005.178578
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices a 17% chance the CLARITY Act is signed into law by the end of 2026, keeping it a clear long shot."
  - "SEC proposing Regulation Crypto adds regulatory momentum, but the Polymarket contract shows markets do not treat this as a near-term legislative lock."
  - "The Senate yea-vote ladder (CM-EVT-CSYS5KPXK6) implying sub-50 votes reinforces the 17% full-enactment price; passage and signature are two separate hurdles."
  - "Resolves via Polymarket's UMA oracle; the contract requires presidential signature by December 31, 2026, not just Senate passage."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The SEC moved toward proposing its Regulation Crypto framework, adding regulatory momentum to the broader digital asset legislative push including the CLARITY Act."
    publisher: "Yevheny Serhiienko"
    published_at: "2026-08-11T09:06:42.685Z"
    source_url: "https://bitcoinfoundation.org/news/regulation/sec-moves-toward-landmark-regulation-crypto-framework-for-digital-asset-offerings/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yevheny Serhiienko"
        source_url: "https://bitcoinfoundation.org/news/regulation/sec-moves-toward-landmark-regulation-crypto-framework-for-digital-asset-offerings/"
        retrieved_at: "2026-08-12T09:07:43+00:00"
  - type: "pm_response"
    notes: "Polymarket is the venue; the 17% price sits well below a coin flip, consistent with the Senate vote count distribution showing likely failure to reach 60."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yevheny Serhiienko: SEC Moves Toward Landmark ‘Regulation Crypto’ Framework for Digital As"
    url: "https://bitcoinfoundation.org/news/regulation/sec-moves-toward-landmark-regulation-crypto-framework-for-digital-asset-offerings/"
    published_at: "2026-08-11T09:06:42.685Z"
    retrieved_at: "2026-08-12T09:07:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
