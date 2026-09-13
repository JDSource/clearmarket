---
signal_id: "CMSIG2026091307"
signal_slug: "russian-sanctions-bill-becomes-law-kalshi-76-2026-09-13"
headline: "Russian sanctions bill becomes law: Kalshi 76%"
semantic_title: "Russian sanctions bill becoming law stays favored at 76%"
telemetry: "Kalshi 76%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-13T00:00:00.000Z"
event_id: "CM-EVT-C6SL3Y8HY3"
event_slug: "kxsanctionrussia-26jan01"
event_question: "Will a Russian sanctions bill become law?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSANCTIONRUSSIA-26JAN01-27"
  question_raw: "Will a Russian sanctions bill become law before 2027?"
  current_price: 0.76
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "White House"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract prices a Russian sanctions bill becoming law at 76%, resolving via White House."
  - "Continued Russian strikes on Ukrainian civilian infrastructure keep political pressure elevated for legislative action, consistent with the high probability pricing."
  - "The Polymarket contract on the US recognizing Russian sovereignty over Ukraine before 2027 sits at just 3%, suggesting markets see the policy direction as sanctions and support, not accommodation."
  - "Resolution requires White House confirmation of enacted legislation; Senate dynamics (Story 16 notes far-right objections) remain the key procedural risk not yet moving this price below 76%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Russia struck Ukrainian power infrastructure while Kyiv targeted a Russian refining hub, escalating the conflict on September 13."
    publisher: "bloomberg.com"
    published_at: "2026-09-13T00:00:00.000Z"
    source_url: "https://www.bloomberg.com/news/articles/2026-09-13/russia-strikes-ukraine-power-sites-as-kyiv-targets-refining-hub"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bloomberg.com"
        source_url: "https://www.bloomberg.com/news/articles/2026-09-13/russia-strikes-ukraine-power-sites-as-kyiv-targets-refining-hub"
        retrieved_at: "2026-09-13T13:04:33+00:00"
  - type: "pm_response"
    notes: "Kalshi resolves via White House; enacted legislation, not a floor vote, is the resolution trigger."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bloomberg.com: Russia Strikes Ukraine Power Sites as Kyiv Targets Refining Hub - Bloo"
    url: "https://www.bloomberg.com/news/articles/2026-09-13/russia-strikes-ukraine-power-sites-as-kyiv-targets-refining-hub"
    published_at: "2026-09-13T00:00:00.000Z"
    retrieved_at: "2026-09-13T13:04:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
