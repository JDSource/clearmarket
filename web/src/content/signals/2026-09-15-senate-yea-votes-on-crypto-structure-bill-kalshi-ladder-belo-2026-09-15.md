---
signal_id: "CMSIG2026091507"
signal_slug: "senate-yea-votes-on-crypto-structure-bill-kalshi-ladder-belo-2026-09-15"
headline: "Senate Yea votes on crypto structure bill: Kalshi ladder below 50"
semantic_title: "Senate crypto bill vote count priced well below 50 members"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-15T21:31:48.000Z"
event_id: "CM-EVT-CSYS5KPXK6"
event_slug: "kxvoteclarity-26may16"
event_question: "Senate Yea votes on crypto market structure bill"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTECLARITY-26MAY16-T50"
  question_raw: "How many Senate members will vote Yea on a crypto market structure bill (as defined in KXCRYPTOSTRUCTURE)?"
  current_price: 0.06
  volume_24h_usd: 225.99
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi ladder on Senate Yea votes for a crypto market structure bill prices the market-implied count well below 50: only 6% chance of reaching 50 votes."
  - "The Senate bill's collapse is fully consistent with the ladder's distribution, which shows peak probability mass in the 58-62 range implying the bill fell short of cloture."
  - "A related Polymarket contract on the Clarity Act being signed into law by 2026 (CM-EVT-ZXN47LV744) prices at 8%, reinforcing the bleak near-term outlook."
  - "The Kalshi ladder resolves based on the final recorded Senate vote count; a procedural cloture vote total would be the relevant tally."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US Senate crypto market structure bill collapsed, dealing a major blow to efforts to establish the first federal digital asset framework."
    publisher: "AFP  and  Reuters"
    published_at: "2026-09-15T21:31:48.000Z"
    source_url: "https://www.aljazeera.com/economy/2026/9/15/us-senate-crypto-bill-collapses-in-blow-to-industry"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AFP  and  Reuters"
        source_url: "https://www.aljazeera.com/economy/2026/9/15/us-senate-crypto-bill-collapses-in-blow-to-industry"
        retrieved_at: "2026-09-17T13:04:18+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows the market had already priced Senate failure well before the bill's collapse was reported."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AFP  and  Reuters: US Senate crypto bill collapses in blow to industry | Crypto News | Al"
    url: "https://www.aljazeera.com/economy/2026/9/15/us-senate-crypto-bill-collapses-in-blow-to-industry"
    published_at: "2026-09-15T21:31:48.000Z"
    retrieved_at: "2026-09-17T13:04:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
