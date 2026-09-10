---
signal_id: "CMSIG2026091008"
signal_slug: "sept-unemployment-rate-seen-4-0-4-1-ladder-amid-iran-shippin-2026-09-10"
headline: "Sept unemployment rate seen 4.0-4.1%: ladder amid Iran shipping war"
semantic_title: "September unemployment rate priced near 4.0-4.1 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-10T00:00:00.000Z"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "September 2026 US unemployment rate (U-3)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T4.1"
  question_raw: "Will the unemployment rate (U-3) be above 4.1% in September?"
  current_price: 0.47
  volume_24h_usd: 30.26
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "The unemployment ladder prices September 2026 U-3 in the 4.0-4.1% range: 83% above 4.0% but only 47% above 4.1%, placing the implied rate right at the fulcrum."
  - "August payrolls beat sharply at 162,000 jobs added, broadly consistent with the ladder's center near 4.0-4.1%, though the Iran-driven shipping disruption introduces a tail risk not yet priced into near-term labor data."
  - "A sustained Hormuz closure would raise energy and goods costs, potentially slowing hiring in logistics and manufacturing; the unemployment ladder shows no material upside tail priced above 4.5% at this time."
  - "A separate ladder puts the Hormuz normalization probability at only 16% by year-end, suggesting the shipping disruption risk to the labor market is a slow-building rather than immediate shock."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Iran and the US exchanged tanker strikes in the Gulf of Oman in the biggest wave of shipping attacks since the conflict began, raising risks to energy supply chains and economic activity."
    publisher: "Enas Alashray"
    published_at: "2026-09-10T00:00:00.000Z"
    source_url: "https://www.reuters.com/world/middle-east/iran-attacks-us-base-jordan-ships-near-hormuz-after-tankers-sunk-2026-09-09/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Enas Alashray"
        source_url: "https://www.reuters.com/world/middle-east/iran-attacks-us-base-jordan-ships-near-hormuz-after-tankers-sunk-2026-09-09/"
        retrieved_at: "2026-09-10T12:39:52+00:00"
  - type: "pm_response"
    notes: "The unemployment ladder resolves on the Bureau of Labor Statistics September 2026 employment situation release; the 4.1% strike at 47% is the distribution's median pivot point."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Enas Alashray: Iran and US hit tankers in biggest wave of attacks on shipping since w"
    url: "https://www.reuters.com/world/middle-east/iran-attacks-us-base-jordan-ships-near-hormuz-after-tankers-sunk-2026-09-09/"
    published_at: "2026-09-10T00:00:00.000Z"
    retrieved_at: "2026-09-10T12:39:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
