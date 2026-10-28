---
signal_id: "CMSIG2026102806"
signal_slug: "tx-34-house-seat-republican-win-kalshi-89-2026-10-28"
headline: "TX-34 House seat Republican win: Kalshi 89%"
semantic_title: "Republican candidate in TX-34 stays heavily favored"
telemetry: "Kalshi 89%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T00:00:00.000Z"
event_id: "CM-EVT-F19JK9H606"
event_slug: "housetx34-26"
event_question: "Will the Republican candidate win the TX-34 House seat in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSETX34-26-D"
  question_raw: "Will Democratic win the House race for TX-34?"
  current_price: 0.89
  volume_24h_usd: 1321.99
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi places 89% on the Republican candidate winning the TX-34 House seat, resolving via the Library of Congress; trading volume surged 6,564% day over day."
  - "The sharp volume spike signals fresh attention on this seat as midterm campaigns enter their final days and early voting accelerates."
  - "TX-34 has historically been competitive; the 89% pricing with a volume surge suggests the market is moving to price the Republican as a strong but not certain favorite."
  - "The Kalshi contract on Republicans holding more governorships than Democrats after the midterms (CM-EVT-4DFCBXLZN6) sits at 74%, framing a broadly favorable but not dominant Republican map."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Midterm campaigns are making their final push before Election Day with early voters already at the polls across the country."
    publisher: "Caroline Linton Associate Managing Editor, Politics"
    published_at: "2026-10-28T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/live-updates/2026-elections-midtems-house-senate-trump/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Caroline Linton Associate Managing Editor, Politics"
        source_url: "https://www.cbsnews.com/live-updates/2026-elections-midtems-house-senate-trump/"
        retrieved_at: "2026-10-28T14:49:33+00:00"
  - type: "pm_response"
    notes: "Kalshi at 89% on TX-34 with a 66x volume surge is the sharpest signal of late-cycle attention in the midterm contract suite today."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Caroline Linton Associate Managing Editor, Politics: Live Updates: 2026 midterm campaigns make final push before Election D"
    url: "https://www.cbsnews.com/live-updates/2026-elections-midtems-house-senate-trump/"
    published_at: "2026-10-28T00:00:00.000Z"
    retrieved_at: "2026-10-28T14:49:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
