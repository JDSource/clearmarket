---
signal_id: "CMSIG2026112303"
signal_slug: "fed-cut-greater-than-25bp-in-2026-kalshi-2-2026-11-23"
headline: "Fed cut greater than 25bp in 2026: Kalshi 2%"
semantic_title: "Fed rate cut above 25 basis points this year stays a long shot"
telemetry: "Kalshi 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-23T20:27:01.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.018
  volume_24h_usd: 35.57
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market puts only 2% odds on the Fed cutting rates by more than 25 basis points at any point in 2026."
  - "Mixed inflation signals reported this week are not moving the needle toward aggressive cuts; at 2%, the market is effectively ruling out a jumbo cut."
  - "This aligns with the Kalshi ladder on the federal funds upper bound (CM-EVT-MR57HVWJT3), which clusters pricing firmly at 4.00-4.25%, leaving no room for significant near-term easing."
  - "Resolves via Federal Reserve official rate decision announcements; a surprise deterioration in labor or financial conditions is the main scenario that could shift this contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed is receiving conflicting signals, with cooler-than-expected CPI and PPI prints but persistent above-target inflation and strong growth keeping the door open to further hikes."
    publisher: "localtrusttx.com"
    published_at: "2026-11-23T20:27:01.000Z"
    source_url: "https://www.localtrusttx.com/resources/insights/articles/by-the-numbers_081426"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "localtrusttx.com"
        source_url: "https://www.localtrusttx.com/resources/insights/articles/by-the-numbers_081426"
        retrieved_at: "2026-11-25T07:47:45+00:00"
  - type: "pm_response"
    notes: "Kalshi contract on a Fed cut exceeding 25bp; at 2%, the market is firmly positioned against any aggressive easing in the current cycle."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "localtrusttx.com: By the Numbers: Fed receiving conflicting inflation and job market sig"
    url: "https://www.localtrusttx.com/resources/insights/articles/by-the-numbers_081426"
    published_at: "2026-11-23T20:27:01.000Z"
    retrieved_at: "2026-11-25T07:47:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
