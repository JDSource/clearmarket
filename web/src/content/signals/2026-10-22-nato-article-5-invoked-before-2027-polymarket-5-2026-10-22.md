---
signal_id: "CMSIG2026102208"
signal_slug: "nato-article-5-invoked-before-2027-polymarket-5-2026-10-22"
headline: "NATO Article 5 invoked before 2027: Polymarket 5%"
semantic_title: "NATO Article 5 invocation before 2027 stays a long shot"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-22T00:00:00.000Z"
event_id: "CM-EVT-4WNT5S6CN2"
event_slug: "nato-article-5-before-2027"
event_question: "Will NATO Article 5 be invoked before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe7743a393cd98bb7a7cd011361b74a0fd12bac3412643873f4661fcc431ed165"
  question_raw: "NATO article 5 before 2027?"
  current_price: 0.054
  volume_24h_usd: 130.250863
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 5% odds on NATO invoking Article 5 before 2027."
  - "The Hague defense spending pledge signals alliance cohesion, but Polymarket's 5% reading shows markets see elevated commitment as a deterrent, not a sign of imminent invocation."
  - "Ukraine joining NATO before 2027 (Polymarket CM-EVT-5C5D7LP6B5) sits at just 2%, consistent with the market treating the alliance's expansion as a long-run rather than near-term event."
  - "Resolves via UMA oracle; invocation requires a formal NATO council determination that an attack on one member has occurred."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "NATO allies at The Hague summit endorsed a plan to spend 5 percent of GDP on defense by 2035 and reaffirmed collective defense commitments."
    publisher: "link.cfr.org"
    published_at: "2026-10-22T00:00:00.000Z"
    source_url: "https://link.cfr.org/public/40432428"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "link.cfr.org"
        source_url: "https://link.cfr.org/public/40432428"
        retrieved_at: "2026-10-23T07:48:07+00:00"
  - type: "pm_response"
    notes: "Polymarket at 5% treats the defense spending surge as alliance reinforcement rather than a signal of imminent conflict escalation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "link.cfr.org: Across the Globe"
    url: "https://link.cfr.org/public/40432428"
    published_at: "2026-10-22T00:00:00.000Z"
    retrieved_at: "2026-10-23T07:48:07+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
