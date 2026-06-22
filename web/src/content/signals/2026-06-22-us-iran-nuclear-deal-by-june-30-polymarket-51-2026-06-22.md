---
signal_id: "CMSIG2026062201"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-51-2026-06-22"
headline: "US-Iran nuclear deal by June 30: Polymarket 51%"
semantic_title: "Nuclear deal by June 30 consensus wavers at midpoint"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-22T01:39:28.000Z"
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
  - "Polymarket prices the US-Iran nuclear deal by June 30 at 51%, a coin-flip reading despite reported major progress."
  - "Iran cited major progress and a 60-day roadmap, but the June 30 deadline is only 8 days away, explaining market hesitation."
  - "Technical talks continuing through the week keep the June 30 window alive but narrow; the 60-day roadmap points to a late-August finish."
  - "The Polymarket contract resolves via uma_oracle; a formal signed agreement, not a roadmap or statement, is likely required for YES resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran and the US agreed on a 60-day roadmap to a final deal after all-night Switzerland talks, with mediators Qatar and Pakistan confirming encouraging progress."
    publisher: "AFP"
    published_at: "2026-06-22T01:39:28.000Z"
    source_url: "https://www.timesofisrael.com/liveblog_entry/iran-us-agree-on-roadmap-to-reach-final-deal-in-60-days-talks-to-go-on-all-week-mediators-say/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AFP"
        source_url: "https://www.timesofisrael.com/liveblog_entry/iran-us-agree-on-roadmap-to-reach-final-deal-in-60-days-talks-to-go-on-all-week-mediators-say/"
        retrieved_at: "2026-06-22T13:32:28+00:00"
  - type: "pm_response"
    notes: "Polymarket at 51% reflects genuine uncertainty: positive headline flow is partially offset by the very short June 30 deadline against a 60-day stated timeline."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AFP: Iran, US agree on roadmap to reach final deal in 60 days, talks to go"
    url: "https://www.timesofisrael.com/liveblog_entry/iran-us-agree-on-roadmap-to-reach-final-deal-in-60-days-talks-to-go-on-all-week-mediators-say/"
    published_at: "2026-06-22T01:39:28.000Z"
    retrieved_at: "2026-06-22T13:32:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
