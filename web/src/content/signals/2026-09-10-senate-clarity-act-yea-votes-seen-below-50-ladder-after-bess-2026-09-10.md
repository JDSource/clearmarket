---
signal_id: "CMSIG2026091007"
signal_slug: "senate-clarity-act-yea-votes-seen-below-50-ladder-after-bess-2026-09-10"
headline: "Senate Clarity Act yea votes seen below 50: ladder after Bessent push"
semantic_title: "Senate Clarity Act vote count priced below 50 yes votes"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-10T04:38:43.642Z"
event_id: "CM-EVT-CSYS5KPXK6"
event_slug: "kxvoteclarity-26may16"
event_question: "Senate yea votes on crypto market structure bill"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTECLARITY-26MAY16-T50"
  question_raw: "How many Senate members will vote Yea on a crypto market structure bill (as defined in KXCRYPTOSTRUCTURE)?"
  current_price: 0.39
  volume_24h_usd: 1142.79
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Senate vote-count ladder prices the Clarity Act below 50 yea votes: only 39% above 50, 29% above 55, and single digits above 62."
  - "Despite Bessent's public push and Armstrong's optimism, the market assigns a majority probability to the bill falling short of the 50-vote threshold needed for passage."
  - "Coinbase CEO Brian Armstrong said senators he has spoken with are on board, but the ladder's sub-50 center of gravity suggests the market views floor dynamics as far less certain than the lobbying narrative implies."
  - "The Polymarket contract on the Clarity Act being signed into law by 2026 sits at just 16%, consistent with the vote-count ladder's pessimistic read on the path through both chambers and to the White House."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Treasury Secretary Scott Bessent urged Senate passage of the Clarity Act after the Senate returned from recess, while Coinbase CEO Brian Armstrong said the bill is ready for a yes vote."
    publisher: "investingLive"
    published_at: "2026-09-10T04:38:43.642Z"
    source_url: "https://investinglive.com/cryptocurrency/clarity-act-why-washington-could-be-crypto-s-biggest-september-catalyst/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investingLive"
        source_url: "https://investinglive.com/cryptocurrency/clarity-act-why-washington-could-be-crypto-s-biggest-september-catalyst/"
        retrieved_at: "2026-09-10T12:39:52+00:00"
  - type: "pm_response"
    notes: "The vote-count ladder resolves on the official Senate roll-call tally; the 16% Polymarket law-passage contract reflects the sequential hurdles of Senate passage, House concurrence, and presidential signature."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investingLive: CLARITY Act: Why Washington could be crypto’s biggest September cataly"
    url: "https://investinglive.com/cryptocurrency/clarity-act-why-washington-could-be-crypto-s-biggest-september-catalyst/"
    published_at: "2026-09-10T04:38:43.642Z"
    retrieved_at: "2026-09-10T12:39:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
