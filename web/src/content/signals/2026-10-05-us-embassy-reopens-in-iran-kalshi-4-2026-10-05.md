---
signal_id: "CMSIG2026100508"
signal_slug: "us-embassy-reopens-in-iran-kalshi-4-2026-10-05"
headline: "US embassy reopens in Iran: Kalshi 4%"
semantic_title: "US embassy reopening in Iran stays a very long shot"
telemetry: "Kalshi 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-05T00:00:00.000Z"
event_id: "CM-EVT-34SYT4T2T1"
event_slug: "kxiranembassy-27"
event_question: "Will the United States reopen its embassy in Iran?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXIRANEMBASSY-27"
  question_raw: "Will the US reopen its embassy in Iran before Jan 1, 2027?"
  current_price: 0.038
  volume_24h_usd: 11.31
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 4% on the United States reopening its embassy in Iran, with volume up 7,372% day over day -- a massive surge in trading activity signaling fresh attention."
  - "High-level Switzerland talks are drawing market interest, but the 4% price shows participants view full diplomatic normalization as extremely unlikely in the current conflict context."
  - "The Kalshi contract on Iran agreeing to end uranium enrichment by December 31 sits at 13% on Polymarket, implying a hierarchy: enrichment deal possible but embassy reopening seen as a far more distant step."
  - "Resolution source is The New York Times; the contract likely requires a formal, publicly announced US decision to reopen or reestablish an embassy in Tehran."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US Vice President JD Vance and Iranian Foreign Minister Abbas Araghchi opened formal ceasefire negotiations in Switzerland even as the US military conducted strikes on Iranian territory."
    publisher: "cnnbc.com"
    published_at: "2026-10-05T00:00:00.000Z"
    source_url: "https://cnnbc.com/iran-and-united-states-begin-high-level-talks-in-switzerland-to-finalize-interim-ceasefire-agreement"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cnnbc.com"
        source_url: "https://cnnbc.com/iran-and-united-states-begin-high-level-talks-in-switzerland-to-finalize-interim-ceasefire-agreement"
        retrieved_at: "2026-10-05T07:47:16+00:00"
  - type: "pm_response"
    notes: "Kalshi at 4% with volume surging 74.7x day over day -- the talks are attracting heavy market attention even as the probability holds at a long-shot level."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cnnbc.com: Iran and United States Begin High-Level Talks in Switzerland to Finali"
    url: "https://cnnbc.com/iran-and-united-states-begin-high-level-talks-in-switzerland-to-finalize-interim-ceasefire-agreement"
    published_at: "2026-10-05T00:00:00.000Z"
    retrieved_at: "2026-10-05T07:47:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
