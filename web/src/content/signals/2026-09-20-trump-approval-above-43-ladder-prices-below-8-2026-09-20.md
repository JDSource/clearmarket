---
signal_id: "CMSIG2026092005"
signal_slug: "trump-approval-above-43-ladder-prices-below-8-2026-09-20"
headline: "Trump approval above 43%: ladder prices below 8%"
semantic_title: "Trump approval above 43 percent stays near fully priced out"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-20T09:46:15.297Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating level"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.084
  volume_24h_usd: 42.53
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "The approval rating ladder puts only 8% odds on Trump's rating exceeding 43%, with probability collapsing to 6% at 44% and staying flat through 50%, implying the market sees his approval firmly below 43%."
  - "The record-high disapproval figures in the ABC/Ipsos poll are consistent with the ladder's near-zero pricing above 43%; the news and the market are aligned."
  - "A companion ladder on Trump's approval falling below 33% prices that outcome at only 10%, implying the market consensus clusters his approval in the 33-43% range."
  - "Resolution anchors to a named approval-rating polling aggregator; no single poll is sufficient, smoothing out any one-off outlier reading."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A new ABC News/Washington Post/Ipsos poll found two-thirds of Americans say the country is headed in the wrong direction, with Trump's disapproval hitting new records."
    publisher: "ABC News"
    published_at: "2026-09-20T09:46:15.297Z"
    source_url: "https://abcnews.com/Politics/thirds-americans-country-headed-wrong-direction-abc-newswashington/story?id=132583099"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/Politics/thirds-americans-country-headed-wrong-direction-abc-newswashington/story?id=132583099"
        retrieved_at: "2026-09-21T07:47:18+00:00"
  - type: "pm_response"
    notes: "Ladder distributes probability across approval level strikes; current pricing firmly clusters Trump's approval in the low-to-mid 30s range with no path above 43%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: Two-thirds of Americans say country is headed in the wrong direction:"
    url: "https://abcnews.com/Politics/thirds-americans-country-headed-wrong-direction-abc-newswashington/story?id=132583099"
    published_at: "2026-09-20T09:46:15.297Z"
    retrieved_at: "2026-09-21T07:47:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
