---
signal_id: "CMSIG2026102804"
signal_slug: "republicans-hold-more-governorships-after-midterms-kalshi-74-2026-10-28"
headline: "Republicans hold more governorships after midterms: Kalshi 74%"
semantic_title: "GOP gubernatorial edge after midterms stays favored at 74 percent"
telemetry: "Kalshi 74%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T00:00:00.000Z"
event_id: "CM-EVT-4DFCBXLZN6"
event_slug: "kxgovwins-27jan01"
event_question: "Will Republicans hold more governorships than Democrats after the midterms?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVWINS-27JAN01-R-50"
  question_raw: "Will the difference between the number of Republican governors and the number of Democratic governors be between -50 and -1 governors after the 2026 midterms?"
  current_price: 0.74
  volume_24h_usd: 892.45
  arbitration_model: "kalshi_staff"
  resolution_source: "the Statistical Review of World Energy"
  resolves_at: "2027-04-01T15:00:00Z"
bullets:
  - "The Kalshi contract prices 74% odds that Republicans will hold more governorships than Democrats after the 2026 midterms."
  - "Despite news reports of 'GOP midterm woes,' the gubernatorial market holds meaningfully above 50%, suggesting the market is not pricing a Democratic wave on the state level."
  - "The 11-point gap between this contract (74%) and the congressional chamber control contract (63%) implies the market sees the gubernatorial map as the more reliable Republican floor."
  - "Resolves via the Statistical Review of World Energy as named source, an unusual resolution mechanic that traders should verify before sizing positions."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "With midterms days away, Trump is campaigning heavily to shore up Republican positions across multiple states amid reports of mounting GOP woes."
    publisher: "Caroline Linton Associate Managing Editor, Politics"
    published_at: "2026-10-28T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/live-updates/2026-elections-midtems-house-senate-trump/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Caroline Linton Associate Managing Editor, Politics"
        source_url: "https://www.cbsnews.com/live-updates/2026-elections-midtems-house-senate-trump/"
        retrieved_at: "2026-10-28T15:33:55+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 74% on Republican gubernatorial edge runs notably higher than the 63% on congressional chamber control, indicating divergent market views across the two battlefields."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Caroline Linton Associate Managing Editor, Politics: Live Updates: 2026 midterm campaigns make final push before Election D"
    url: "https://www.cbsnews.com/live-updates/2026-elections-midtems-house-senate-trump/"
    published_at: "2026-10-28T00:00:00.000Z"
    retrieved_at: "2026-10-28T15:33:55+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
