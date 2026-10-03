---
signal_id: "CMSIG2026100307"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-20-2026-10-03"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 20%"
semantic_title: "Strait of Hormuz traffic back to normal by year-end at 20 percent"
telemetry: "Polymarket 20%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-03T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.2
  volume_24h_usd: 156355.179048
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 20% on Strait of Hormuz traffic returning to normal by December 31, resolving via UMA oracle."
  - "The IRGC escalation warning and third US carrier strike group deployment pull against the 20% pricing, while the reported MoU framework (Story 27) provides the bullish tail."
  - "Israel-Saudi normalization contract at 7% (same UMA oracle resolver) signals the broader regional settlement is not expected; Hormuz normalization likely requires that broader calm."
  - "Resolution requires UMA oracle confirmation of traffic normalization; partial resumption or contested shipping data may create settlement ambiguity."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's IRGC warned the US of a more lethal response as the USS Theodore Roosevelt heads to the Middle East, while Houthi missile debris injured a Saudi resident and a US-Iran framework agreement is reportedly in late drafting stages."
    publisher: "Surabhi Vasundharadevi, Nathaniel Lacsina"
    published_at: "2026-10-03T00:00:00.000Z"
    source_url: "https://gulfnews.com/world/mena/irans-irgc-warns-us-of-more-lethal-response-as-houthi-missile-debris-injures-saudi-resident-1.500696738"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Surabhi Vasundharadevi, Nathaniel Lacsina"
        source_url: "https://gulfnews.com/world/mena/irans-irgc-warns-us-of-more-lethal-response-as-houthi-missile-debris-injures-saudi-resident-1.500696738"
        retrieved_at: "2026-10-03T07:47:35+00:00"
  - type: "pm_response"
    notes: "Polymarket at 20% reflects a market genuinely split between escalation and negotiated resolution, with competing news catalysts on the same trading day."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Surabhi Vasundharadevi, Nathaniel Lacsina: Iran's IRGC warns US of 'more lethal' response as Houthi missile debri"
    url: "https://gulfnews.com/world/mena/irans-irgc-warns-us-of-more-lethal-response-as-houthi-missile-debris-injures-saudi-resident-1.500696738"
    published_at: "2026-10-03T00:00:00.000Z"
    retrieved_at: "2026-10-03T07:47:35+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
