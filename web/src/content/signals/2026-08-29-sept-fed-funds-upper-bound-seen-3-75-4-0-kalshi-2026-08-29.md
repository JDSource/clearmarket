---
signal_id: "CMSIG2026082901"
signal_slug: "sept-fed-funds-upper-bound-seen-3-75-4-0-kalshi-2026-08-29"
headline: "Sept Fed funds upper bound seen 3.75-4.0%: Kalshi"
semantic_title: "Fed funds above 4 percent after September stays a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-29T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound after September 2026 FOMC"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.37
  volume_24h_usd: 0.37
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the post-September Fed funds upper bound in the 3.75-4.0% range: 93% chance above 3.50%, but only 37% above 4.0%."
  - "Warsh's hawkish Jackson Hole speech is partially consistent with the pricing: markets see a hike as plausible but not the base case, stopping well short of a full 4%-plus scenario."
  - "The 75% probability above 3.75% suggests the market is pricing roughly one additional hike from the current hold, not the multi-hike cycle Warsh's language could imply."
  - "A companion Kalshi ladder (CM-EVT-6BS28TS762) shows nearly identical distribution, 95% above 3.50% but only 6% above 4.0%, reinforcing the single-hike consensus read."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh signaled at Jackson Hole that rate hikes may be needed if above-target inflation persists, raising stakes for the September FOMC meeting."
    publisher: "pbs.org"
    published_at: "2026-08-29T00:00:00.000Z"
    source_url: "https://www.pbs.org/newshour/economy/warsh-raises-stakes-for-feds-next-meeting-and-other-takeaways-from-jackson-hole-conference"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pbs.org"
        source_url: "https://www.pbs.org/newshour/economy/warsh-raises-stakes-for-feds-next-meeting-and-other-takeaways-from-jackson-hole-conference"
        retrieved_at: "2026-08-31T15:47:21+00:00"
  - type: "pm_response"
    notes: "Two near-identical Kalshi ladders on the September outcome show consistent distribution, giving high confidence in the market-implied 3.75-4.0% central tendency."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pbs.org: Warsh raises stakes for Fed's next meeting, and other takeaways from J"
    url: "https://www.pbs.org/newshour/economy/warsh-raises-stakes-for-feds-next-meeting-and-other-takeaways-from-jackson-hole-conference"
    published_at: "2026-08-29T00:00:00.000Z"
    retrieved_at: "2026-08-31T15:47:21+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
