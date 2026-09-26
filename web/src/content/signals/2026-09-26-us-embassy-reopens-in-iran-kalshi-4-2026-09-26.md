---
signal_id: "CMSIG2026092602"
signal_slug: "us-embassy-reopens-in-iran-kalshi-4-2026-09-26"
headline: "US embassy reopens in Iran: Kalshi 4%"
semantic_title: "US embassy in Iran remains a long shot at 4%"
telemetry: "Kalshi 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-26T00:00:00.000Z"
event_id: "CM-EVT-34SYT4T2T1"
event_slug: "kxiranembassy-27"
event_question: "Will the United States reopen its embassy in Iran?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXIRANEMBASSY-27"
  question_raw: "Will the US reopen its embassy in Iran before Jan 1, 2027?"
  current_price: 0.037
  volume_24h_usd: 166.73
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only a 4% chance the United States reopens its embassy in Iran, per The New York Times resolution source."
  - "Trump's rejection of Iran's peace plan aligns with the market's near-zero odds on any formal diplomatic normalization."
  - "Trading volume on CM-EVT-38HGT3RJ52 (US obtaining Iranian enriched uranium) surged approximately 1,000x day-over-day, indicating fresh speculative interest in the conflict's trajectory."
  - "Polymarket's 22% on Hormuz traffic returning to normal by December 31 sets an upper bound for how optimistic markets are on any Iran breakthrough this year."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Iran is awaiting a US move after a WSJ report indicated Trump rejected Iran's peace plan, stalling any diplomatic normalization."
    publisher: "Menna Alaaeldin"
    published_at: "2026-09-26T00:00:00.000Z"
    source_url: "https://www.reuters.com/world/middle-east/iran-awaits-us-move-after-wsj-report-says-trump-rejects-peace-plan-2026-09-26/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Menna Alaaeldin"
        source_url: "https://www.reuters.com/world/middle-east/iran-awaits-us-move-after-wsj-report-says-trump-rejects-peace-plan-2026-09-26/"
        retrieved_at: "2026-09-26T12:39:23+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via The New York Times; at 4%, the market treats full US-Iran normalization as a remote tail event."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Menna Alaaeldin: Iran awaits US move after WSJ report says Trump rejects peace plan | R"
    url: "https://www.reuters.com/world/middle-east/iran-awaits-us-move-after-wsj-report-says-trump-rejects-peace-plan-2026-09-26/"
    published_at: "2026-09-26T00:00:00.000Z"
    retrieved_at: "2026-09-26T12:39:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
