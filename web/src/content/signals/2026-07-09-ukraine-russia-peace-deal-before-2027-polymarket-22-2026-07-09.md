---
signal_id: "CMSIG2026070907"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-22-2026-07-09"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 22%"
semantic_title: "Ukraine peace deal before 2027 holds at deep discount"
telemetry: "Polymarket 22%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-09T09:58:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.22
  volume_24h_usd: 1017.811138
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices 22% on Ukraine signing a peace deal with Russia before 2027, resolved via UMA oracle."
  - "Kremlin-source reporting of likely escalation is consistent with the market's low peace-deal pricing; the two readings reinforce each other."
  - "Companion Polymarket contracts show only 6% on Ukraine giving up the rest of Donbas and 10% on a peace referendum passing before 2027, confirming the market sees no near-term settlement path."
  - "Resolves via UMA oracle using a publicly verifiable signed peace agreement; partial ceasefires or memoranda of understanding would not trigger resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Sources close to the Kremlin indicated Putin is likely to escalate the Ukraine war in coming months, rejecting peace talks despite Trump administration optimism."
    publisher: "thestar.com.my"
    published_at: "2026-07-09T09:58:00.000Z"
    source_url: "https://www.thestar.com.my/news/world/2026/07/09/exclusive-putin-likely-to-escalate-ukraine-war-despite-trump-peace-push-sources-say"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "thestar.com.my"
        source_url: "https://www.thestar.com.my/news/world/2026/07/09/exclusive-putin-likely-to-escalate-ukraine-war-despite-trump-peace-push-sources-say"
        retrieved_at: "2026-07-11T09:24:13+00:00"
  - type: "pm_response"
    notes: "Polymarket is the primary venue; the 6% Donbas-concession and 10% referendum contracts bracket the peace-deal probability, showing the market prices escalation as the base case."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "thestar.com.my: Exclusive-Putin likely to escalate Ukraine war, despite Trump peace pu"
    url: "https://www.thestar.com.my/news/world/2026/07/09/exclusive-putin-likely-to-escalate-ukraine-war-despite-trump-peace-push-sources-say"
    published_at: "2026-07-09T09:58:00.000Z"
    retrieved_at: "2026-07-11T09:24:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
