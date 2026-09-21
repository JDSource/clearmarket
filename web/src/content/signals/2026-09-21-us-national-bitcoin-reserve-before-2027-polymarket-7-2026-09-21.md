---
signal_id: "CMSIG2026092107"
signal_slug: "us-national-bitcoin-reserve-before-2027-polymarket-7-2026-09-21"
headline: "US national Bitcoin reserve before 2027: Polymarket 7%"
semantic_title: "US national Bitcoin reserve before 2027 stays a long shot at 7 percent"
telemetry: "Polymarket 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-21T00:00:00.000Z"
event_id: "CM-EVT-0F2G0B8X49"
event_slug: "us-national-bitcoin-reserve-before-2027"
event_question: "Will the United States establish a national Bitcoin reserve before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x953b1439569eef0a0e639566acd35d32ebadee8ab70dbb2f8e00bb936a277aa2"
  question_raw: "US national Bitcoin reserve before 2027?"
  current_price: 0.07
  volume_24h_usd: 1239.31
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices just 7% on the United States formally establishing a national Bitcoin reserve before 2027, keeping this a heavy long shot despite committee progress."
  - "The House panel advance is a procedural step, not enactment; the market's low probability is consistent with the long distance between committee approval and signed law."
  - "A Kalshi contract on Trump creating a National Bitcoin Reserve in 2026 sits at only 4%, and Kalshi pricing the Fed holding an emergency meeting in 2026 is at 10%, together suggesting markets see institutional crypto policy as slow-moving."
  - "Resolution via UMA oracle requires formal establishment of a reserve, not merely executive order or committee vote; the gap between committee action and legal standing drives the low price."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A House committee advanced legislation to codify the existing US Strategic Bitcoin Reserve and ban sales of qualifying federal bitcoin for 20 years."
    publisher: "Kevin Helms"
    published_at: "2026-09-21T00:00:00.000Z"
    source_url: "https://news.bitcoin.com/regulation-and-legal/house-panel-advances-us-bitcoin-reserve-bill-with-20-year-hold/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kevin Helms"
        source_url: "https://news.bitcoin.com/regulation-and-legal/house-panel-advances-us-bitcoin-reserve-bill-with-20-year-hold/"
        retrieved_at: "2026-09-21T07:47:18+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on formal establishment; the 7% price signals the market treats committee advancement as far from a done deal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kevin Helms: House Panel Advances US Bitcoin Reserve Bill With 20-Year Hold"
    url: "https://news.bitcoin.com/regulation-and-legal/house-panel-advances-us-bitcoin-reserve-bill-with-20-year-hold/"
    published_at: "2026-09-21T00:00:00.000Z"
    retrieved_at: "2026-09-21T07:47:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
