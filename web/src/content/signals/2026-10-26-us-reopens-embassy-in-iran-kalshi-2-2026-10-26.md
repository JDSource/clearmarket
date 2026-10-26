---
signal_id: "CMSIG2026102608"
signal_slug: "us-reopens-embassy-in-iran-kalshi-2-2026-10-26"
headline: "US reopens embassy in Iran: Kalshi 2%"
semantic_title: "US reopening Iran embassy stays close to zero probability"
telemetry: "Kalshi 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-26T13:20:19.000Z"
event_id: "CM-EVT-34SYT4T2T1"
event_slug: "kxiranembassy-27"
event_question: "Will the United States reopen its embassy in Iran?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXIRANEMBASSY-27"
  question_raw: "Will the US reopen its embassy in Iran before Jan 1, 2027?"
  current_price: 0.018
  volume_24h_usd: 2.29
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market prices the U.S. reopening its embassy in Iran at just 2%."
  - "Trading volume on this contract rose 14,724% day over day, a sharp surge consistent with the news that U.S. personnel are being drawn down, not redeployed, in the region."
  - "Embassy staff reductions and heightened alert are the opposite of normalization, making the 2% pricing directionally aligned with the news even as volume spikes on attention."
  - "Resolves via The New York Times as the named source; formal reopening would require a diplomatic breakthrough well beyond current conditions."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The U.S. government put Middle East embassy staff on heightened alert and moved to reduce personnel at embassies and consulates after intelligence showed Iran is preparing potential retaliatory action."
    publisher: "Ammanuel Desta"
    published_at: "2026-10-26T13:20:19.000Z"
    source_url: "https://www.justsecurity.org/162014/early-edition-october-26-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ammanuel Desta"
        source_url: "https://www.justsecurity.org/162014/early-edition-october-26-2026/"
        retrieved_at: "2026-10-26T14:48:08+00:00"
  - type: "pm_response"
    notes: "Kalshi at 2% with volume up nearly 148x day over day captures a market that is watching the Iran crisis intensify while keeping normalization firmly off the table."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ammanuel Desta: Early Edition: October 26, 2026"
    url: "https://www.justsecurity.org/162014/early-edition-october-26-2026/"
    published_at: "2026-10-26T13:20:19.000Z"
    retrieved_at: "2026-10-26T14:48:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
