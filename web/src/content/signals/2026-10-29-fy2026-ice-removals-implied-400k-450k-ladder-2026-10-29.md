---
signal_id: "CMSIG2026102908"
signal_slug: "fy2026-ice-removals-implied-400k-450k-ladder-2026-10-29"
headline: "FY2026 ICE removals implied 400K-450K: ladder"
semantic_title: "ICE removals in FY2026 seen above 400,000 but below 500,000"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-29T00:00:00.000Z"
event_id: "CM-EVT-F0MWBBP842"
event_slug: "kxdeportations-27jan01"
event_question: "FY2026 ICE removals"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXDEPORTATIONS-27JAN01-T450000"
  question_raw: "Will the number of ICE removals be above 450000 in FY2026?"
  current_price: 0.45
  volume_24h_usd: 0.96
  arbitration_model: "kalshi_staff"
  resolution_source: "the Statistical Review of World Energy"
  resolves_at: "2027-04-01T15:00:00Z"
bullets:
  - "Prediction market ladder implies FY2026 ICE removals in the 400,000-450,000 range: 94% above 400K but only 45% above 450K."
  - "The 22% probability above 500K shows the market treats a half-million removals as unlikely, even amid the enforcement surge AP documents."
  - "The 98% probability above 300K confirms the market fully prices in a historically high removal year; the debate is only about the upper end of the range."
  - "Resolves via official DHS or ICE fiscal-year statistics; the FY2026 close provides a clean settlement date."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "AP reports Trump's immigration crackdown is generating political backlash ahead of midterms, with voters souring on enforcement policies."
    publisher: "Tim Sullivan, Nicholas Riccardi"
    published_at: "2026-10-29T00:00:00.000Z"
    source_url: "https://apnews.com/article/trump-immigration-politics-ice-democrats-deportations-973ea68bd778fbfd7f38209f65bb351c"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Tim Sullivan, Nicholas Riccardi"
        source_url: "https://apnews.com/article/trump-immigration-politics-ice-democrats-deportations-973ea68bd778fbfd7f38209f65bb351c"
        retrieved_at: "2026-10-29T07:47:47+00:00"
  - type: "pm_response"
    notes: "Ladder contract; no venue attribution available in the data, but the distribution is internally consistent and anchors the immigration enforcement debate."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Tim Sullivan, Nicholas Riccardi: Immigration crackdowns lose political power as voters sour on Trump's"
    url: "https://apnews.com/article/trump-immigration-politics-ice-democrats-deportations-973ea68bd778fbfd7f38209f65bb351c"
    published_at: "2026-10-29T00:00:00.000Z"
    retrieved_at: "2026-10-29T07:47:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
