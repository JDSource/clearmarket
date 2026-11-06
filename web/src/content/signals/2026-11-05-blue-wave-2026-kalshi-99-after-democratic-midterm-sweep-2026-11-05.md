---
signal_id: "CMSIG2026110505"
signal_slug: "blue-wave-2026-kalshi-99-after-democratic-midterm-sweep-2026-11-05"
headline: "Blue wave 2026: Kalshi 99% after Democratic midterm sweep"
semantic_title: "Blue wave in 2026 nears full pricing after Democratic sweep"
telemetry: "Kalshi 99%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-11-05T12:31:10.000Z"
event_id: "CM-EVT-QK0HJYVMX2"
event_slug: "kxbluewavecombo-27feb"
event_question: "Will there be a blue wave in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBLUEWAVECOMBO-27FEB"
  question_raw: "Will Democrats hold 218 or more seats in the House after the 2026 midterms AND hold 49 or more seats in the Senate after the 2026 midterms?"
  current_price: 0.99
  volume_24h_usd: 360378.37
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices 99% on a blue wave in 2026, essentially fully resolved after NBC's projection of a Democratic sweep of Congress."
  - "News of Democrats flipping control of both chambers is consistent with the near-certain pricing; the market led or ran concurrent with election-night calls."
  - "Companion Polymarket contract (CM-EVT-64KY3VMH10) prices Trump impeachment at only 2%, suggesting markets see the new Democratic Congress as a check but not a removal vehicle."
  - "Resolution source is Bureau of Labor Statistics per the Kalshi contract metadata, though standard blue-wave resolution would typically reference official certified election results."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "NBC News projects Democrats swept the 2026 midterms, flipping Congress and winning major races including the Los Angeles mayor's race."
    publisher: "0 NBC News NBC News"
    published_at: "2026-11-05T12:31:10.000Z"
    source_url: "https://www.nbcnews.com/politics/2026-election/live-blog/election-results-house-senate-trump-congress-live-updates-rcna607549"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "0 NBC News NBC News"
        source_url: "https://www.nbcnews.com/politics/2026-election/live-blog/election-results-house-senate-trump-congress-live-updates-rcna607549"
        retrieved_at: "2026-11-06T07:48:14+00:00"
  - type: "pm_response"
    notes: "Kalshi at 99% is effectively resolved; resolution source listed as BLS, which may indicate a data-mapping note rather than the operative resolver for this contract."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "0 NBC News NBC News: Election 2026 results live updates: Vote counts in Alaska, Mississippi"
    url: "https://www.nbcnews.com/politics/2026-election/live-blog/election-results-house-senate-trump-congress-live-updates-rcna607549"
    published_at: "2026-11-05T12:31:10.000Z"
    retrieved_at: "2026-11-06T07:48:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
