---
signal_id: "CMSIG2026092001"
signal_slug: "fed-funds-upper-bound-4-0-4-25-kalshi-ladder-85-35-2026-09-20"
headline: "Fed funds upper bound 4.0-4.25%: Kalshi ladder 85/35%"
semantic_title: "Fed funds above 4 percent stays heavily favored after hike"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-20T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound following September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.35
  volume_24h_usd: 108.27
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the post-September Fed funds upper bound in the 4.00-4.25% range: 85% above 4.00%, collapsing to 35% above 4.25%."
  - "Multiple outlets confirm the Fed hiked a quarter-point at the September 16 meeting; the ladder distribution is fully consistent with a 25bp hike landing the rate at 4.00-4.25%."
  - "The 4.50% strike prices at just 1%, signaling the market sees near-zero chance the Fed delivered more than 25bp or will immediately hike again to that level."
  - "A companion Kalshi contract on a Fed rate cut greater than 25bp this year sits at 1%, reinforcing the one-and-done hike read from this ladder."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve raised its benchmark interest rate for the first time since 2023, with Bitcoin ETF inflows returning despite the hike."
    publisher: "walletinvestor.com"
    published_at: "2026-09-20T00:00:00.000Z"
    source_url: "https://walletinvestor.com/news/crypto-news/bitcoin-holds-above-80000-as-etf-inflows-return-and-altcoins-rally/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "walletinvestor.com"
        source_url: "https://walletinvestor.com/news/crypto-news/bitcoin-holds-above-80000-as-etf-inflows-return-and-altcoins-rally/"
        retrieved_at: "2026-09-20T07:47:17+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves against the Federal Reserve's official post-meeting rate announcement; the distribution tightly clusters around the 4.00-4.25% band consistent with a single 25bp hike."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "walletinvestor.com: Bitcoin Holds Above $80,000 as ETF Inflows Return and Altcoins Rally -"
    url: "https://walletinvestor.com/news/crypto-news/bitcoin-holds-above-80000-as-etf-inflows-return-and-altcoins-rally/"
    published_at: "2026-09-20T00:00:00.000Z"
    retrieved_at: "2026-09-20T07:47:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
