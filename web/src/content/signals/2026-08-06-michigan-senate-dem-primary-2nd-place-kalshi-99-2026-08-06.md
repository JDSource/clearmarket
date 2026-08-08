---
signal_id: "CMSIG2026080606"
signal_slug: "michigan-senate-dem-primary-2nd-place-kalshi-99-2026-08-06"
headline: "Michigan Senate Dem primary 2nd place: Kalshi 99%"
semantic_title: "Second place in Michigan Senate Democratic primary near certain"
telemetry: "Kalshi 99%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-08-06T08:34:16.391Z"
event_id: "CM-EVT-KW32LYSWB7"
event_slug: "kxprimaryplace-senatemid26-2"
event_question: "Who will finish in second place in the Michigan Senate Democratic primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-SENATEMID26-2-HSTE"
  question_raw: "Will Haley Stevens finish 2nd in the 2026 Michigan Senate Democratic primary?"
  current_price: 0.99
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "official election authority responsible for certifying results in geography"
  resolves_at: "2027-08-04T14:00:00Z"
bullets:
  - "Kalshi contract on who finishes second in the Michigan Senate Democratic primary is at 99%, effectively resolved."
  - "El-Sayed won; Stevens is the near-certain second-place finisher per the AP call cited in the news."
  - "El-Sayed now faces Republican Mike Rogers in a general election that could decide Senate control, a race not yet fully priced by related markets."
  - "Resolves via the official election authority responsible for certifying the Michigan primary results."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Left-wing candidate Abdul El-Sayed won the Michigan Democratic Senate primary, defeating Rep. Haley Stevens."
    publisher: "BBC"
    published_at: "2026-08-06T08:34:16.391Z"
    source_url: "https://www.bbc.com/news/articles/ckgdkpz07kvo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "BBC"
        source_url: "https://www.bbc.com/news/articles/ckgdkpz07kvo"
        retrieved_at: "2026-08-08T08:35:11+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 99%; effectively a live resolution play given the AP call."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "BBC: Left-wing political outsider wins Democratic Senate primary in Michiga"
    url: "https://www.bbc.com/news/articles/ckgdkpz07kvo"
    published_at: "2026-08-06T08:34:16.391Z"
    retrieved_at: "2026-08-08T08:35:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
