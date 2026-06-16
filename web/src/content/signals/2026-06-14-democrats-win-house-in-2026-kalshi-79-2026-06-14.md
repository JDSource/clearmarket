---
signal_id: "CMSIG2026061407"
signal_slug: "democrats-win-house-in-2026-kalshi-79-2026-06-14"
headline: "Democrats win House in 2026: Kalshi 79%"
semantic_title: "Democrats retaking the House in 2026 solidifies near strong consensus"
telemetry: "Kalshi 79%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-14T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party or the Republican Party win control of the U.S. House of Representatives in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.79
  volume_24h_usd: 9624.1
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices a 79% probability Democrats win control of the US House in the 2026 midterms."
  - "The NBC poll's five-point Democratic generic ballot lead is broadly consistent with the 79% pricing: markets and surveys align on a Democratic House lean."
  - "The Polymarket House contract (CM-EVT-2N6T7M0T15) prices 83% for Democrats, a small cross-venue gap suggesting Polymarket is modestly more bullish on a Democratic flip."
  - "Senate control (CM-EVT-M9WJY06T90) prices only 44% for Republicans, implying a potential split-chamber outcome is the market-implied base case heading into November."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "An NBC News poll shows Democrats holding a five-point generic ballot lead as Trump's approval rating weighs on Republican midterm prospects."
    publisher: "nbcnews.com"
    published_at: "2026-06-14T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/politics/2026-election/poll-democrats-maintain-edge-fight-congress-trump-gets-poor-marks-rcna348913"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nbcnews.com"
        source_url: "https://www.nbcnews.com/politics/2026-election/poll-democrats-maintain-edge-fight-congress-trump-gets-poor-marks-rcna348913"
        retrieved_at: "2026-06-16T12:50:14+00:00"
  - type: "pm_response"
    notes: "Kalshi and Polymarket House contracts converge near 80% for Democrats, with the Senate pricing a much tighter race reflecting differing map dynamics."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nbcnews.com: Poll: Democrats maintain an edge in the fight for Congress as Trump ge"
    url: "https://www.nbcnews.com/politics/2026-election/poll-democrats-maintain-edge-fight-congress-trump-gets-poor-marks-rcna348913"
    published_at: "2026-06-14T00:00:00.000Z"
    retrieved_at: "2026-06-16T12:50:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
