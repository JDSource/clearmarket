---
signal_id: "CMSIG2026062303"
signal_slug: "trump-approval-above-43-kalshi-ladder-below-43-2026-06-23"
headline: "Trump approval above 43%: Kalshi ladder below 43"
semantic_title: "Trump approval pricing breaks away below 43 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-23T18:10:09.000Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating during polling period"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.28
  volume_24h_usd: 19.57
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Kalshi ladder implies approval below 43%: only 28% chance above 43%, dropping to 6% above 47%."
  - "The Reuters/Ipsos poll showing a term-low approval is consistent with the market placing the most likely range well under 43%."
  - "The companion below-ladder (CM-EVT-0DMSQTKVX3) puts 54% odds on approval below 36%, pointing to a wide downside distribution."
  - "Resolution depends on a named approval-rating data source; polling aggregators can lag sharp single-poll moves by several days."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Reuters/Ipsos poll shows Trump approval ties its term low, with only 25% of Americans saying the Iran war was worth its costs."
    publisher: "devdiscourse.com"
    published_at: "2026-06-23T18:10:09.000Z"
    source_url: "https://www.devdiscourse.com/article/politics/3939576-few-in-us-say-iran-war-was-worth-it-trump-approval-ties-lowest-of-term-reutersipsos-poll-finds"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "devdiscourse.com"
        source_url: "https://www.devdiscourse.com/article/politics/3939576-few-in-us-say-iran-war-was-worth-it-trump-approval-ties-lowest-of-term-reutersipsos-poll-finds"
        retrieved_at: "2026-06-24T10:45:49+00:00"
  - type: "pm_response"
    notes: "Two Kalshi approval ladders (above and below) triangulate a market-implied approval range of roughly 33-40%, consistent with reported poll results."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "devdiscourse.com: Few in US say Iran war was worth it; Trump approval ties lowest of ter"
    url: "https://www.devdiscourse.com/article/politics/3939576-few-in-us-say-iran-war-was-worth-it-trump-approval-ties-lowest-of-term-reutersipsos-poll-finds"
    published_at: "2026-06-23T18:10:09.000Z"
    retrieved_at: "2026-06-24T10:45:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
