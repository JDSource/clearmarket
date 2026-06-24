---
signal_id: "CMSIG2026062405"
signal_slug: "iran-ends-enrichment-by-june-30-polymarket-24-2026-06-24"
headline: "Iran ends enrichment by June 30: Polymarket 24%"
semantic_title: "Iran ends uranium enrichment by June 30 pricing holds deep discount"
telemetry: "Polymarket 24%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T00:00:00.000Z"
event_id: "CM-EVT-73D6P1DKY8"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-june-30"
event_question: "Will Iran agree to end uranium enrichment by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9d3f02264a94bafc676afd7add8b11442e6ec72dabaa69cefef835f0672275c7"
  question_raw: " Iran agrees to end enrichment of uranium by June 30?"
  current_price: 0.24
  volume_24h_usd: 173700.74918100028
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices Iran agreeing to end uranium enrichment by June 30 at just 24%, a steep discount to the broader deal probability."
  - "Trump's ultimatum on inspections suggests enrichment cessation is a harder ask than a general deal framework, and the market reflects that gap."
  - "The broader US-Iran deal by June 30 contract (CM-EVT-LG47Z78CF2) sits at 51%, making enrichment-end roughly half as likely as any deal."
  - "Resolves via UMA oracle; a formal public commitment to halt enrichment, not just inspection access, is required for settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump threatened to cancel meetings with Iran if Tehran denies IAEA nuclear inspections, as both sides dispute whether Iran has already agreed."
    publisher: "economictimes.indiatimes.com"
    published_at: "2026-06-24T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/news/international/global-trends/trump-says-he-would-cancel-meetings-with-iran-if-they-denies-iaea-nuclear-inspections/articleshow/131952535.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "economictimes.indiatimes.com"
        source_url: "https://economictimes.indiatimes.com/news/international/global-trends/trump-says-he-would-cancel-meetings-with-iran-if-they-denies-iaea-nuclear-inspections/articleshow/131952535.cms"
        retrieved_at: "2026-06-24T10:45:49+00:00"
  - type: "pm_response"
    notes: "The 27-point spread between Polymarket's any-deal (51%) and enrichment-end (24%) contracts reveals the market sees a partial or framework deal as far more likely than full enrichment cessation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "economictimes.indiatimes.com: Trump says he would 'cancel meetings' with Iran if they deny IAEA nucl"
    url: "https://economictimes.indiatimes.com/news/international/global-trends/trump-says-he-would-cancel-meetings-with-iran-if-they-denies-iaea-nuclear-inspections/articleshow/131952535.cms"
    published_at: "2026-06-24T00:00:00.000Z"
    retrieved_at: "2026-06-24T10:45:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
