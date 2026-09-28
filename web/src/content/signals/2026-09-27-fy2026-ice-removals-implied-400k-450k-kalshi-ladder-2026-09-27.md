---
signal_id: "CMSIG2026092707"
signal_slug: "fy2026-ice-removals-implied-400k-450k-kalshi-ladder-2026-09-27"
headline: "FY2026 ICE removals implied 400K-450K: Kalshi ladder"
semantic_title: "ICE removals in FY2026 seen near 400K-450K, well above floor"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-27T00:00:00.000Z"
event_id: "CM-EVT-F0MWBBP842"
event_slug: "kxdeportations-27jan01"
event_question: "FY2026 ICE removals total"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXDEPORTATIONS-27JAN01-T450000"
  question_raw: "Will the number of ICE removals be above 450000 in FY2026?"
  current_price: 0.16
  volume_24h_usd: 4.92
  arbitration_model: "kalshi_staff"
  resolution_source: "the Statistical Review of World Energy"
  resolves_at: "2027-04-01T15:00:00Z"
bullets:
  - "Kalshi ladder prices ICE removals in the 400K-450K range: 96% above 400K, collapsing to 16% above 450K and only 5% above 500K."
  - "Senator Jim Banks's legislative push to lock in enforcement levels is consistent with a market that sees removals running well above historical norms but plateauing near 400K-450K."
  - "The sharp drop from 96% to 16% between the 400K and 450K strikes implies the market sees the current pace as near its ceiling absent new statutory authority."
  - "Resolution is via FY2026 official ICE removal data; fiscal year ends September 30, 2026, meaning the final figure is imminent."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Senator Jim Banks is pushing to codify Trump's immigration enforcement into statute, warning executive-only enforcement could be reversed by a future administration."
    publisher: "foxnews.com"
    published_at: "2026-09-27T00:00:00.000Z"
    source_url: "https://www.foxnews.com/politics/massive-ice-sweep-fuels-gop-push-lock-trump-immigration-crackdown-law"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "foxnews.com"
        source_url: "https://www.foxnews.com/politics/massive-ice-sweep-fuels-gop-push-lock-trump-immigration-crackdown-law"
        retrieved_at: "2026-09-28T07:47:41+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolution source is unspecified beyond FY2026 ICE data; the fiscal year close on September 30 makes this a near-term settlement event."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "foxnews.com: Sen. Jim Banks pushes to codify Trump immigration crackdown into law |"
    url: "https://www.foxnews.com/politics/massive-ice-sweep-fuels-gop-push-lock-trump-immigration-crackdown-law"
    published_at: "2026-09-27T00:00:00.000Z"
    retrieved_at: "2026-09-28T07:47:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
