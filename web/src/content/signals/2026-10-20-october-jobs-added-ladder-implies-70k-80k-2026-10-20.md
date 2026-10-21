---
signal_id: "CMSIG2026102004"
signal_slug: "october-jobs-added-ladder-implies-70k-80k-2026-10-20"
headline: "October jobs added: ladder implies 70K-80K"
semantic_title: "October nonfarm payrolls seen around 70K-80K jobs added"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-20T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payroll change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.4
  volume_24h_usd: 4.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "The ladder places 50% above 70,000 and 40% above 80,000, with consensus pinned in the 70K-80K range for October payrolls."
  - "The ADP 4-week average of 18,500 weekly hires implies roughly 74,000 monthly, landing squarely in the ladder's consensus zone; the market is not fading the weak ADP signal."
  - "The 93% probability above negative 25,000 confirms the market still prices out a payroll contraction despite the softening hiring data."
  - "The October unemployment ladder (CM-EVT-2X91TW50H2) showing 4.1-4.2% is consistent: moderate payroll growth supports gradual unemployment drift, not a sharp spike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "ADP's NER Pulse showed US private employers added an average of only 18,500 jobs per week in early October, signaling a loss of hiring momentum."
    publisher: "FXStreet Team"
    published_at: "2026-10-20T00:00:00.000Z"
    source_url: "https://www.fxstreet.com/news/us-adp-employment-change-4-week-average-drops-to-1850k-202610201221"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "FXStreet Team"
        source_url: "https://www.fxstreet.com/news/us-adp-employment-change-4-week-average-drops-to-1850k-202610201221"
        retrieved_at: "2026-10-21T07:48:07+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder's 70K-80K implied range aligns tightly with the ADP weekly pulse data, suggesting no meaningful disagreement between the high-frequency hiring signal and market pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "FXStreet Team: US ADP Employment Change 4-week average drops to 18.50K"
    url: "https://www.fxstreet.com/news/us-adp-employment-change-4-week-average-drops-to-1850k-202610201221"
    published_at: "2026-10-20T00:00:00.000Z"
    retrieved_at: "2026-10-21T07:48:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
