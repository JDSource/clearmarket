---
signal_id: "CMSIG2026102408"
signal_slug: "solana-above-150-by-jan-1-2027-ladder-implies-below-150-2026-10-24"
headline: "Solana above $150 by Jan 1 2027: ladder implies below $150"
semantic_title: "Solana above $150 before year-end stays below 25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-24T00:00:00.000Z"
event_id: "CM-EVT-L4YY954KX3"
event_slug: "kxsolmaxy-27jan01"
event_question: "Solana spot price ceiling, January 1 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSOLMAXY-27JAN01-150"
  question_raw: "Will the spot price of Solana be above $150.00 before Jan 1, 2027 at 12:00 AM ET?"
  current_price: 0.25
  volume_24h_usd: 54.98
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Prediction market ladder prices only 25% on Solana reaching above $150 before January 1, 2027, with spot near $100.83."
  - "The ladder distribution falls rapidly from 25% at $150 to 17% at $160 and 11% at $170, implying the market sees sub-$150 as the base case."
  - "A companion Kalshi contract (CM-EVT-1TG94NXKV4) puts only 2% on Solana ending 2026 above $500, consistent with the ladder's bearish upper-end pricing."
  - "Resolves via the stated ladder mechanism; the $100 current spot level means a 50% price move is needed just to reach the 25% strike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "HSBC launched its RedCoin Hong Kong dollar stablecoin for retail users, while Solana spot prices traded near $100.83 amid broad crypto weakness."
    publisher: "theblock.co"
    published_at: "2026-10-24T00:00:00.000Z"
    source_url: "https://www.theblock.co/newsletters/the-daily/2026-10-24-hsbc-stablecoin-more-crypto-news-428396"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theblock.co"
        source_url: "https://www.theblock.co/newsletters/the-daily/2026-10-24-hsbc-stablecoin-more-crypto-news-428396"
        retrieved_at: "2026-10-26T07:47:50+00:00"
  - type: "pm_response"
    notes: "Ladder contract (unspecified venue); the full distribution strongly implies the market consensus is for Solana to finish 2026 well below $150."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theblock.co: HSBC's RedCoin stablecoin goes live, and more crypto news"
    url: "https://www.theblock.co/newsletters/the-daily/2026-10-24-hsbc-stablecoin-more-crypto-news-428396"
    published_at: "2026-10-24T00:00:00.000Z"
    retrieved_at: "2026-10-26T07:47:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
