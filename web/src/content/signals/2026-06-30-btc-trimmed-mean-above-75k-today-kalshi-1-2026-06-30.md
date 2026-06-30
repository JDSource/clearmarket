---
signal_id: "CMSIG2026063002"
signal_slug: "btc-trimmed-mean-above-75k-today-kalshi-1-2026-06-30"
headline: "BTC trimmed mean above $75K today: Kalshi 1%"
semantic_title: "BTC above $75K by June 30 sits at near-zero pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-30T10:46:42.000Z"
event_id: "CM-EVT-3MXSH7KHK5"
event_slug: "kxbtcmaxmon-btc-26jun30"
event_question: "BTC trimmed mean above $75K by Jun 30 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26JUN30-7500000"
  question_raw: "Will BTC trimmed mean be above $75000.00 by 11:59 PM ET on Jun 30, 2026?"
  current_price: 0.01
  volume_24h_usd: 29.37
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi ladder prices less than 1% at every strike from $75K to $92.5K for today's BTC trimmed mean, implying current price well below $75K."
  - "Bitcoin breaking the 200-week moving average is consistent with the near-zero probability across the entire upside ladder for June 30."
  - "The year-end Kalshi contract at 15% above $100K (CM-EVT-0MWN62PNG9) shows the market sees the near-term damage as a longer-horizon drag."
  - "Resolves via CF Benchmarks trimmed mean at 11:59 PM ET on June 30, 2026; any intraday recovery above $75K would be a significant surprise at current pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin slipped below its 200-week moving average over the weekend, trading around $60,238, turning a key cycle-support marker into an active demand test."
    publisher: "bitrss.com"
    published_at: "2026-06-30T10:46:42.000Z"
    source_url: "https://bitrss.com/bitcoin-just-slipped-below-the-bear-market-line-traders-cannot-ignore-226083"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bitrss.com"
        source_url: "https://bitrss.com/bitcoin-just-slipped-below-the-bear-market-line-traders-cannot-ignore-226083"
        retrieved_at: "2026-06-30T10:54:27+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves same-day via CF Benchmarks; the entire strike ladder at 1% or below makes this one of the most one-sided current-day crypto prints available."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bitrss.com: Bitcoin just slipped below the bear-market line traders cannot ignore"
    url: "https://bitrss.com/bitcoin-just-slipped-below-the-bear-market-line-traders-cannot-ignore-226083"
    published_at: "2026-06-30T10:46:42.000Z"
    retrieved_at: "2026-06-30T10:54:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
