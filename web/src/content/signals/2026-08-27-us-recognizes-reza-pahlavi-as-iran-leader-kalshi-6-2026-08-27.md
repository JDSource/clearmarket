---
signal_id: "CMSIG2026082704"
signal_slug: "us-recognizes-reza-pahlavi-as-iran-leader-kalshi-6-2026-08-27"
headline: "US recognizes Reza Pahlavi as Iran leader: Kalshi 6%"
semantic_title: "Markets put long odds on US recognizing Reza Pahlavi as Iran leader"
telemetry: "Kalshi 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-27T00:00:00.000Z"
event_id: "CM-EVT-SY50TZ6672"
event_slug: "kxrecogpersoniran-26"
event_question: "Will the United States recognize Reza Pahlavi as the leader of Iran by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRECOGPERSONIRAN-26"
  question_raw: "Will the United States recognize Reza Pahlavi as the leader of Iran in 2026?"
  current_price: 0.061
  volume_24h_usd: 159.8
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices US recognition of Reza Pahlavi as Iran's leader at just 6%, with trading volume up over 23,000% day over day."
  - "The stalemate narrative is broadly consistent with the low probability: no regime change outcome is in sight despite six months of conflict."
  - "The companion Polymarket contract on the same question sits at 5%, showing near-identical cross-venue pricing with no meaningful gap."
  - "Both contracts resolve via ABC News reporting; the volume spike signals the stalemate story is drawing fresh speculative attention, not a pricing shift."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "After six months of war, the US-Iran conflict has reached a costly stalemate, with Trump shifting from airstrikes to economic warfare and Iran betting time is on its side."
    publisher: "Samia Nakhoul"
    published_at: "2026-08-27T00:00:00.000Z"
    source_url: "https://www.reuters.com/world/china/after-six-months-iran-war-has-reached-its-endgame-costly-stalemate-2026-08-27/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Samia Nakhoul"
        source_url: "https://www.reuters.com/world/china/after-six-months-iran-war-has-reached-its-endgame-costly-stalemate-2026-08-27/"
        retrieved_at: "2026-08-29T13:34:02+00:00"
  - type: "pm_response"
    notes: "Kalshi and Polymarket both at 5-6% on Pahlavi recognition, with Kalshi volume surging over 23,000% day over day as the stalemate narrative accelerates."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Samia Nakhoul: After six months, the Iran war has reached its endgame, a costly stal"
    url: "https://www.reuters.com/world/china/after-six-months-iran-war-has-reached-its-endgame-costly-stalemate-2026-08-27/"
    published_at: "2026-08-27T00:00:00.000Z"
    retrieved_at: "2026-08-29T13:34:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
