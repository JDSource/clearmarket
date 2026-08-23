---
signal_id: "CMSIG2026082305"
signal_slug: "senate-clarity-act-yea-votes-ladder-below-50-2026-08-23"
headline: "Senate Clarity Act Yea votes: ladder below 50"
semantic_title: "Senate crypto bill vote count stays below 50 in early pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-23T01:22:06.000Z"
event_id: "CM-EVT-CSYS5KPXK6"
event_slug: "kxvoteclarity-26may16"
event_question: "Senate Yea votes on crypto market structure bill"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTECLARITY-26MAY16-T50"
  question_raw: "How many Senate members will vote Yea on a crypto market structure bill (as defined in KXCRYPTOSTRUCTURE)?"
  current_price: 0.41
  volume_24h_usd: 5.33
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Ladder pricing puts the Senate Yea vote count below 50: 41% chance at or above 50, 40% at 55 or above, falling to 8% at 66 or above."
  - "Bitcoin's surge past $79,000 reflects optimism on the Clarity Act, but the vote-count ladder shows the market has not priced a supermajority outcome."
  - "The 41% at 50-plus Yea votes means passage probability on a simple majority is roughly even, markets are not treating Clarity Act passage as a done deal."
  - "The National Bitcoin Reserve Kalshi contract sits at just 5%, suggesting markets separate crypto regulatory optimism from full-scale government Bitcoin accumulation."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin surged past $79,000 as Washington and Wall Street pushed the Clarity Act crypto regulation bill toward a final vote."
    publisher: "John Marshall"
    published_at: "2026-08-23T01:22:06.000Z"
    source_url: "https://www.webpronews.com/bitcoins-sudden-surge-past-79000-shows-how-washington-and-wall-street-can-still-move-markets/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "John Marshall"
        source_url: "https://www.webpronews.com/bitcoins-sudden-surge-past-79000-shows-how-washington-and-wall-street-can-still-move-markets/"
        retrieved_at: "2026-08-23T08:24:02+00:00"
  - type: "pm_response"
    notes: "Ladder distribution shows sharp drop-off above 60 Yea votes; resolution depends on a recorded Senate floor vote count."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "John Marshall: Bitcoin's Sudden Surge Past $79,000 Shows How Washington and Wall Stre"
    url: "https://www.webpronews.com/bitcoins-sudden-surge-past-79000-shows-how-washington-and-wall-street-can-still-move-markets/"
    published_at: "2026-08-23T01:22:06.000Z"
    retrieved_at: "2026-08-23T08:24:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
