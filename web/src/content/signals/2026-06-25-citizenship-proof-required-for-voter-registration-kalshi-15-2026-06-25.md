---
signal_id: "CMSIG2026062507"
signal_slug: "citizenship-proof-required-for-voter-registration-kalshi-15-2026-06-25"
headline: "Citizenship proof required for voter registration: Kalshi 15%"
semantic_title: "Citizenship proof for federal voter registration wavers at low odds"
telemetry: "Kalshi 15%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-25T09:00:00.000Z"
event_id: "CM-EVT-G8CYMWNWC6"
event_slug: "kxelectionbill"
event_question: "Will proof of citizenship be required for federal voter registration?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXELECTIONBILL-27JAN01"
  question_raw: "Will legislation that requires proof of U.S. citizenship as a condition of registering to vote in federal elections become law before Jan 1, 2027?"
  current_price: 0.15
  volume_24h_usd: 897.5
  arbitration_model: "kalshi_staff"
  resolution_source: "White House"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 15% on proof of citizenship becoming a federal voter registration requirement, despite active White House pressure."
  - "Federal judges have blocked Trump's election executive orders, and Senate Republican resistance to the SAVE America Act is consistent with the low Kalshi probability."
  - "Companion Kalshi contract (CM-EVT-T5VXKJT451) at 40% on Republicans controlling at least one chamber after midterms suggests GOP legislative leverage is itself uncertain."
  - "Resolves via the White House; a formal regulatory or legislative implementation of the citizenship requirement triggers YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump refused to sign a bipartisan housing bill, demanding Congress pass the SAVE America Act requiring proof of citizenship for federal voter registration."
    publisher: "newstribune.com"
    published_at: "2026-06-25T09:00:00.000Z"
    source_url: "https://www.newstribune.com/news/2026/jun/25/trump-refuses-to-sign-landmark-housing-bill/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "newstribune.com"
        source_url: "https://www.newstribune.com/news/2026/jun/25/trump-refuses-to-sign-landmark-housing-bill/"
        retrieved_at: "2026-06-27T01:35:43+00:00"
  - type: "pm_response"
    notes: "Kalshi at 15% positions this as a long-shot legislative outcome despite Trump's public hostage-taking of the housing bill to extract the vote ID demand."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "newstribune.com: Trump refuses to sign landmark housing bill, demanding Congress pass v"
    url: "https://www.newstribune.com/news/2026/jun/25/trump-refuses-to-sign-landmark-housing-bill/"
    published_at: "2026-06-25T09:00:00.000Z"
    retrieved_at: "2026-06-27T01:35:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
