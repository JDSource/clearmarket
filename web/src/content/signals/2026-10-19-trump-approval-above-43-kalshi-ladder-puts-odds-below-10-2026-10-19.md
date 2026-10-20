---
signal_id: "CMSIG2026101906"
signal_slug: "trump-approval-above-43-kalshi-ladder-puts-odds-below-10-2026-10-19"
headline: "Trump approval above 43%: Kalshi ladder puts odds below 10%"
semantic_title: "Trump approval above 43 percent stays a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-19T00:00:00.000Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating threshold during contract window"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.031
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Kalshi ladder shows only 3% probability of Trump's approval rating exceeding 43%, with no strike above 50% reaching double digits."
  - "The record-low approval news is consistent with the ladder's distribution, which implies the market already embedded a sub-43% approval scenario."
  - "The companion Kalshi binary (CM-EVT-0DMSQTKVX3) puts 10% odds on approval ending below its stated threshold on December 31, 2026, suggesting modest recovery odds are priced in over the longer horizon."
  - "Resolution for CM-EVT-0DMSQTKVX3 cites a polling organization as source; the unnamed resolver is a settlement-edge risk if methodologies diverge across pollsters."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "PBS News reports President Donald Trump's approval rating hit a record low, with NPR and Cook Political Report analysts discussing the political fallout."
    publisher: "Geoff Bennett, Ali Schmitz"
    published_at: "2026-10-19T00:00:00.000Z"
    source_url: "https://www.pbs.org/newshour/show/tamara-keith-and-carrie-dann-on-trumps-approval-rating-hitting-a-record-low"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Geoff Bennett, Ali Schmitz"
        source_url: "https://www.pbs.org/newshour/show/tamara-keith-and-carrie-dann-on-trumps-approval-rating-hitting-a-record-low"
        retrieved_at: "2026-10-20T07:47:27+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on Trump approval; the distribution is tightly stacked below 43%, fully aligned with the record-low news and leaving little room for upside surprise."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Geoff Bennett, Ali Schmitz: Tamara Keith and Carrie Dann on Trump's approval rating hitting a reco"
    url: "https://www.pbs.org/newshour/show/tamara-keith-and-carrie-dann-on-trumps-approval-rating-hitting-a-record-low"
    published_at: "2026-10-19T00:00:00.000Z"
    retrieved_at: "2026-10-20T07:47:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
