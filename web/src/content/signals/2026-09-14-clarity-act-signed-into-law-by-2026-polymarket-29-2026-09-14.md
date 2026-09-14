---
signal_id: "CMSIG2026091405"
signal_slug: "clarity-act-signed-into-law-by-2026-polymarket-29-2026-09-14"
headline: "Clarity Act signed into law by 2026: Polymarket 29%"
semantic_title: "Clarity Act signed into law by 2026 stays a long shot at 29 percent"
telemetry: "Polymarket 29%"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-09-14T00:00:00.000Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act (H.R. 3633) be signed into law by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act (H.R.3633) signed into law in 2026?"
  current_price: 0.29
  volume_24h_usd: 678875.732376
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket puts 29% on the Clarity Act being signed into law by end of 2026, resolving via UMA oracle."
  - "Tuesday's cloture vote is a necessary but not sufficient step; the market reflects significant doubt the bill clears both chambers and gains presidential signature this year."
  - "Companion ladder (CM-EVT-CSYS5KPXK6) implies roughly 60 Senate yea votes, sitting right at the 60-vote cloture threshold and flagging procedural risk."
  - "At 29%, the law-by-2026 contract prices in passage failure risk even if cloture succeeds, given House and presidential signature steps remaining."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Senate is set to hold a make-or-break cloture vote Tuesday on the Digital Asset Market Clarity Act, a major crypto regulatory framework bill."
    publisher: "Garrett Downs"
    published_at: "2026-09-14T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/09/14/clarity-act-senate-vote-crypto-regulation.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Garrett Downs"
        source_url: "https://www.cnbc.com/2026/09/14/clarity-act-senate-vote-crypto-regulation.html"
        retrieved_at: "2026-09-14T14:41:02+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on whether H.R. 3633 is signed into law before January 1, 2027."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Garrett Downs: Clarity Act faces crucial Senate vote Tuesday in big moment for crypto"
    url: "https://www.cnbc.com/2026/09/14/clarity-act-senate-vote-crypto-regulation.html"
    published_at: "2026-09-14T00:00:00.000Z"
    retrieved_at: "2026-09-14T14:41:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
