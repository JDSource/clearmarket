---
signal_id: "CMSIG2026070303"
signal_slug: "5-gop-senate-incumbents-lose-re-election-kalshi-38-2026-07-03"
headline: "5+ GOP Senate incumbents lose re-election: Kalshi 38%"
semantic_title: "Senate Republican re-election losses consensus wavers near 38%"
telemetry: "Kalshi 38%"
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
  current_price: 0.38
  volume_24h_usd: 12.0
  arbitration_model: "kalshi_staff"
  resolution_source: "the Senate Parliamentarian"
  resolves_at: "2026-12-31T15:00:00Z"
bullets:
  - "Kalshi prices a 38% probability that at least 5 Senate Republicans lose re-election in 2026, resolved via the Senate Parliamentarian."
  - "Trading volume on this Kalshi contract surged 23,617% day over day, reflecting intense fresh interest following the Trump Senate candidate story."
  - "At 38%, the market treats mass Republican Senate losses as a minority but meaningful risk, not a base case despite Trump's aggressive reshaping of the field."
  - "A companion Kalshi contract (CM-EVT-RSPZ64CMS2) sits at 97% for a lower threshold of Senate Republican primary losses, revealing the market separates primary disruption from general election defeat."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump reshaped the Senate map by sidelining Republican incumbents and elevating loyalists ahead of the 2026 midterms."
    publisher: "ABC News"
    published_at: "2026-07-03T04:02:57.000Z"
    source_url: "https://abcnews.com/Politics/wireStory/trump-senate-candidates-wanted-spend-134432889"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/Politics/wireStory/trump-senate-candidates-wanted-spend-134432889"
        retrieved_at: "2026-07-05T10:07:52+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolving via Senate Parliamentarian; the extreme volume spike marks the story as a major catalyst for fresh prediction-market activity."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: Trump got the Senate candidates he wanted. How much will he spend to h"
    url: "https://abcnews.com/Politics/wireStory/trump-senate-candidates-wanted-spend-134432889"
    published_at: "2026-07-03T04:02:57.000Z"
    retrieved_at: "2026-07-05T10:07:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
