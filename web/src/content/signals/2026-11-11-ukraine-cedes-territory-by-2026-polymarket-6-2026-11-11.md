---
signal_id: "CMSIG2026111107"
signal_slug: "ukraine-cedes-territory-by-2026-polymarket-6-2026-11-11"
headline: "Ukraine cedes territory by 2026: Polymarket 6%"
semantic_title: "Ukraine agreeing to cede territory by 2026 stays a long shot"
telemetry: "Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-11T01:08:22.000Z"
event_id: "CM-EVT-XP7FFT2MC9"
event_slug: "will-ukraine-agree-to-cede-territory-to-russia-before-2027"
event_question: "Will Ukraine agree to cede territory to Russia by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x21bf9a7dae81b6bd51acae73185686ab8997b81b1401e4be10e114d472599c26"
  question_raw: "Will Ukraine agree to cede territory to Russia before 2027?"
  current_price: 0.065
  volume_24h_usd: 810.495895
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Ukraine agreeing to cede territory to Russia by 2026 sits at 6%."
  - "Zelenskyy's public framing of Putin as disconnected from reality signals Kyiv is not moving toward concessions; the 6% price is consistent with this posture."
  - "The 7% peace deal contract and 4% Donbas-cession contract on Polymarket form a coherent cluster: all three put the probability of a breakthrough in single digits."
  - "Resolves via UMA oracle; requires a formal public Ukrainian agreement to transfer sovereign territory to Russia before the 2026 year-end deadline."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukrainian President Volodymyr Zelenskyy said Putin lives in a different reality as Abu Dhabi trilateral talks got underway with no territorial concessions signaled."
    publisher: "Guardian staff"
    published_at: "2026-11-11T01:08:22.000Z"
    source_url: "https://www.theguardian.com/world/2026/nov/11/ukraine-war-briefing-zelenskyy-says-putin-lives-in-a-different-reality-as-abu-dhabi-talks-get-under-way"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Guardian staff"
        source_url: "https://www.theguardian.com/world/2026/nov/11/ukraine-war-briefing-zelenskyy-says-putin-lives-in-a-different-reality-as-abu-dhabi-talks-get-under-way"
        retrieved_at: "2026-11-11T07:47:31+00:00"
  - type: "pm_response"
    notes: "Polymarket holds at 6%, unchanged by two days of Abu Dhabi talks, reflecting deep skepticism about a territorial deal materializing in 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Guardian staff: Ukraine war briefing: Zelenskyy says Putin ‘lives in a different reali"
    url: "https://www.theguardian.com/world/2026/nov/11/ukraine-war-briefing-zelenskyy-says-putin-lives-in-a-different-reality-as-abu-dhabi-talks-get-under-way"
    published_at: "2026-11-11T01:08:22.000Z"
    retrieved_at: "2026-11-11T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
