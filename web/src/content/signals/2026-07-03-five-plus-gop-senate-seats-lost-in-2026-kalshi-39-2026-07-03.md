---
signal_id: "CMSIG2026070308"
signal_slug: "five-plus-gop-senate-seats-lost-in-2026-kalshi-39-2026-07-03"
headline: "Five-plus GOP Senate seats lost in 2026: Kalshi 39%"
semantic_title: "Five or more Senate Republicans losing re-election wavers below coin flip"
telemetry: "Kalshi 39%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-03T04:02:57.000Z"
event_id: "CM-EVT-39Y2BB24Y8"
event_slug: "kxlosereelectionrsen-2026"
event_question: "Will at least 5 the Senate Republicans lose re-election in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLOSEREELECTIONRSEN-2026-5"
  question_raw: "Will at least 5 the Senate Republicans lose re-election in 2026?"
  current_price: 0.39
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "the Senate Parliamentarian"
  resolves_at: "2026-12-31T15:00:00Z"
bullets:
  - "The Kalshi prediction market puts 39% on at least five Senate Republicans losing re-election in 2026."
  - "Trump's success in installing loyalist candidates may boost primary turnout but introduces general-election vulnerability, the 39% reading reflects genuine uncertainty about that tradeoff."
  - "Companion Kalshi contract CM-EVT-RSPZ64CMS2 prices 92% on more than some threshold of Republicans losing their primary, suggesting primary disruption is near-fully priced while general-election losses remain contested."
  - "Kalshi contract resolves via the Senate Parliamentarian's certification of election results; the threshold of exactly five seats is a precise trigger that makes near-miss scenarios material to settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump reshaped the 2026 Senate map by sidelining incumbents and promoting loyalists, raising questions about how much he will spend to protect them."
    publisher: "ABC News"
    published_at: "2026-07-03T04:02:57.000Z"
    source_url: "https://abcnews.com/Politics/wireStory/trump-senate-candidates-wanted-spend-134432889"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/Politics/wireStory/trump-senate-candidates-wanted-spend-134432889"
        retrieved_at: "2026-07-03T10:32:12+00:00"
  - type: "pm_response"
    notes: "Kalshi binary at 39%; the 53-point gap versus companion CM-EVT-RSPZ64CMS2 at 92% reveals the market sees primary disruption as likely but general-election losses as a coin-flip."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: Trump got the Senate candidates he wanted. How much will he spend to h"
    url: "https://abcnews.com/Politics/wireStory/trump-senate-candidates-wanted-spend-134432889"
    published_at: "2026-07-03T04:02:57.000Z"
    retrieved_at: "2026-07-03T10:32:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
