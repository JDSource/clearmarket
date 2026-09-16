---
signal_id: "CMSIG2026091605"
signal_slug: "russia-sanctions-bill-into-law-kalshi-84-2026-09-16"
headline: "Russia sanctions bill into law: Kalshi 84%"
semantic_title: "Russian sanctions bill becoming law holds near 84 percent"
telemetry: "Kalshi 84%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-16T00:00:00.000Z"
event_id: "CM-EVT-C6SL3Y8HY3"
event_slug: "kxsanctionrussia-26jan01"
event_question: "Will a Russian sanctions bill become law?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSANCTIONRUSSIA-26JAN01-27"
  question_raw: "Will a Russian sanctions bill become law before 2027?"
  current_price: 0.84
  volume_24h_usd: 447.54
  arbitration_model: "kalshi_staff"
  resolution_source: "White House"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract on a Russian sanctions bill becoming law sits at 84%, resolves via the White House signing record."
  - "House passage is consistent with the elevated 84% pricing; the remaining gap to 100% likely reflects Senate procedural and timeline risk."
  - "The bill's House advancement does not guarantee Senate passage or a presidential signature before year-end, which the 16% residual captures."
  - "No companion market with a Senate-specific contract is available in the provided data; the Kalshi contract is the primary pricing signal."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US House took up a sweeping Russia sanctions bill backed by the late Senator Lindsey Graham, advancing it through the chamber."
    publisher: "Patricia Zengerle"
    published_at: "2026-09-16T00:00:00.000Z"
    source_url: "https://www.reuters.com/legal/government/us-house-takes-up-russia-sanctions-bill-backed-by-late-senator-graham-2026-09-16/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Patricia Zengerle"
        source_url: "https://www.reuters.com/legal/government/us-house-takes-up-russia-sanctions-bill-backed-by-late-senator-graham-2026-09-16/"
        retrieved_at: "2026-09-16T13:02:46+00:00"
  - type: "pm_response"
    notes: "The Kalshi contract at 84% is consistent with House passage; resolution requires White House confirmation of a signed bill."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Patricia Zengerle: US House takes up Russia sanctions bill backed by late senator Graham"
    url: "https://www.reuters.com/legal/government/us-house-takes-up-russia-sanctions-bill-backed-by-late-senator-graham-2026-09-16/"
    published_at: "2026-09-16T00:00:00.000Z"
    retrieved_at: "2026-09-16T13:02:46+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
