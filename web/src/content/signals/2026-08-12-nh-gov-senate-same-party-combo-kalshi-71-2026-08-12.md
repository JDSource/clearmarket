---
signal_id: "CMSIG2026081205"
signal_slug: "nh-gov-senate-same-party-combo-kalshi-71-2026-08-12"
headline: "NH Gov-Senate same-party combo: Kalshi 71%"
semantic_title: "New Hampshire same-party governor-senate outcome stays favored"
telemetry: "Kalshi 71%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-12T00:00:00.000Z"
event_id: "CM-EVT-2P1810WLM7"
event_slug: "kxnhsengovcombo-26nov"
event_question: "Will the Governor of New Hampshire and the U.S. Senator from New Hampshire be from the same political party by 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXNHSENGOVCOMBO-26NOV-REPDEM"
  question_raw: "Will New Hampshire Governor winner be Republican party and New Hampshire Senate winner be Democratic party?"
  current_price: 0.71
  volume_24h_usd: 4529.43
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-11-03T15:00:00Z"
bullets:
  - "Kalshi prices New Hampshire electing a governor and senator from the same party at 71%, making it the most likely single-party sweep among tracked states."
  - "Volume on this contract jumped 194x day over day, consistent with primary results shifting the perceived probability of a unified New Hampshire outcome."
  - "Iowa's same-party contract at 35% and Michigan's at 53% show the market sees wide variation in state-level sweep probability across competitive midterm battlegrounds."
  - "Resolves via Bureau of Labor Statistics as named source; final settlement depends on certified general-election results in November 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Democratic primary voters are prioritizing change candidates, reshaping competitive state general-election landscapes ahead of November 2026 midterms."
    publisher: "apnews.com"
    published_at: "2026-08-12T00:00:00.000Z"
    source_url: "https://apnews.com/article/democrats-wisconsin-primary-hong-crowley-flanagan-0618c650d24c17a2a8f2d3273d813808"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/democrats-wisconsin-primary-hong-crowley-flanagan-0618c650d24c17a2a8f2d3273d813808"
        retrieved_at: "2026-08-15T08:21:50+00:00"
  - type: "pm_response"
    notes: "Kalshi volume on CM-EVT-2P1810WLM7 rose 194x day over day, one of the strongest activity signals in the midterm suite, pointing to meaningful fresh positioning after primary results."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Democratic voters are making clear they just want change | AP News"
    url: "https://apnews.com/article/democrats-wisconsin-primary-hong-crowley-flanagan-0618c650d24c17a2a8f2d3273d813808"
    published_at: "2026-08-12T00:00:00.000Z"
    retrieved_at: "2026-08-15T08:21:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
