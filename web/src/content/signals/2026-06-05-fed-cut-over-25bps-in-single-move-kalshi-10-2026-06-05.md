---
signal_id: "CMSIG2026060501"
signal_slug: "fed-cut-over-25bps-in-single-move-kalshi-10-2026-06-05"
headline: "Fed cut over 25bps in single move: Kalshi 10%"
semantic_title: "Fed cut above 25 basis points priced near zero"
telemetry: "Kalshi 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-05T17:44:14.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve cut interest rates by more than 25 basis points in a single action this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.104
  volume_24h_usd: 26.64
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 10% probability that the Fed cuts by more than 25 basis points in any single meeting."
  - "Hot May jobs print of 172,000 is consistent with a market already skeptical of aggressive Fed easing."
  - "A 10% price on outsized cuts means the market sees the path as steady-hold or shallow-cut, not a pivot."
  - "Resolves via Federal Reserve official rate decision; any meeting where the cut exceeds 25bps triggers yes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May payrolls surged to 172,000, far above the 105,000 forecast, removing near-term Fed rate cut expectations and complicating new Chair Kevin Warsh's policy path."
    publisher: "Jeff Cox"
    published_at: "2026-06-05T17:44:14.000Z"
    source_url: "https://www.cnbc.com/2026/06/05/hot-jobs-report-puts-fed-cuts-further-out-of-reach-as-chair-warsh-faces-policy-tests.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/06/05/hot-jobs-report-puts-fed-cuts-further-out-of-reach-as-chair-warsh-faces-policy-tests.html"
        retrieved_at: "2026-06-07T10:26:16+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 10% aligns with post-jobs consensus that the Fed is on extended hold under Chair Kevin Warsh."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: Hot jobs report puts Fed cuts further out of reach as Chair Warsh face"
    url: "https://www.cnbc.com/2026/06/05/hot-jobs-report-puts-fed-cuts-further-out-of-reach-as-chair-warsh-faces-policy-tests.html"
    published_at: "2026-06-05T17:44:14.000Z"
    retrieved_at: "2026-06-07T10:26:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
