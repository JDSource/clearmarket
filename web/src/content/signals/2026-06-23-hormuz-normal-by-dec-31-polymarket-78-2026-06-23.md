---
signal_id: "CMSIG2026062302"
signal_slug: "hormuz-normal-by-dec-31-polymarket-78-2026-06-23"
headline: "Hormuz normal by Dec 31: Polymarket 78%"
semantic_title: "Hormuz year-end reopening consensus hardens above three-quarters"
telemetry: "Polymarket 78%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-23T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will traffic through the Strait of Hormuz return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.78
  volume_24h_usd: 289674.7514719999
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Hormuz traffic returning to normal by December 31 at 78%."
  - "Iran's assertion of control over Hormuz is at odds with the elevated probability, suggesting markets weight the broader diplomatic trajectory over Iran's bargaining posture."
  - "The June 30 Hormuz deadline contract sits at only 18%, showing the market expects normalization to take months, not days."
  - "Resolves via portwatch.imf.org traffic data; the definition of 'normal' relative to pre-war baselines is the key settlement edge."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran insisted it will control the Strait of Hormuz even as the US agreed to lift sanctions following Switzerland talks."
    publisher: "news24.com"
    published_at: "2026-06-23T00:00:00.000Z"
    source_url: "https://www.news24.com/world/iran-insists-it-will-control-strait-of-hormuz-as-us-agrees-to-lift-sanctions-20260623-0295"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "news24.com"
        source_url: "https://www.news24.com/world/iran-insists-it-will-control-strait-of-hormuz-as-us-agrees-to-lift-sanctions-20260623-0295"
        retrieved_at: "2026-06-23T10:59:18+00:00"
  - type: "pm_response"
    notes: "Polymarket's 78% year-end price versus 18% end-of-June price reveals a market expecting a gradual, post-deal normalization arc rather than an imminent reopening."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "news24.com: Iran insists it will control Strait of Hormuz as US agrees to lift san"
    url: "https://www.news24.com/world/iran-insists-it-will-control-strait-of-hormuz-as-us-agrees-to-lift-sanctions-20260623-0295"
    published_at: "2026-06-23T00:00:00.000Z"
    retrieved_at: "2026-06-23T10:59:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
