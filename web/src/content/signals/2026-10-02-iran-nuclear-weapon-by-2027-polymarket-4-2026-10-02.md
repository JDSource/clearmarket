---
signal_id: "CMSIG2026100207"
signal_slug: "iran-nuclear-weapon-by-2027-polymarket-4-2026-10-02"
headline: "Iran nuclear weapon by 2027: Polymarket 4%"
semantic_title: "Iran nuclear weapon before 2027 stays a long shot"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-02T00:00:00.000Z"
event_id: "CM-EVT-RV9Z73GLB0"
event_slug: "iran-nuke-before-2027"
event_question: "Will Iran develop a nuclear weapon before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8bdeac60c92d3bc494792fd334ca181b0cf70355f23dca4098d558280b554c81"
  question_raw: "Iran Nuke before 2027?"
  current_price: 0.038
  volume_24h_usd: 3462.204447
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Iran developing a nuclear weapon before 2027 prices at 4%, pricing the scenario as a remote tail risk despite active military and diplomatic tensions."
  - "Israeli defense officials flag narrowing Iranian options under sanctions pressure, but the Polymarket contract at 4% suggests the market does not interpret this as a credible near-term nuclear breakout."
  - "A companion Kalshi contract on the U.S. and Iran reaching a final nuclear deal by 2026 has no live price, leaving the diplomatic resolution pathway unquantified."
  - "Resolves via UMA oracle; nuclear weapon development by Iran would need independent verification before year-end 2026, a very high evidentiary bar in the available timeline."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A senior Israeli defense official said Iran's options have narrowed amid U.S. sanctions, while Israel prepares for the possibility of an escalatory Iranian move."
    publisher: "AMIR BOHBOT"
    published_at: "2026-10-02T00:00:00.000Z"
    source_url: "https://www.jpost.com/middle-east/iran-news/article-910402"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AMIR BOHBOT"
        source_url: "https://www.jpost.com/middle-east/iran-news/article-910402"
        retrieved_at: "2026-10-02T14:25:25+00:00"
  - type: "pm_response"
    notes: "Polymarket at 4% on Iranian nuclear weapons before 2027 is consistent with elevated geopolitical tension but stops well short of pricing a credible near-term breakout scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AMIR BOHBOT: Iran weighs options as US pressure, nuclear impasse deepen | The Jerus"
    url: "https://www.jpost.com/middle-east/iran-news/article-910402"
    published_at: "2026-10-02T00:00:00.000Z"
    retrieved_at: "2026-10-02T14:25:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
