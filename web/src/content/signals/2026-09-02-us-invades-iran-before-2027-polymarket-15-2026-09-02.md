---
signal_id: "CMSIG2026090207"
signal_slug: "us-invades-iran-before-2027-polymarket-15-2026-09-02"
headline: "US invades Iran before 2027: Polymarket 15%"
semantic_title: "Full US invasion of Iran before 2027 stays a long shot at 15%"
telemetry: "Polymarket 15%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-02T00:00:00.000Z"
event_id: "CM-EVT-WD982793G1"
event_slug: "will-the-us-invade-iran-before-2027"
event_question: "Will the U.S. invade Iran before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5db999fad322cea2914535aae5517060c3f80ad6d8c0231cde2124a434d16846"
  question_raw: "Will the U.S. invade Iran before 2027?"
  current_price: 0.15
  volume_24h_usd: 679620.8267169998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on a US invasion of Iran before 2027 sits at 15%, a long shot but non-trivial given the active military exchange."
  - "The current conflict involves airstrikes and base attacks, not a ground invasion; the market appears to distinguish between an air campaign and a full invasion at 15%."
  - "A companion Polymarket contract on the Iranian regime falling before 2027 sits at 7%, suggesting markets see the conflict as serious but not existential for Tehran."
  - "Resolution via UMA oracle; the contract likely requires ground forces or an explicit invasion declaration to resolve YES, not an expanded air campaign alone."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran launched retaliatory strikes on US bases throughout the Middle East after US CENTCOM strikes killed five people at a wedding, marking the biggest exchange since July."
    publisher: "Darryl Coote"
    published_at: "2026-09-02T00:00:00.000Z"
    source_url: "https://www.upi.com/Top_News/World-News/2026/09/02/iran-us-retalitory-strike/9321788328562/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Darryl Coote"
        source_url: "https://www.upi.com/Top_News/World-News/2026/09/02/iran-us-retalitory-strike/9321788328562/"
        retrieved_at: "2026-09-02T12:29:02+00:00"
  - type: "pm_response"
    notes: "Polymarket prices the invasion scenario at 15% and regime collapse at 7% simultaneously, implying the market sees neither outcome as likely even as active military strikes continue."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Darryl Coote: Iran attacks U.S. bases after CENTCOM strike kills 5 at wedding - UPI."
    url: "https://www.upi.com/Top_News/World-News/2026/09/02/iran-us-retalitory-strike/9321788328562/"
    published_at: "2026-09-02T00:00:00.000Z"
    retrieved_at: "2026-09-02T12:29:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
