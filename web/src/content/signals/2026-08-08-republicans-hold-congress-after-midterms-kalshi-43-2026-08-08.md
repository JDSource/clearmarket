---
signal_id: "CMSIG2026080804"
signal_slug: "republicans-hold-congress-after-midterms-kalshi-43-2026-08-08"
headline: "Republicans hold Congress after midterms: Kalshi 43%"
semantic_title: "GOP holding Congress after midterms stays below 50 percent"
telemetry: "Kalshi 43%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-08T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.43
  volume_24h_usd: 3254.45
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices Republicans controlling at least one chamber of Congress after the 2026 midterms at 43%."
  - "The Senate's passage of a funding bill removes a shutdown risk that could have further damaged the GOP brand, but the market still puts odds below 50%."
  - "A separate Kalshi contract on Republicans holding more governorships than Democrats sits at 54%, suggesting mixed signals across different electoral contests."
  - "Resolves via the Bureau of Labor Statistics as named source, though actual resolution will hinge on certified election results from November 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Senate passed a government funding bill to avert a shutdown ahead of the 2026 midterm elections."
    publisher: "Morgan Rimmer"
    published_at: "2026-08-08T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/08/08/politics/senate-government-funding-shutdown"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Morgan Rimmer"
        source_url: "https://www.cnn.com/2026/08/08/politics/senate-government-funding-shutdown"
        retrieved_at: "2026-08-10T09:14:34+00:00"
  - type: "pm_response"
    notes: "Kalshi prices Republicans as slight underdogs to hold either chamber, with the shutdown avoidance providing minimal electoral uplift in the current pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Morgan Rimmer: Senate passes bill to fund government in bid to avert shutdown ahead o"
    url: "https://www.cnn.com/2026/08/08/politics/senate-government-funding-shutdown"
    published_at: "2026-08-08T00:00:00.000Z"
    retrieved_at: "2026-08-10T09:14:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
