---
signal_id: "CMSIG2026071506"
signal_slug: "us-recognizes-reza-pahlavi-as-iran-leader-by-2026-kalshi-8-2026-07-15"
headline: "US recognizes Reza Pahlavi as Iran leader by 2026: Kalshi 8%"
semantic_title: "Reza Pahlavi recognition consensus stays depressed amid active Iran war"
telemetry: "Kalshi 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-15T02:46:23.000Z"
event_id: "CM-EVT-SY50TZ6672"
event_slug: "kxrecogpersoniran-26"
event_question: "Will the United States recognize Reza Pahlavi as the leader of Iran by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRECOGPERSONIRAN-26"
  question_raw: "Will the United States recognize Reza Pahlavi as the leader of Iran in 2026?"
  current_price: 0.077
  volume_24h_usd: 7.79
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices US recognition of Reza Pahlavi as Iran's leader by 2026 at 8%, a low but non-trivial tail."
  - "Active US strikes on Iran focus on military and energy targets, not political transition, making formal recognition unlikely in the near term."
  - "Companion Polymarket contract CM-EVT-0SWQB28081 prices the same scenario at 4%, a 4-point gap across venues worth monitoring as a cross-venue spread."
  - "Resolves via ABC; recognition would require an explicit US government declaration, a high procedural bar."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump held a Situation Room meeting on massive new Iran strikes, with the US escalating military action rather than pursuing regime-change recognition."
    publisher: "Barak Ravid"
    published_at: "2026-07-15T02:46:23.000Z"
    source_url: "https://www.axios.com/2026/07/15/trump-situation-room-iran-bombing"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Barak Ravid"
        source_url: "https://www.axios.com/2026/07/15/trump-situation-room-iran-bombing"
        retrieved_at: "2026-07-15T10:00:10+00:00"
  - type: "pm_response"
    notes: "Kalshi at 8% versus Polymarket at 4% on the same scenario suggests modest cross-venue disagreement on a low-probability tail event."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Barak Ravid: Trump held Situation Room meeting on massive new Iran strikes"
    url: "https://www.axios.com/2026/07/15/trump-situation-room-iran-bombing"
    published_at: "2026-07-15T02:46:23.000Z"
    retrieved_at: "2026-07-15T10:00:10+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
