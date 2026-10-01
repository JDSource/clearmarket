---
signal_id: "CMSIG2026100107"
signal_slug: "us-embassy-reopen-in-iran-kalshi-2-2026-10-01"
headline: "US embassy reopen in Iran: Kalshi 2%"
semantic_title: "US embassy reopening in Iran stays a long shot at 2 percent"
telemetry: "Kalshi 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-01T00:00:00.000Z"
event_id: "CM-EVT-34SYT4T2T1"
event_slug: "kxiranembassy-27"
event_question: "Will the United States reopen its embassy in Iran?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXIRANEMBASSY-27"
  question_raw: "Will the US reopen its embassy in Iran before Jan 1, 2027?"
  current_price: 0.024
  volume_24h_usd: 2.64
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices the US reopening its embassy in Iran at 2%, consistent with near-complete market skepticism about a diplomatic breakthrough."
  - "Iran readying retaliatory posture and Trump's threat to strike Tehran are fully consistent with this near-zero probability; market and news are aligned."
  - "A separate Kalshi contract on the US recognizing Reza Pahlavi as Iran's leader sits at 4%, also negligible, framing the entire Iran diplomatic spectrum as a long shot."
  - "Kalshi resolves via the New York Times; the low base rate means even a credible preliminary deal announcement would likely produce sharp repricing from a very low starting point."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Iran is readying harder retaliation if attacked as US-Iran diplomacy faces long odds, with both sides believing they hold sufficient leverage."
    publisher: "Parisa Hafezi"
    published_at: "2026-10-01T00:00:00.000Z"
    source_url: "https://www.al-monitor.com/originals/2026/10/iran-readies-harder-retaliation-if-attacked-diplomacy-faces-long-odds"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Parisa Hafezi"
        source_url: "https://www.al-monitor.com/originals/2026/10/iran-readies-harder-retaliation-if-attacked-diplomacy-faces-long-odds"
        retrieved_at: "2026-10-01T15:03:15+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via the New York Times; at 2%, this is one of the most one-sided political contracts in the current batch, pricing out any near-term normalization scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Parisa Hafezi: Iran readies harder retaliation if attacked as diplomacy faces long od"
    url: "https://www.al-monitor.com/originals/2026/10/iran-readies-harder-retaliation-if-attacked-diplomacy-faces-long-odds"
    published_at: "2026-10-01T00:00:00.000Z"
    retrieved_at: "2026-10-01T15:03:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
