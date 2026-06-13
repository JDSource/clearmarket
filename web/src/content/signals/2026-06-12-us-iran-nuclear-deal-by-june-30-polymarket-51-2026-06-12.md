---
signal_id: "CMSIG2026061201"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-51-2026-06-12"
headline: "US-Iran nuclear deal by June 30: Polymarket 51%"
semantic_title: "US-Iran nuclear deal by June 30 sits at a coin flip"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-12T04:05:15.000Z"
event_id: "CM-EVT-LG47Z78CF2"
event_slug: "us-iran-nuclear-deal-by-june-30"
event_question: "Will the US and Iran reach a nuclear deal by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa70fc3695a65833b91b45df6db6015096f3e1471b70352ca411b4209010e7633"
  question_raw: "US-Iran nuclear deal by June 30?"
  current_price: 0.51
  volume_24h_usd: 1088905.717404001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices the US-Iran nuclear deal by June 30 at 51%, a near-even split."
  - "Multiple official signals of imminent signing push the market to a slight lean toward yes, but far from conviction."
  - "Companion Polymarket contract on Hormuz traffic returning to normal by end of June sits at only 18%, flagging market skepticism that a deal translates quickly to restored shipping."
  - "Resolves via UMA oracle; disputed or partial agreements could complicate settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump and Iranian officials signal a war-ending agreement is imminent, with a potential signing in Geneva on June 14."
    publisher: "ABC News"
    published_at: "2026-06-12T04:05:15.000Z"
    source_url: "https://abcnews.com/US/wireStory/trump-raising-expectations-time-close-deal-iran-wind-133806942"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/US/wireStory/trump-raising-expectations-time-close-deal-iran-wind-133806942"
        retrieved_at: "2026-06-13T10:25:37+00:00"
  - type: "pm_response"
    notes: "Polymarket prices the near-term deal probability at 51%, consistent with official optimism but reflecting persistent execution uncertainty."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: Trump is raising expectations that this time he really will close deal"
    url: "https://abcnews.com/US/wireStory/trump-raising-expectations-time-close-deal-iran-wind-133806942"
    published_at: "2026-06-12T04:05:15.000Z"
    retrieved_at: "2026-06-13T10:25:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
