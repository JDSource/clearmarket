---
signal_id: "CMSIG2026072806"
signal_slug: "us-invades-iran-before-2027-polymarket-21-2026-07-28"
headline: "US invades Iran before 2027: Polymarket 21%"
semantic_title: "US invasion of Iran before 2027 stays a long shot at 21%"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-28T00:00:00.000Z"
event_id: "CM-EVT-WD982793G1"
event_slug: "will-the-us-invade-iran-before-2027"
event_question: "Will the U.S. invade Iran before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5db999fad322cea2914535aae5517060c3f80ad6d8c0231cde2124a434d16846"
  question_raw: "Will the U.S. invade Iran before 2027?"
  current_price: 0.21
  volume_24h_usd: 221526.91338299992
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 21% chance the United States invades Iran before 2027, a substantial but minority probability."
  - "High-level White House diplomacy with Zelenskyy and Netanyahu, alongside the three-day ceasefire, is consistent with the market staying well below 50%."
  - "The 21% figure reflects a meaningful tail risk rather than a base case, given Trump's simultaneous diplomatic outreach and military warnings."
  - "Companion Kalshi contract CM-EVT-34SYT4T2T1 prices only 3% on the US reopening its embassy in Iran, suggesting full normalization is seen as near-impossible."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The White House prepared for high-stakes talks with Ukrainian President Volodymyr Zelenskyy and Israeli Prime Minister Benjamin Netanyahu as the Iran and Ukraine conflicts converged."
    publisher: "euronews.com"
    published_at: "2026-07-28T00:00:00.000Z"
    source_url: "https://www.euronews.com/2026/07/28/white-house-prepares-for-high-stakes-talks-with-zelenskyy-and-netanyahu"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "euronews.com"
        source_url: "https://www.euronews.com/2026/07/28/white-house-prepares-for-high-stakes-talks-with-zelenskyy-and-netanyahu"
        retrieved_at: "2026-07-28T10:30:26+00:00"
  - type: "pm_response"
    notes: "Polymarket binary resolving via UMA oracle; the 21% sits well below the diplomatic-failure threshold that would be needed to shift toward majority pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "euronews.com: White House prepares for high-stakes talks with Zelenskyy and Netanyah"
    url: "https://www.euronews.com/2026/07/28/white-house-prepares-for-high-stakes-talks-with-zelenskyy-and-netanyahu"
    published_at: "2026-07-28T00:00:00.000Z"
    retrieved_at: "2026-07-28T10:30:26+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
