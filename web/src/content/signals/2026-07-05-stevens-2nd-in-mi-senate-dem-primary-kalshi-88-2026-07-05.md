---
signal_id: "CMSIG2026070507"
signal_slug: "stevens-2nd-in-mi-senate-dem-primary-kalshi-88-2026-07-05"
headline: "Stevens 2nd in MI Senate Dem primary: Kalshi 88%"
semantic_title: "Haley Stevens second-place Michigan primary finish hardens sharply"
telemetry: "Kalshi 88%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-05T18:03:12.000Z"
event_id: "CM-EVT-KW32LYSWB7"
event_slug: "kxprimaryplace-senatemid26-2"
event_question: "Will Haley Stevens finish 2nd in the 2026 Michigan Senate Democratic primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-SENATEMID26-2-HSTE"
  question_raw: "Will Haley Stevens finish 2nd in the 2026 Michigan Senate Democratic primary?"
  current_price: 0.88
  volume_24h_usd: 629.52
  arbitration_model: "kalshi_staff"
  resolution_source: "official election authority responsible for certifying results in geography"
  resolves_at: "2027-08-04T14:00:00Z"
bullets:
  - "Kalshi prices an 88% chance Haley Stevens finishes second in the 2026 Michigan Senate Democratic primary."
  - "McMorrow's suspension removes a top-tier competitor, which is consistent with the high probability on Stevens placing second."
  - "A separate Kalshi contract prices 63% on a Democrat winning the general Michigan Senate election, suggesting the seat remains competitive."
  - "Resolves via the official election authority responsible for certifying the Michigan primary result; a recount or certification delay could defer resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Michigan Democrat Mallory McMorrow suspended her U.S. Senate campaign, reshaping the Democratic primary field."
    publisher: "ABC News"
    published_at: "2026-07-05T18:03:12.000Z"
    source_url: "https://abcnews.com/Politics/wireStory/democrat-mallory-mcmorrow-suspends-michigan-senate-campaign-scrambles-134501095"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/Politics/wireStory/democrat-mallory-mcmorrow-suspends-michigan-senate-campaign-scrambles-134501095"
        retrieved_at: "2026-07-06T12:00:14+00:00"
  - type: "pm_response"
    notes: "Kalshi at 88% on Stevens for second reflects the primary field thinning after McMorrow's exit, with the general election outcome still a coin-flip at 63%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: Democrat Mallory McMorrow suspends her Michigan Senate campaign - ABC"
    url: "https://abcnews.com/Politics/wireStory/democrat-mallory-mcmorrow-suspends-michigan-senate-campaign-scrambles-134501095"
    published_at: "2026-07-05T18:03:12.000Z"
    retrieved_at: "2026-07-06T12:00:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
