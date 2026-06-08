---
signal_id: "CMSIG2026060808"
signal_slug: "dems-win-house-in-2026-midterms-kalshi-78-2026-06-08"
headline: "Dems win House in 2026 midterms: Kalshi 78%"
semantic_title: "Democrats retaking House consensus holds at high conviction"
telemetry: "Kalshi 78%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-08T10:36:59.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party or the Republican Party win control of the U.S. House of Representatives in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.78
  volume_24h_usd: 13639.57
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices 78% on the Democratic Party winning House control after the 2026 midterms."
  - "Gerrymandering stories highlight Republican map-drawing efforts, yet prediction markets price Democrats as heavy favorites, markets are not endorsing GOP redistricting as a game-changer."
  - "A companion Kalshi contract (CM-EVT-T5VXKJT451) prices only 23% on Republicans controlling at least one chamber after midterms, reinforcing the Democratic-lean consensus."
  - "Resolves via Library of Congress official chamber composition record post-election; the 78% probability reflects a structural midterm-wave expectation, not a specific district call."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Mid-decade gerrymandering efforts by state legislatures are redrawing congressional maps ahead of the 2026 midterms, complicating House majority calculus."
    publisher: "Grace Segers"
    published_at: "2026-06-08T10:36:59.000Z"
    source_url: "https://newrepublic.com/article/211427/partisan-gerrymandering-going-get-worse"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Grace Segers"
        source_url: "https://newrepublic.com/article/211427/partisan-gerrymandering-going-get-worse"
        retrieved_at: "2026-06-08T12:25:51+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Library of Congress; the 78% Democratic House win probability versus 23% GOP chamber control probability are directionally consistent across venues."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Grace Segers: Gerrymandering Is Only Going to Get Worse | The New Republic"
    url: "https://newrepublic.com/article/211427/partisan-gerrymandering-going-get-worse"
    published_at: "2026-06-08T10:36:59.000Z"
    retrieved_at: "2026-06-08T12:25:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
