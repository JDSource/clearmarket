---
signal_id: "CMSIG2026080306"
signal_slug: "btc-above-100k-by-sep-1-kalshi-ladder-under-11-2026-08-03"
headline: "BTC above $100K by Sep 1: Kalshi ladder under 11%"
semantic_title: "Bitcoin above $100K by September stays a heavy long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-03T08:54:30.000Z"
event_id: "CM-EVT-ZPMYBGJP99"
event_slug: "kxbtcmax100-26"
event_question: "Bitcoin price above $100,000 by September 1, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAX100-26-AUG"
  question_raw: "Will Bitcoin be above $100000.00 by Sep 1, 2026 at 12:00AMET?"
  current_price: 0.03
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-10-01T04:00:00Z"
bullets:
  - "Kalshi ladder prices Bitcoin above $100K by September 1 at just 3-11% across the ladder's top strikes, a heavy long shot."
  - "Carry-trade unwind fears and yen intervention pledges add macro headwinds to crypto, broadly consistent with the sub-11% ceiling odds."
  - "A concurrent Bitcoin death-cross signal (20-week EMA crossing below 200-week EMA) reinforces the bearish technical backdrop already embedded in low ladder probabilities."
  - "The longer-horizon ladder (CM-EVT-0MWN62PNG9, by Dec 31) prices $100K at only 13%, showing the market sees persistent downside risk well beyond September."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin fell on carry-trade unwind fears as U.S. Treasury Secretary pledged further yen intervention."
    publisher: "Varinder Singh"
    published_at: "2026-08-03T08:54:30.000Z"
    source_url: "https://coingape.com/bitcoin-falls-carry-trade-unwind-fears-us-treasury-sec-pledges-further-yen-intervention/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Varinder Singh"
        source_url: "https://coingape.com/bitcoin-falls-carry-trade-unwind-fears-us-treasury-sec-pledges-further-yen-intervention/"
        retrieved_at: "2026-08-03T11:18:40+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on September 1 threshold; the December 31 companion ladder confirms the sub-$100K consensus is not a short-term artifact."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Varinder Singh: Bitcoin Falls on Carry Trade Unwind Fears as US Treasury Sec Pledges F"
    url: "https://coingape.com/bitcoin-falls-carry-trade-unwind-fears-us-treasury-sec-pledges-further-yen-intervention/"
    published_at: "2026-08-03T08:54:30.000Z"
    retrieved_at: "2026-08-03T11:18:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
