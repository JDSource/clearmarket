---
signal_id: "CMSIG2026092601"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-22-2026-09-26"
headline: "Hormuz traffic normal by Dec 31: Polymarket 22%"
semantic_title: "Hormuz reopening by year-end stays near 25% odds"
telemetry: "Polymarket 22%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-26T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.22
  volume_24h_usd: 327248.0929920001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 22% on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Trump's reported rejection of Iran's seven-day ceasefire offer is consistent with the market's low-odds pricing on a near-term resolution."
  - "Trading volume on the related CM-EVT-38HGT3RJ52 contract surged roughly 1,000x day-over-day, signaling sharply rising market attention on the Iran standoff."
  - "The Kalshi contract on US embassy reopening in Iran sits at just 4%, suggesting markets see the diplomatic relationship as broadly frozen beyond the Hormuz question alone."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump has reportedly rejected Iran's seven-day ceasefire proposal to reopen the Strait of Hormuz, leaving negotiations at an impasse."
    publisher: "theguardian.com"
    published_at: "2026-09-26T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/sep/26/trump-dismiss-iran-seven-day-peace-deal-hormuz"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theguardian.com"
        source_url: "https://www.theguardian.com/world/2026/sep/26/trump-dismiss-iran-seven-day-peace-deal-hormuz"
        retrieved_at: "2026-09-26T12:39:23+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 22% price reflects persistent doubt that US-Iran talks produce a working agreement before year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theguardian.com: Trump reportedly rejects Iran’s seven-day peace deal to reopen strait"
    url: "https://www.theguardian.com/world/2026/sep/26/trump-dismiss-iran-seven-day-peace-deal-hormuz"
    published_at: "2026-09-26T00:00:00.000Z"
    retrieved_at: "2026-09-26T12:39:23+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
