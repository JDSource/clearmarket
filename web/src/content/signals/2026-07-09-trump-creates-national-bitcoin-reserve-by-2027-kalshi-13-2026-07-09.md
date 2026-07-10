---
signal_id: "CMSIG2026070908"
signal_slug: "trump-creates-national-bitcoin-reserve-by-2027-kalshi-13-2026-07-09"
headline: "Trump creates National Bitcoin Reserve by 2027: Kalshi 13%"
semantic_title: "National Bitcoin Reserve creation skepticism holds at low odds"
telemetry: "Kalshi 13%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-09T00:00:00.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve before 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.13
  volume_24h_usd: 1.95
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market prices 13% on Trump creating a National Bitcoin Reserve before 2027, resolving via The New York Times."
  - "Growing political embrace of crypto globally has not shifted the market's skepticism: 87% implied probability that no formal US Bitcoin reserve is established this year."
  - "A companion Kalshi contract on crypto market structure legislation becoming law by 2027 sits at 39%, suggesting markets see regulatory framework as more likely than a direct sovereign reserve."
  - "Resolution requires New York Times confirmation of an official reserve creation; Bitcoin's 30% year-to-date decline and the current geopolitical risk environment are consistent with the low reserve probability."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin has lost more than half its value since its October 2025 peak yet cryptocurrency is spreading into politics, sanctions evasion, and global finance as politicians and sanctioned states embrace digital assets."
    publisher: "aljazeera.com"
    published_at: "2026-07-09T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/video/counting-the-cost/2026/7/9/why-is-the-cryptocurrency-market-slumping"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aljazeera.com"
        source_url: "https://www.aljazeera.com/video/counting-the-cost/2026/7/9/why-is-the-cryptocurrency-market-slumping"
        retrieved_at: "2026-07-10T10:49:37+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via The New York Times; the 13% price reflects market skepticism that political crypto enthusiasm translates into formal US sovereign reserve policy before year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aljazeera.com: Why are politicians and sanctioned states embracing crypto? | Crypto |"
    url: "https://www.aljazeera.com/video/counting-the-cost/2026/7/9/why-is-the-cryptocurrency-market-slumping"
    published_at: "2026-07-09T00:00:00.000Z"
    retrieved_at: "2026-07-10T10:49:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
