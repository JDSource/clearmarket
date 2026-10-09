---
signal_id: "CMSIG2026100906"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-18-2026-10-09"
headline: "Hormuz traffic normal by Dec 31: Polymarket 18%"
semantic_title: "Strait of Hormuz returning to normal by year-end stays unlikely"
telemetry: "Polymarket 18%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-09T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.18
  volume_24h_usd: 71803.92267199999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 sits at 18%, resolving via UMA oracle."
  - "Trump's stated decision to delay strikes reduces near-term escalation risk, but the Polymarket price at 18% shows the market is not pricing a quick resolution to Hormuz disruption."
  - "Oil prices dropped on Trump's no-strike announcement per the news, yet the Polymarket contract remains far below 50%, suggesting the market sees the Hormuz standoff as a persistent issue through year-end."
  - "The Kalshi contract on the US reopening its embassy in Iran sits at 3%, consistent with the market view that US-Iran normalization is distant even as talks continue."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump ruled out Iran strikes before the midterms while Tehran weighs a Hormuz proposal, leaving the straits' commercial traffic status unresolved."
    publisher: "Surabhi Vasundharadevi, Jay Hilotin, Nathaniel Lacsina, Huda Ata"
    published_at: "2026-10-09T00:00:00.000Z"
    source_url: "https://gulfnews.com/world/mena/us-iran-war-trump-rules-out-strikes-before-midterms-as-tehran-weighs-hormuz-plan-iranian-spies-eye-us-bases-in-germany-1.500704037"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Surabhi Vasundharadevi, Jay Hilotin, Nathaniel Lacsina, Huda Ata"
        source_url: "https://gulfnews.com/world/mena/us-iran-war-trump-rules-out-strikes-before-midterms-as-tehran-weighs-hormuz-plan-iranian-spies-eye-us-bases-in-germany-1.500704037"
        retrieved_at: "2026-10-09T14:55:32+00:00"
  - type: "pm_response"
    notes: "Polymarket prices Hormuz normalization by year-end at 18%, with the US embassy in Iran contract at 3% on Kalshi, signaling the market treats US-Iran tension as structurally unresolved."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Surabhi Vasundharadevi, Jay Hilotin, Nathaniel Lacsina, Huda Ata: Trump Delays Strikes on Iran Before Midterms as Tehran Reviews Hormuz"
    url: "https://gulfnews.com/world/mena/us-iran-war-trump-rules-out-strikes-before-midterms-as-tehran-weighs-hormuz-plan-iranian-spies-eye-us-bases-in-germany-1.500704037"
    published_at: "2026-10-09T00:00:00.000Z"
    retrieved_at: "2026-10-09T14:55:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
