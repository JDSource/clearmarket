---
signal_id: "CMSIG2026082901"
signal_slug: "fed-funds-upper-bound-post-meeting-seen-3-75-4-0-kalshi-2026-08-29"
headline: "Fed funds upper bound post-meeting seen 3.75-4.0%: Kalshi"
semantic_title: "Markets put long odds on Fed rate above 4 percent after next meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-29T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Fed funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 62.74
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound in the 3.75-4.00% range post-meeting, with 59% above 3.75% but only 10% above 4.00%."
  - "Warsh's hawkish Jackson Hole posture is consistent with the ladder moving above the 3.75% strike, but the market stops well short of pricing a hike above 4.00%, suggesting limited conviction on an aggressive move; trading volume surged 50x day-over-day, signaling sharp fresh attention."
  - "The companion Kalshi ladder for a later meeting (CM-EVT-MR57HVWJT3) puts 66% above 3.75% and 32% above 4.00%, implying the market sees a slightly higher ceiling further out on the curve."
  - "Resolution turns on the official FOMC statement rate announcement; any language softening the hike bias would collapse the above-3.75% probability rapidly."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh raised the stakes at Jackson Hole, signaling rates may need to rise if above-target inflation persists."
    publisher: "pbs.org"
    published_at: "2026-08-29T00:00:00.000Z"
    source_url: "https://www.pbs.org/newshour/economy/warsh-raises-stakes-for-feds-next-meeting-and-other-takeaways-from-jackson-hole-conference"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pbs.org"
        source_url: "https://www.pbs.org/newshour/economy/warsh-raises-stakes-for-feds-next-meeting-and-other-takeaways-from-jackson-hole-conference"
        retrieved_at: "2026-08-30T13:30:27+00:00"
  - type: "pm_response"
    notes: "Kalshi volume up 50x day-over-day on this contract; the distribution clusters tightly in the 3.75-4.00% range, well below what a full hike cycle would imply."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pbs.org: Warsh raises stakes for Fed's next meeting, and other takeaways from J"
    url: "https://www.pbs.org/newshour/economy/warsh-raises-stakes-for-feds-next-meeting-and-other-takeaways-from-jackson-hole-conference"
    published_at: "2026-08-29T00:00:00.000Z"
    retrieved_at: "2026-08-30T13:30:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
