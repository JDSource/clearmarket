---
signal_id: "CMSIG2026080506"
signal_slug: "mi-senate-dem-primary-2nd-place-kalshi-99-2026-08-05"
headline: "MI Senate Dem primary 2nd place: Kalshi 99%"
semantic_title: "Michigan Senate Democratic primary second-place finish near fully priced"
telemetry: "Kalshi 99%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-08-05T16:34:06.425Z"
event_id: "CM-EVT-KW32LYSWB7"
event_slug: "kxprimaryplace-senatemid26-2"
event_question: "Who will finish in second place in the Michigan Senate Democratic primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-SENATEMID26-2-HSTE"
  question_raw: "Will Haley Stevens finish 2nd in the 2026 Michigan Senate Democratic primary?"
  current_price: 0.99
  volume_24h_usd: 1232.08
  arbitration_model: "kalshi_staff"
  resolution_source: "official election authority responsible for certifying results in geography"
  resolves_at: "2027-08-04T14:00:00Z"
bullets:
  - "Kalshi prices 99% on the Michigan Senate Democratic primary second-place finisher being determined, with trading volume up 276x day-over-day, a near-certain settlement."
  - "El-Sayed's victory over Stevens is the catalyst; at 99%, Kalshi treats the result as effectively resolved."
  - "Volume surging 276x day-over-day confirms this was a heavily traded event on primary night as results came in."
  - "Kalshi also prices 81% on El-Sayed, Flanagan, and Hong all winning their respective primaries (CM-EVT-DKZGD9P320), implying the broader progressive slate outcome is not yet fully settled."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Progressive candidate Abdul El-Sayed won the Michigan Democratic Senate primary, defeating moderate U.S. Representative Haley Stevens in a close race."
    publisher: "BBC"
    published_at: "2026-08-05T16:34:06.425Z"
    source_url: "https://www.bbc.com/news/articles/ckgdkpz07kvo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "BBC"
        source_url: "https://www.bbc.com/news/articles/ckgdkpz07kvo"
        retrieved_at: "2026-08-06T10:35:15+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via official election authority; the 276x volume spike reflects primary-night settlement activity on August 4-5."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "BBC: Left-wing political outsider wins Democratic Senate primary in Michiga"
    url: "https://www.bbc.com/news/articles/ckgdkpz07kvo"
    published_at: "2026-08-05T16:34:06.425Z"
    retrieved_at: "2026-08-06T10:35:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
