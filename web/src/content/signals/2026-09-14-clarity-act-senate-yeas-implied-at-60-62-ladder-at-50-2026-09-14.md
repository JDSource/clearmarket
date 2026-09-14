---
signal_id: "CMSIG2026091406"
signal_slug: "clarity-act-senate-yeas-implied-at-60-62-ladder-at-50-2026-09-14"
headline: "Clarity Act Senate yeas implied at 60-62: ladder at 50%"
semantic_title: "Senate yea votes on crypto bill priced right at the 60-vote line"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-14T00:00:00.000Z"
event_id: "CM-EVT-CSYS5KPXK6"
event_slug: "kxvoteclarity-26may16"
event_question: "Senate yea votes on crypto market structure bill"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTECLARITY-26MAY16-T62"
  question_raw: "How many Senate members will vote Yea on a crypto market structure bill (as defined in KXCRYPTOSTRUCTURE)?"
  current_price: 0.25
  volume_24h_usd: 0.45
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Ladder prices 50% above 60 yea votes and only 25% above 62, putting the market-implied vote count right on the cloture knife-edge."
  - "Final text release with ethics provisions is consistent with last-minute vote-gathering; the market has not broken clearly above the 60-vote threshold."
  - "The 64% probability above 55 votes versus 50% above 60 shows the market expects votes in the high 50s to low 60s as the modal outcome."
  - "Polymarket law-by-2026 contract (CM-EVT-ZXN47LV744) at 29% reflects that clearing cloture still leaves House passage and presidential signature as hurdles."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Senators Lummis, Boozman, and Scott released the final Clarity Act text late Sunday ahead of Tuesday's cloture vote, incorporating a Trump-backed ethics deal."
    publisher: "cryptotimes.io"
    published_at: "2026-09-14T00:00:00.000Z"
    source_url: "https://www.cryptotimes.io/2026/09/14/senate-unveils-final-clarity-act-text-with-trump-backed-ethics-deal-ahead-of-tuesday-cloture-vote/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cryptotimes.io"
        source_url: "https://www.cryptotimes.io/2026/09/14/senate-unveils-final-clarity-act-text-with-trump-backed-ethics-deal-ahead-of-tuesday-cloture-vote/"
        retrieved_at: "2026-09-14T14:41:02+00:00"
  - type: "pm_response"
    notes: "Ladder resolves via official Senate roll-call vote records; threshold of 60 is the cloture requirement under Senate procedure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cryptotimes.io: Senate Unveils Final CLARITY Act Text With Trump-Backed Ethics Deal Ah"
    url: "https://www.cryptotimes.io/2026/09/14/senate-unveils-final-clarity-act-text-with-trump-backed-ethics-deal-ahead-of-tuesday-cloture-vote/"
    published_at: "2026-09-14T00:00:00.000Z"
    retrieved_at: "2026-09-14T14:41:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
