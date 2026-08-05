---
signal_id: "CMSIG2026080506"
signal_slug: "michigan-senate-dem-primary-2nd-place-kalshi-99-2026-08-05"
headline: "Michigan Senate Dem primary 2nd place: Kalshi 99%"
semantic_title: "Second place in Michigan Senate Democratic primary stays near full pricing"
telemetry: "Kalshi 99%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-08-05T05:58:17.000Z"
event_id: "CM-EVT-KW32LYSWB7"
event_slug: "kxprimaryplace-senatemid26-2"
event_question: "Who will finish in second place in the Michigan Senate Democratic primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-SENATEMID26-2-HSTE"
  question_raw: "Will Haley Stevens finish 2nd in the 2026 Michigan Senate Democratic primary?"
  current_price: 0.99
  volume_24h_usd: 136661.19
  arbitration_model: "kalshi_staff"
  resolution_source: "official election authority responsible for certifying results in geography"
  resolves_at: "2027-08-04T14:00:00Z"
bullets:
  - "Kalshi contract on second place in the Michigan Senate Democratic primary sits at 99%, effectively fully resolved."
  - "El-Sayed's win is now reported by NBC News, making this a lagging market, the result is known and the contract is pricing a near-certain outcome."
  - "Resolution is via the official election authority responsible for certifying the result; no remaining uncertainty on the primary outcome."
  - "The companion Polymarket contract (CM-EVT-P54SDG6NP7) prices Democrats winning all four core Senate races at 55%, meaning the El-Sayed primary win is absorbed but general-election risk remains live."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Abdul El-Sayed won Michigan's Democratic Senate primary over Haley Stevens, notching a Midwest victory for the progressive left."
    publisher: "nbcnews.com"
    published_at: "2026-08-05T05:58:17.000Z"
    source_url: "https://www.nbcnews.com/politics/2026-election/abdul-el-sayed-wins-michigans-democratic-senate-primary-notching-midwe-rcna589750"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nbcnews.com"
        source_url: "https://www.nbcnews.com/politics/2026-election/abdul-el-sayed-wins-michigans-democratic-senate-primary-notching-midwe-rcna589750"
        retrieved_at: "2026-08-05T10:30:51+00:00"
  - type: "pm_response"
    notes: "Kalshi at 99% reflects a concluded primary; the contract is essentially in settlement territory pending official certification."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nbcnews.com: Abdul El-Sayed wins Michigan’s Democratic Senate primary, notching a M"
    url: "https://www.nbcnews.com/politics/2026-election/abdul-el-sayed-wins-michigans-democratic-senate-primary-notching-midwe-rcna589750"
    published_at: "2026-08-05T05:58:17.000Z"
    retrieved_at: "2026-08-05T10:30:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
