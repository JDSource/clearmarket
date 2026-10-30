---
signal_id: "CMSIG2026102905"
signal_slug: "iran-nuclear-test-before-2027-polymarket-4-2026-10-29"
headline: "Iran nuclear test before 2027: Polymarket 4%"
semantic_title: "Iran nuclear test before 2027 remains a long shot despite missile news"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-29T00:00:00.000Z"
event_id: "CM-EVT-YQ6BFV3GX1"
event_slug: "iran-nuclear-test-before-2027"
event_question: "Will Iran conduct a nuclear test before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x765e5daae966128da2acac8edab65d23abcabcf8958563a490d24c3498812c85"
  question_raw: "Iran nuclear test before 2027?"
  current_price: 0.035
  volume_24h_usd: 2827.2733249999997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on an Iranian nuclear test before 2027 sits at 4%, despite an active week of proliferation headlines."
  - "The UN nuclear chief's report that Iran has not repaired damaged facilities is consistent with the market's low probability, the infrastructure for a test appears absent."
  - "Trading volume on this contract surged 17,043% day over day, signaling the proliferation headlines are drawing sharp attention even as the price holds low."
  - "The Kalshi contract on Trump visiting Iran (CM-EVT-V9QGT2SSP7) sits at just 2%, suggesting the market sees diplomacy as even less likely than a test, both tail risks remain priced near zero."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Proliferation news includes Putin test-firing a nuclear-capable missile, North Korea missile launches, and a UN nuclear chief report that Iran has not repaired facilities damaged in US strikes."
    publisher: "carnegieendowment.org"
    published_at: "2026-10-29T00:00:00.000Z"
    source_url: "https://carnegieendowment.org/programs/nuclear-policy/proliferation-news/proliferation-news-october-29-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "carnegieendowment.org"
        source_url: "https://carnegieendowment.org/programs/nuclear-policy/proliferation-news/proliferation-news-october-29-2026"
        retrieved_at: "2026-10-30T07:48:00+00:00"
  - type: "pm_response"
    notes: "Polymarket holds Iran nuclear test odds at 4% despite a surge in volume, consistent with UN reporting that Iran's nuclear facilities remain damaged."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "carnegieendowment.org: Proliferation News October 29, 2026 | Carnegie Endowment for Internati"
    url: "https://carnegieendowment.org/programs/nuclear-policy/proliferation-news/proliferation-news-october-29-2026"
    published_at: "2026-10-29T00:00:00.000Z"
    retrieved_at: "2026-10-30T07:48:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
