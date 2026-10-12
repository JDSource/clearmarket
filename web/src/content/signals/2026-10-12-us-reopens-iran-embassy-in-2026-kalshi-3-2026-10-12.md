---
signal_id: "CMSIG2026101206"
signal_slug: "us-reopens-iran-embassy-in-2026-kalshi-3-2026-10-12"
headline: "US reopens Iran embassy in 2026: Kalshi 3%"
semantic_title: "US reopening its embassy in Iran stays a long shot"
telemetry: "Kalshi 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-12T00:00:00.000Z"
event_id: "CM-EVT-34SYT4T2T1"
event_slug: "kxiranembassy-27"
event_question: "Will the United States reopen its embassy in Iran?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXIRANEMBASSY-27"
  question_raw: "Will the US reopen its embassy in Iran before Jan 1, 2027?"
  current_price: 0.026
  volume_24h_usd: 1.56
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi puts only 3% on the US reopening its embassy in Iran, resolved via The New York Times, reflecting deep skepticism about diplomatic normalization."
  - "High-level talks in Geneva represent a notable step, but the Kalshi pricing treats a formal diplomatic reopening as far beyond what early-stage ceasefire talks imply."
  - "A companion Kalshi contract on the US recognizing Reza Pahlavi as Iran's leader sits at 4%, similarly reflecting markets pricing no regime-change or normalization path."
  - "The Strait of Hormuz traffic returning to normal by December sits at 14% on Polymarket, suggesting markets see ongoing Iran tensions as the base case through year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US and Iranian delegations opened formal ceasefire negotiations in Switzerland, led by Vice President JD Vance and Iranian Foreign Minister Abbas Araghchi."
    publisher: "cnnbc.com"
    published_at: "2026-10-12T00:00:00.000Z"
    source_url: "https://cnnbc.com/iran-and-united-states-begin-high-level-talks-in-switzerland-to-finalize-interim-ceasefire-agreement"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cnnbc.com"
        source_url: "https://cnnbc.com/iran-and-united-states-begin-high-level-talks-in-switzerland-to-finalize-interim-ceasefire-agreement"
        retrieved_at: "2026-10-12T07:49:04+00:00"
  - type: "pm_response"
    notes: "Kalshi resolves the embassy contract via New York Times reporting; the low 3% reflects how far markets see formal normalization from current ceasefire-talk status."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cnnbc.com: Iran and United States Begin High-Level Talks in Switzerland to Finali"
    url: "https://cnnbc.com/iran-and-united-states-begin-high-level-talks-in-switzerland-to-finalize-interim-ceasefire-agreement"
    published_at: "2026-10-12T00:00:00.000Z"
    retrieved_at: "2026-10-12T07:49:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
