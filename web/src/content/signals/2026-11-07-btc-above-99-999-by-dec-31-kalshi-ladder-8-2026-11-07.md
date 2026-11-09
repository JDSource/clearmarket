---
signal_id: "CMSIG2026110707"
signal_slug: "btc-above-99-999-by-dec-31-kalshi-ladder-8-2026-11-07"
headline: "BTC above $99,999 by Dec 31: Kalshi ladder 8%"
semantic_title: "Bitcoin above $100K by year-end stays a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-07T00:00:00.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price above $100K by December 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.08
  volume_24h_usd: 1095.98
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "Kalshi ladder puts only 8% on Bitcoin exceeding $99,999 by December 31, 2026, with probabilities falling to 1-2% above $150K."
  - "Bitcoin's drop to around $73,700 on Democratic sweep concerns and macro uncertainty is consistent with the ladder's heavily bearish lean."
  - "The ladder's sharp probability drop above $110K implies the market sees very limited upside recovery potential through year-end."
  - "A separate Kalshi contract prices only 4% on Bitcoin's minimum price reaching a floor above zero before January 1, 2027, suggesting downside tail risk remains a live concern."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin fell to multi-month lows near $73,700 following the Democratic midterm sweep, Nvidia scandal headlines, and stalled Iran talks, with over $1 billion in liquidations."
    publisher: "theblock.co"
    published_at: "2026-11-07T00:00:00.000Z"
    source_url: "https://www.theblock.co/newsletters/the-daily/2026-11-07-treasury-mexc-crypto-401k-435962"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theblock.co"
        source_url: "https://www.theblock.co/newsletters/the-daily/2026-11-07-treasury-mexc-crypto-401k-435962"
        retrieved_at: "2026-11-09T07:47:40+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via CF Benchmarks; current spot near $74K leaves roughly a 35% gap to the $100K strike with less than two months remaining."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theblock.co: Treasury cuts off MEXC Global, crypto moves closer to 401(k) plans, an"
    url: "https://www.theblock.co/newsletters/the-daily/2026-11-07-treasury-mexc-crypto-401k-435962"
    published_at: "2026-11-07T00:00:00.000Z"
    retrieved_at: "2026-11-09T07:47:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
