---
signal_id: "CMSIG2026062506"
signal_slug: "any-hormuz-ship-transit-by-june-30-polymarket-28-2026-06-25"
headline: "Any Hormuz ship transit by June 30: Polymarket 28%"
semantic_title: "Any Hormuz transit by June 30 consensus wavers at long-shot"
telemetry: "Polymarket 28%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-25T21:47:54.000Z"
event_id: "CM-EVT-VB1YHPRLZ3"
event_slug: "will-ships-transit-the-strait-of-hormuz-on-any-day-by-june-30"
event_question: "Will any ships transit the Strait of Hormuz by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc38b96e6fb12fc68d003ff326f2a11eb3c8f04c2fce7fcfc9d62f5e18131817c"
  question_raw: "Will 60 ships transit the Strait of Hormuz on any day by June 30, 2026?"
  current_price: 0.28
  volume_24h_usd: 18035.20589
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T16:00:00Z"
bullets:
  - "Polymarket prices only 28% on any ships transiting the Strait of Hormuz by June 30, consistent with the UN halting its evacuation plan after the attack."
  - "The UN suspension of evacuation operations directly reinforces the below-50% pricing on near-term transit resumption."
  - "The June 30 unrestricted-shipping contract at 31% and this any-transit contract at 28% are closely clustered, suggesting the market sees even minimal transit as uncertain."
  - "Resolves via portwatch.imf.org traffic data; the IMF's port-watch feed is the named settlement source, giving the contract an objective, delay-resistant resolution path."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The UN paused its evacuation of trapped mariners in the Strait of Hormuz after Iran struck a commercial vessel, halting corridor-reopening efforts."
    publisher: "abc.net.au"
    published_at: "2026-06-25T21:47:54.000Z"
    source_url: "https://www.abc.net.au/news/2026-06-26/hormuz-strait-ship-attack-prompts-un-to-pause-evacuation/106843940"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "abc.net.au"
        source_url: "https://www.abc.net.au/news/2026-06-26/hormuz-strait-ship-attack-prompts-un-to-pause-evacuation/106843940"
        retrieved_at: "2026-06-26T10:48:01+00:00"
  - type: "pm_response"
    notes: "Polymarket's 28% on any transit by June 30 is directionally aligned with the UN pause, treating corridor reopening as a low-probability event this month."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "abc.net.au: UN pauses Strait of Hormuz evacuation after ship reports attack - ABC"
    url: "https://www.abc.net.au/news/2026-06-26/hormuz-strait-ship-attack-prompts-un-to-pause-evacuation/106843940"
    published_at: "2026-06-25T21:47:54.000Z"
    retrieved_at: "2026-06-26T10:48:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
