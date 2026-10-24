---
signal_id: "CMSIG2026102207"
signal_slug: "blue-tsunami-in-2026-midterms-kalshi-55-2026-10-22"
headline: "Blue tsunami in 2026 midterms: Kalshi 55%"
semantic_title: "Blue tsunami in 2026 midterms holds near 50 percent odds"
telemetry: "Kalshi 55%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-22T00:00:00.000Z"
event_id: "CM-EVT-6CY3Y4C610"
event_slug: "kxbluetsunamicombo-27feb"
event_question: "Will there be a blue tsunami in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBLUETSUNAMICOMBO-27FEB"
  question_raw: "Will Democrats hold 235 or more seats in the House after the 2026 midterms AND hold 51 or more seats in the Senate after the 2026 midterms?"
  current_price: 0.55
  volume_24h_usd: 32326.57
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market puts 55% odds on a blue tsunami in the 2026 midterms, a slim majority-favored outcome."
  - "Pollsters pointing to a great Democratic night are broadly consistent with Kalshi's pricing, but the 55% reading shows the market sees it as a coin-flip-plus rather than a certainty."
  - "A companion Kalshi contract (CM-EVT-QK0HJYVMX2) on a generic blue wave sits at 84%, suggesting markets distinguish between a wave and the stronger tsunami threshold."
  - "Resolution is via the Bureau of Labor Statistics as listed on Kalshi, the specific resolution criteria for 'blue tsunami' versus 'blue wave' will determine which contracts settle yes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Four top pollsters said polls point to a strong Democratic night on November 3, though reliability of polling remains debated."
    publisher: "Riya Misra"
    published_at: "2026-10-22T00:00:00.000Z"
    source_url: "https://www.politico.com/news/magazine/2026/10/21/4-top-pollsters-on-what-worries-them-most-01126222"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Riya Misra"
        source_url: "https://www.politico.com/news/magazine/2026/10/21/4-top-pollsters-on-what-worries-them-most-01126222"
        retrieved_at: "2026-10-24T07:48:16+00:00"
  - type: "pm_response"
    notes: "Kalshi prices the blue tsunami at 55%, sitting well below the 84% blue wave contract and reflecting genuine market uncertainty about the magnitude of any Democratic sweep."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Riya Misra: 4 Top Pollsters on What the Polls Are Really Saying"
    url: "https://www.politico.com/news/magazine/2026/10/21/4-top-pollsters-on-what-worries-them-most-01126222"
    published_at: "2026-10-22T00:00:00.000Z"
    retrieved_at: "2026-10-24T07:48:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
