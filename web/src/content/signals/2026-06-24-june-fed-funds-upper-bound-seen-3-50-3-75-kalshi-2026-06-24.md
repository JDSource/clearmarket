---
signal_id: "CMSIG2026062401"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-24"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound consensus anchors at 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T01:30:39.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound following June 2026 FOMC"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 3.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi pins the Fed funds upper bound in the 3.50-3.75% range: 95% above 3.50%, but only 36% above 3.75%."
  - "Warsh's post-meeting statement emphasizing price stability aligns with the market holding the upper bound well above pre-Warsh levels."
  - "The sharp drop from 95% to 36% between 3.50% and 3.75% signals the market sees 3.50% as the near-certain floor, with the next hike as a live but minority bet."
  - "A companion Kalshi ladder (CM-EVT-PHWX2H6DM5) shows near-identical structure at 90% above 3.50% and 13% above 3.75%, confirming cross-contract consistency."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh held rates steady and signaled stronger inflation concerns, with outside news sources citing 77% rate-hike odds."
    publisher: "Kevin Helms"
    published_at: "2026-06-24T01:30:39.000Z"
    source_url: "https://news.bitcoin.com/cryptos-liquidity-outlook-darkens-as-fed-hawkish-pivot-pushes-hike-odds-to-77/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kevin Helms"
        source_url: "https://news.bitcoin.com/cryptos-liquidity-outlook-darkens-as-fed-hawkish-pivot-pushes-hike-odds-to-77/"
        retrieved_at: "2026-06-24T10:45:49+00:00"
  - type: "pm_response"
    notes: "Two Kalshi Fed funds ladders (CM-EVT-4ZQLQPNH91 and CM-EVT-PHWX2H6DM5) show tightly aligned distributions, reinforcing the 3.50-3.75% consensus read."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kevin Helms: Crypto's Liquidity Outlook Darkens as Fed Hawkish Pivot Pushes Hike Od"
    url: "https://news.bitcoin.com/cryptos-liquidity-outlook-darkens-as-fed-hawkish-pivot-pushes-hike-odds-to-77/"
    published_at: "2026-06-24T01:30:39.000Z"
    retrieved_at: "2026-06-24T10:45:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
