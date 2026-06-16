---
signal_id: "CMSIG2026061603"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-51-2026-06-16"
headline: "US-Iran nuclear deal by June 30: Polymarket 51%"
semantic_title: "US-Iran nuclear deal by June 30 wavers near coin flip"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-16T10:19:23.000Z"
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
  - "Polymarket prices a 51% probability the US and Iran reach a formal nuclear deal by June 30."
  - "Iran's announcement of talks beginning this week is consistent with the near-50% pricing: a process start, not a completed deal, within 14 days."
  - "The July 31 contract (CM-EVT-Y2L01CWLW3) sits at 59%, suggesting the extra month adds meaningful probability but uncertainty remains substantial."
  - "Separately, the uranium enrichment end contract (CM-EVT-8SWDJJDJM0) prices only 29% by July 31, flagging the nuclear terms as the hard sticking point."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran confirmed final-deal talks will begin this week inside a 60-day window after the memorandum of understanding is physically signed."
    publisher: "france24.com"
    published_at: "2026-06-16T10:19:23.000Z"
    source_url: "https://www.france24.com/en/live-news/20260616-iran-says-talks-on-final-us-deal-to-begin-this-week"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "france24.com"
        source_url: "https://www.france24.com/en/live-news/20260616-iran-says-talks-on-final-us-deal-to-begin-this-week"
        retrieved_at: "2026-06-16T12:50:14+00:00"
  - type: "pm_response"
    notes: "Polymarket's June 30 and July 31 contracts together map a term structure showing deal completion is a drawn-out probability, not an imminent certainty."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "france24.com: Iran says talks on final US deal to begin this week"
    url: "https://www.france24.com/en/live-news/20260616-iran-says-talks-on-final-us-deal-to-begin-this-week"
    published_at: "2026-06-16T10:19:23.000Z"
    retrieved_at: "2026-06-16T12:50:14+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
