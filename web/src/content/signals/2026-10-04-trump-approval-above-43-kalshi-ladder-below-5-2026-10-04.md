---
signal_id: "CMSIG2026100403"
signal_slug: "trump-approval-above-43-kalshi-ladder-below-5-2026-10-04"
headline: "Trump approval above 43%: Kalshi ladder below 5%"
semantic_title: "Trump approval odds stay below 43 percent threshold"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-04T09:06:50.000Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating threshold ladder"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.04
  volume_24h_usd: 1.13
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Kalshi ladder prices only 4% odds on Trump approval exceeding 43%, implying the market-implied level sits well below that threshold."
  - "Sinking approval headlines are consistent with the pricing, the market shows no meaningful probability of a recovery above 43%."
  - "The ladder shows near-zero probability across all strikes from 43% to 50%, a uniform bearish read on Trump's approval trajectory."
  - "Companion Polymarket contract CM-EVT-VNTLCWF6Y5 (Trump approval 2026) sits at 4%, cross-venue alignment confirms the low-approval consensus."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Multiple polls show Trump approval ratings sinking ahead of November 3 midterms, with USA Today reporting continued declines."
    publisher: "Fernando Cervantes Jr."
    published_at: "2026-10-04T09:06:50.000Z"
    source_url: "https://www.usatoday.com/story/news/politics/2026/10/04/trump-approval-rating-midterms-republicans-polls/92061673007/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Fernando Cervantes Jr."
        source_url: "https://www.usatoday.com/story/news/politics/2026/10/04/trump-approval-rating-midterms-republicans-polls/92061673007/"
        retrieved_at: "2026-10-04T13:39:12+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolution via polling organization; all strikes from 43% to 50% price at 5% or below, a tight distribution at the low end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Fernando Cervantes Jr.: Trump approval ratings sink ahead of midterms"
    url: "https://www.usatoday.com/story/news/politics/2026/10/04/trump-approval-rating-midterms-republicans-polls/92061673007/"
    published_at: "2026-10-04T09:06:50.000Z"
    retrieved_at: "2026-10-04T13:39:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
