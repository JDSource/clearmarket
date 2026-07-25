---
signal_id: "CMSIG2026072508"
signal_slug: "us-national-bitcoin-reserve-before-2027-polymarket-17-2026-07-25"
headline: "US national Bitcoin reserve before 2027: Polymarket 17%"
semantic_title: "National Bitcoin reserve by 2027 holds below 25 percent on Polymarket"
telemetry: "Polymarket 17%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-25T00:00:00.000Z"
event_id: "CM-EVT-0F2G0B8X49"
event_slug: "us-national-bitcoin-reserve-before-2027"
event_question: "Will the United States establish a national Bitcoin reserve before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x953b1439569eef0a0e639566acd35d32ebadee8ab70dbb2f8e00bb936a277aa2"
  question_raw: "US national Bitcoin reserve before 2027?"
  current_price: 0.17
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 17% chance the United States establishes a national Bitcoin reserve before 2027."
  - "A $288 million government Bitcoin transfer to Coinbase spotlights uncertainty around reserve rules, but Polymarket at 17% shows the market still treats formal reserve establishment as unlikely before 2027."
  - "A companion Kalshi contract (CM-EVT-JQRXSG4ZX9) prices a Trump-created National Bitcoin Reserve in 2026 at 19%, consistent with the Polymarket read across venues."
  - "Resolution via Polymarket UMA oracle based on an official U.S. government announcement of a formal national Bitcoin reserve structure."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The U.S. government transferred $288 million to Coinbase, raising questions about compliance with Bitcoin strategic reserve executive order rules."
    publisher: "bitrss.com"
    published_at: "2026-07-25T00:00:00.000Z"
    source_url: "https://bitrss.com/us-government-sends-288m-to-coinbase-putting-bitcoin-reserve-rules-into-question-232030"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bitrss.com"
        source_url: "https://bitrss.com/us-government-sends-288m-to-coinbase-putting-bitcoin-reserve-rules-into-question-232030"
        retrieved_at: "2026-07-25T09:42:27+00:00"
  - type: "pm_response"
    notes: "Polymarket at 17% and Kalshi at 19% show cross-venue agreement that a formal U.S. Bitcoin reserve remains a minority-probability outcome before 2027."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bitrss.com: US government sends $288M to Coinbase putting Bitcoin reserve rules in"
    url: "https://bitrss.com/us-government-sends-288m-to-coinbase-putting-bitcoin-reserve-rules-into-question-232030"
    published_at: "2026-07-25T00:00:00.000Z"
    retrieved_at: "2026-07-25T09:42:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
