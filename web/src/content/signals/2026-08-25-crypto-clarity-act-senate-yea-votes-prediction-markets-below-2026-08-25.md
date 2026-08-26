---
signal_id: "CMSIG2026082506"
signal_slug: "crypto-clarity-act-senate-yea-votes-prediction-markets-below-2026-08-25"
headline: "Crypto Clarity Act Senate yea votes: prediction markets below 50"
semantic_title: "Crypto bill Senate vote count odds stay below 50 votes"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-25T20:37:04.193Z"
event_id: "CM-EVT-CSYS5KPXK6"
event_slug: "kxvoteclarity-26may16"
event_question: "Senate yea votes on crypto market structure bill"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTECLARITY-26MAY16-T50"
  question_raw: "How many Senate members will vote Yea on a crypto market structure bill (as defined in KXCRYPTOSTRUCTURE)?"
  current_price: 0.35
  volume_24h_usd: 76.46
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The prediction market ladder implies fewer than 50 Senate yea votes on the crypto market structure bill, with only 35% probability above 50 votes and 22% above 55."
  - "Trading volume surged 21,158% day-over-day, by far the largest volume spike in this batch, reflecting heavy fresh positioning ahead of the September 15 procedural vote."
  - "The 35%-at-50 versus 22%-at-55 gap shows the market does not expect the bill to clear the 60-vote cloture threshold, making passage a long shot."
  - "South Korea's parallel digital asset law announcement adds international regulatory context, but the US market is pricing domestic Senate arithmetic, not global momentum."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Digital Asset Market Clarity Act faces a procedural Senate vote on September 15, with Kalshi traders signaling low likelihood it reaches the 60-vote threshold needed."
    publisher: "Ananya Chetia"
    published_at: "2026-08-25T20:37:04.193Z"
    source_url: "https://www.cnbc.com/2026/08/25/kalshi-traders-see-low-likelihood-of-major-crypto-bill-becoming-law-this-year.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ananya Chetia"
        source_url: "https://www.cnbc.com/2026/08/25/kalshi-traders-see-low-likelihood-of-major-crypto-bill-becoming-law-this-year.html"
        retrieved_at: "2026-08-26T08:38:02+00:00"
  - type: "pm_response"
    notes: "Prediction market volume exploded 212.6x day-over-day on the Senate crypto vote count ladder, with the distribution firmly implying failure to reach 60 votes."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ananya Chetia: Kalshi traders see low likelihood of major crypto bill becoming law th"
    url: "https://www.cnbc.com/2026/08/25/kalshi-traders-see-low-likelihood-of-major-crypto-bill-becoming-law-this-year.html"
    published_at: "2026-08-25T20:37:04.193Z"
    retrieved_at: "2026-08-26T08:38:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
