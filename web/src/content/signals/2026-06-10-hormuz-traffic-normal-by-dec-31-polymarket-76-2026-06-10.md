---
signal_id: "CMSIG2026061003"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-76-2026-06-10"
headline: "Hormuz traffic normal by Dec 31: Polymarket 76%"
semantic_title: "Hormuz traffic normal by December holds above three-quarters"
telemetry: "Polymarket 76%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-10T09:16:09.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will traffic through the Strait of Hormuz return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.76
  volume_24h_usd: 24270.863375000004
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by December 31 at 76%, despite active US-Iran military exchanges."
  - "The news of Iran striking US bases is consistent with near-term disruption, yet the market maintains a strong majority view that normalcy returns within six months."
  - "The June 30 normal-traffic contract sits at only 20%, reflecting near-zero confidence in a rapid resolution but leaving December odds elevated."
  - "Resolves via portwatch.imf.org shipping data; a sustained blockade or mine-laying campaign would be required to push the December contract materially lower."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran attacked US bases in Jordan and Bahrain, marking a major setback to truce talks and raising fresh doubts about Strait of Hormuz shipping."
    publisher: "Eoghan Dalton"
    published_at: "2026-06-10T09:16:09.000Z"
    source_url: "https://www.thejournal.ie/iran-us-2-7066011-Jun2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Eoghan Dalton"
        source_url: "https://www.thejournal.ie/iran-us-2-7066011-Jun2026/"
        retrieved_at: "2026-06-10T11:36:47+00:00"
  - type: "pm_response"
    notes: "Polymarket's 76% December read versus 20% for end-June implies traders price the conflict as a weeks-to-months disruption, not a structural closure of the strait."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Eoghan Dalton: Iran attacks US army bases in Jordan and Bahrain in latest setback to"
    url: "https://www.thejournal.ie/iran-us-2-7066011-Jun2026/"
    published_at: "2026-06-10T09:16:09.000Z"
    retrieved_at: "2026-06-10T11:36:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
