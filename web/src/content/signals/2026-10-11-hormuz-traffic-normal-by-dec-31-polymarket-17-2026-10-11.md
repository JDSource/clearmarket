---
signal_id: "CMSIG2026101107"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-17-2026-10-11"
headline: "Hormuz traffic normal by Dec 31: Polymarket 17%"
semantic_title: "Hormuz traffic back to normal by year-end stays near 17 percent"
telemetry: "Polymarket 17%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-11T14:04:32.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.17
  volume_24h_usd: 26101.151168
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts just 17% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Escalating IRGC attacks and stalled war-ending efforts are consistent with the market's bearish read on near-term normalization."
  - "A separate news report describes US forces disabling a ship attempting to breach Iran's Gulf of Oman blockade, adding operational evidence for continued disruption."
  - "Trump separately said he is considering joining Saudi Arabia in striking Houthi targets, an escalation path that would further reduce normalization odds."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "IRGC warnings intensified and Hormuz attack activity escalated as US-Israel-Iran war efforts showed no sign of resolution."
    publisher: "Maziar Motamedi"
    published_at: "2026-10-11T14:04:32.000Z"
    source_url: "https://www.aljazeera.com/news/2026/10/11/hormuz-attacks-intensify-as-efforts-to-end-war-on-iran-stall"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Maziar Motamedi"
        source_url: "https://www.aljazeera.com/news/2026/10/11/hormuz-attacks-intensify-as-efforts-to-end-war-on-iran-stall"
        retrieved_at: "2026-10-11T14:35:49+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; at 17%, the market is treating full Hormuz normalization by year-end as a tail outcome given current military posture."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Maziar Motamedi: Hormuz attacks intensify as efforts to end war on Iran stall | US-Isra"
    url: "https://www.aljazeera.com/news/2026/10/11/hormuz-attacks-intensify-as-efforts-to-end-war-on-iran-stall"
    published_at: "2026-10-11T14:04:32.000Z"
    retrieved_at: "2026-10-11T14:35:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
