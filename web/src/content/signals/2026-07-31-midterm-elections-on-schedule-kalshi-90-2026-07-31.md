---
signal_id: "CMSIG2026073108"
signal_slug: "midterm-elections-on-schedule-kalshi-90-2026-07-31"
headline: "Midterm elections on schedule: Kalshi 90%"
semantic_title: "Midterm elections staying on schedule priced as near certainty"
telemetry: "Kalshi 90%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-31T00:00:00.000Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.9
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi prices 90% on the 2026 midterm elections happening on schedule."
  - "Despite the administration's earlier gutting of election security infrastructure and ongoing rebuilding efforts, markets see only a 10% chance of any delay or cancellation."
  - "Noncitizen voter roll claims by the Trump administration and rebuilding security gaps are narrative risks, but Kalshi's 90% reflects that legal and constitutional constraints make delay very unlikely."
  - "Kalshi resolves via The Washington Post; any official postponement or cancellation of a scheduled federal election would trigger a NO."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Trump administration is rebuilding election security infrastructure it had previously dismantled as the 2026 midterms approach."
    publisher: "Tierney Sneed, Sean Lyngaas, Evan Perez"
    published_at: "2026-07-31T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/07/31/politics/trump-admin-rebuild-election-security-months-after-gutting-it"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Tierney Sneed, Sean Lyngaas, Evan Perez"
        source_url: "https://www.cnn.com/2026/07/31/politics/trump-admin-rebuild-election-security-months-after-gutting-it"
        retrieved_at: "2026-08-01T09:54:52+00:00"
  - type: "pm_response"
    notes: "Kalshi at 90% treats election schedule disruption as a tail risk only, consistent with the constitutional difficulty of postponing federal elections."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Tierney Sneed, Sean Lyngaas, Evan Perez: Trump admin tries to rebuild election security infrastructure it gutte"
    url: "https://www.cnn.com/2026/07/31/politics/trump-admin-rebuild-election-security-months-after-gutting-it"
    published_at: "2026-07-31T00:00:00.000Z"
    retrieved_at: "2026-08-01T09:54:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
