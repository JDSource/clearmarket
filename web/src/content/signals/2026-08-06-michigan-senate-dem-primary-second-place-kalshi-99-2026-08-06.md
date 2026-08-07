---
signal_id: "CMSIG2026080606"
signal_slug: "michigan-senate-dem-primary-second-place-kalshi-99-2026-08-06"
headline: "Michigan Senate Dem primary second place: Kalshi 99%"
semantic_title: "Michigan Senate Democratic primary second place near certain"
telemetry: "Kalshi 99%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-08-06T08:52:41.982Z"
event_id: "CM-EVT-KW32LYSWB7"
event_slug: "kxprimaryplace-senatemid26-2"
event_question: "Who will finish in second place in the Michigan Senate Democratic primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-SENATEMID26-2-HSTE"
  question_raw: "Will Haley Stevens finish 2nd in the 2026 Michigan Senate Democratic primary?"
  current_price: 0.99
  volume_24h_usd: 17.09
  arbitration_model: "kalshi_staff"
  resolution_source: "official election authority responsible for certifying results in geography"
  resolves_at: "2027-08-04T14:00:00Z"
bullets:
  - "The Kalshi contract on who finishes second in the Michigan Senate Democratic primary is priced at 99%, indicating the result is effectively settled."
  - "El-Sayed's confirmed primary win means the second-place finisher is also determined, making this contract consistent with the reported outcome."
  - "The primary result sets up a general election contest that will draw national attention given El-Sayed's progressive profile and Michigan's swing-state status."
  - "Resolves via the official election authority responsible for certifying Michigan primary results; at 99% the contract leaves minimal residual uncertainty."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Left-wing political outsider Abdul El-Sayed won the Democratic Senate primary in Michigan, according to BBC reporting."
    publisher: "BBC"
    published_at: "2026-08-06T08:52:41.982Z"
    source_url: "https://www.bbc.com/news/articles/ckgdkpz07kvo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "BBC"
        source_url: "https://www.bbc.com/news/articles/ckgdkpz07kvo"
        retrieved_at: "2026-08-07T08:53:43+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 99% resolves via official Michigan election certification; near-full pricing reflects reported outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "BBC: Left-wing political outsider wins Democratic Senate primary in Michiga"
    url: "https://www.bbc.com/news/articles/ckgdkpz07kvo"
    published_at: "2026-08-06T08:52:41.982Z"
    retrieved_at: "2026-08-07T08:53:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
