---
signal_id: "CMSIG2026100705"
signal_slug: "gop-controls-at-least-one-chamber-after-midterms-kalshi-65-2026-10-07"
headline: "GOP controls at least one chamber after midterms: Kalshi 65%"
semantic_title: "Republicans holding at least one chamber stays near 65%"
telemetry: "Kalshi 65%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-07T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.65
  volume_24h_usd: 29987.54
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices 65% odds that Republicans will control at least one chamber of Congress after the 2026 midterms."
  - "News that massive GOP spending has not moved polls is at odds with a 65% Republican-control probability; the market has not shifted to reflect Democratic momentum."
  - "The companion Kalshi contract (CM-EVT-FV8MR86S63) prices 90% on Democrats winning the House, implying the market sees the Senate as the likely GOP hold."
  - "Resolves via Bureau of Labor Statistics-cited source tracking official congressional election outcomes; final certification required."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Half a billion dollars in Republican spending has failed to meaningfully move midterm polls, with Democrats expanding their competitive map."
    publisher: "Isaac Arnsdorf"
    published_at: "2026-10-07T00:00:00.000Z"
    source_url: "https://www.washingtonpost.com/politics/2026/10/07/half-billion-dollars-gop-spending-does-little-move-polls/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Isaac Arnsdorf"
        source_url: "https://www.washingtonpost.com/politics/2026/10/07/half-billion-dollars-gop-spending-does-little-move-polls/"
        retrieved_at: "2026-10-07T15:02:04+00:00"
  - type: "pm_response"
    notes: "Kalshi at 65% for GOP holding one chamber alongside 90% for a Democratic House implies a split-Congress base case, which the spending-effectiveness story does not yet dislodge."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Isaac Arnsdorf: Half a billion dollars in GOP spending does little to move polls - The"
    url: "https://www.washingtonpost.com/politics/2026/10/07/half-billion-dollars-gop-spending-does-little-move-polls/"
    published_at: "2026-10-07T00:00:00.000Z"
    retrieved_at: "2026-10-07T15:02:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
