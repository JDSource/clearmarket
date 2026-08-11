---
signal_id: "CMSIG2026080807"
signal_slug: "gop-holds-congress-after-2026-midterms-kalshi-43-2026-08-08"
headline: "GOP holds Congress after 2026 midterms: Kalshi 43%"
semantic_title: "Republicans holding Congress after midterms stays below 50%"
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
  volume_24h_usd: 9376.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices Republicans controlling at least one chamber of Congress after the 2026 midterms at 43%, a slight minority probability."
  - "Senate Republicans averting a shutdown is a defensive political win, but the market at 43% suggests it is not enough to shift the chamber-control outlook."
  - "The Todd Blanche attorney general confirmation by a single 50-49 vote underscores thin Republican Senate margins heading into November."
  - "Kalshi's Michigan same-party governor-senator outcome at 56% (CM-EVT-5BB4SFW2V1) signals Democrats are favored in a key swing-state bellwether."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Senate passed a government-funding bill to avert a shutdown ahead of the November midterm elections."
    publisher: "Morgan Rimmer"
    published_at: "2026-08-08T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/08/08/politics/senate-government-funding-shutdown"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Morgan Rimmer"
        source_url: "https://www.cnn.com/2026/08/08/politics/senate-government-funding-shutdown"
        retrieved_at: "2026-08-11T08:49:29+00:00"
  - type: "pm_response"
    notes: "Kalshi contract; resolution source listed as Bureau of Labor Statistics (likely a Kalshi tagging quirk); settles on certified 2026 midterm results."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Morgan Rimmer: Senate passes bill to fund government in bid to avert shutdown ahead o"
    url: "https://www.cnn.com/2026/08/08/politics/senate-government-funding-shutdown"
    published_at: "2026-08-08T00:00:00.000Z"
    retrieved_at: "2026-08-11T08:49:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
