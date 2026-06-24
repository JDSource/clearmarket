---
signal_id: "CMSIG2026062404"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-51-2026-06-24"
headline: "US-Iran nuclear deal by June 30: Polymarket 51%"
semantic_title: "US-Iran nuclear deal by June 30 pricing wavers near coin-flip"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T09:41:25.000Z"
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
  - "Polymarket prices the US-Iran nuclear deal by June 30 at 51%, essentially a coin-flip with only six days remaining."
  - "IAEA confirmation of inspector access is a positive signal, but the public US-Iran dispute over inspection terms keeps the market split."
  - "The July 31 contract (CM-EVT-Y2L01CWLW3) sits at 59%, implying only an 8-point premium for an extra month, signaling compressed timeline doubt."
  - "Resolves via UMA oracle; a formal signed agreement before June 30 close-of-day is required, not just technical-level arrangements."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "IAEA chief confirmed inspectors will visit Iranian nuclear sites under an interim US-Iran deal, though the two sides publicly dispute inspection scope."
    publisher: "By MARI YAMAGUCHI and JON GAMBRELL"
    published_at: "2026-06-24T09:41:25.000Z"
    source_url: "https://www.the-journal.com/articles/un-nuclear-agency-boss-says-inspectors-will-visit-irans-nuclear-sites-under-iran-us-interim-deal/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "By MARI YAMAGUCHI and JON GAMBRELL"
        source_url: "https://www.the-journal.com/articles/un-nuclear-agency-boss-says-inspectors-will-visit-irans-nuclear-sites-under-iran-us-interim-deal/"
        retrieved_at: "2026-06-24T10:45:49+00:00"
  - type: "pm_response"
    notes: "Polymarket's June 30 (51%) and July 31 (59%) contracts show a flat term structure, suggesting the market assigns most probability mass to a near-term resolution or none at all."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "By MARI YAMAGUCHI and JON GAMBRELL: UN nuclear agency boss says inspectors will visit Iran's nuclear sites"
    url: "https://www.the-journal.com/articles/un-nuclear-agency-boss-says-inspectors-will-visit-irans-nuclear-sites-under-iran-us-interim-deal/"
    published_at: "2026-06-24T09:41:25.000Z"
    retrieved_at: "2026-06-24T10:45:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
