---
signal_id: "CMSIG2026091307"
signal_slug: "democrats-win-us-house-in-2026-kalshi-85-2026-09-13"
headline: "Democrats win US House in 2026: Kalshi 85%"
semantic_title: "Democrats winning the House stays heavily favored at 85 percent"
telemetry: "Kalshi 85%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-13T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.85
  volume_24h_usd: 19531.84
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi puts 85% on the Democratic Party winning the US House in the 2026 midterm election, resolving via Library of Congress."
  - "Democrat planning for post-majority oversight tools is consistent with a market that already strongly prices in a Democratic House takeover."
  - "Companion Kalshi contract (CM-EVT-T5VXKJT451) prices Republicans holding at least one chamber at 50%, pointing to a split-Congress scenario as the modal outcome."
  - "The gap between 85% Democratic House and 50% Republican at least one chamber implies Republicans retaining the Senate as the most likely balance."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Democrats are eyeing new oversight tools if they retake the House majority in the 2026 midterms, as CNN reports on planning for potential Trump accountability investigations."
    publisher: "Annie Grayer"
    published_at: "2026-09-13T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/09/13/politics/democrats-trump-investigations-midterms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Annie Grayer"
        source_url: "https://www.cnn.com/2026/09/13/politics/democrats-trump-investigations-midterms"
        retrieved_at: "2026-09-14T14:41:02+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Library of Congress official certification of midterm House results; covers the full 2026 general election cycle."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Annie Grayer: Democrats eye a new tool to hold Trump accountable if they win the Hou"
    url: "https://www.cnn.com/2026/09/13/politics/democrats-trump-investigations-midterms"
    published_at: "2026-09-13T00:00:00.000Z"
    retrieved_at: "2026-09-14T14:41:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
