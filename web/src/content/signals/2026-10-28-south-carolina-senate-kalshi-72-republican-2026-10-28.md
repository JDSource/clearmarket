---
signal_id: "CMSIG2026102804"
signal_slug: "south-carolina-senate-kalshi-72-republican-2026-10-28"
headline: "South Carolina Senate: Kalshi 72% Republican"
semantic_title: "Republican holds slight edge in South Carolina Senate race"
telemetry: "Kalshi 72%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T00:00:00.000Z"
event_id: "CM-EVT-YB0M8XXMW8"
event_slug: "senatesc-26"
event_question: "Who will win the South Carolina Senate election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATESC-26-R"
  question_raw: "Will Republicans win the Senate race in South Carolina?"
  current_price: 0.72
  volume_24h_usd: 96065.13
  arbitration_model: "kalshi_staff"
  resolution_source: "United States Congress"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican win in the South Carolina Senate race at 72%, making it a moderately favored but not locked-in outcome."
  - "Trump's in-state rally visit aligns with the Republican-lean pricing, though 28% odds still leave meaningful uncertainty."
  - "A companion Kalshi contract on New Hampshire holding a same-party governor-senator combo sits at 86%, illustrating how different state-level races carry varying certainty."
  - "Kalshi resolves via United States Congress certification; final margin, not Trump rally count, determines the outcome."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump visited South Carolina on the campaign trail as the Senate race draws attention in the final days before midterm Election Day."
    publisher: "Caroline Linton Associate Managing Editor, Politics"
    published_at: "2026-10-28T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/live-updates/2026-elections-midtems-house-senate-trump/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Caroline Linton Associate Managing Editor, Politics"
        source_url: "https://www.cbsnews.com/live-updates/2026-elections-midtems-house-senate-trump/"
        retrieved_at: "2026-10-30T14:47:28+00:00"
  - type: "pm_response"
    notes: "Kalshi's 72% Republican read on South Carolina is consistent with a lean-red state in a Democratic wave environment, reflecting a partial but not complete blue-wave spillover."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Caroline Linton Associate Managing Editor, Politics: Live Midterm Election Updates: Peltola denies \"tricking voters,\" Trump"
    url: "https://www.cbsnews.com/live-updates/2026-elections-midtems-house-senate-trump/"
    published_at: "2026-10-28T00:00:00.000Z"
    retrieved_at: "2026-10-30T14:47:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
