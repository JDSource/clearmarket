---
signal_id: "CMSIG2026100608"
signal_slug: "hormuz-traffic-to-normal-by-dec-31-polymarket-19-2026-10-06"
headline: "Hormuz traffic to normal by Dec 31: Polymarket 19%"
semantic_title: "Hormuz normalization by year-end stays a long shot at 19%"
telemetry: "Polymarket 19%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-06T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.19
  volume_24h_usd: 45923.53801600001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 prices at 19%, well below an even-money read."
  - "The Saudi-led coalition's military escalation in Yemen and Houthi strikes on Riyadh's King Khalid International Airport and Aramco facilities signal the conflict is broadening, not resolving."
  - "Iran's rejection of US diplomatic talks (Story 26) reinforces the low probability of a near-term Hormuz normalization."
  - "Resolves via Polymarket's UMA oracle; the definition of 'normal' Hormuz traffic and the verification source are critical settlement considerations."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Yemen government forces recaptured the Red Sea port of Mokha from Houthis as Saudi Arabia, Turkey, and Pakistan agreed to deploy forces and activate deterrence measures, keeping oil markets on edge."
    publisher: "Sam Meredith"
    published_at: "2026-10-06T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/10/06/iran-war-yemen-saudi-arabia-mokha-oil.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Sam Meredith"
        source_url: "https://www.cnbc.com/2026/10/06/iran-war-yemen-saudi-arabia-mokha-oil.html"
        retrieved_at: "2026-10-06T14:42:27+00:00"
  - type: "pm_response"
    notes: "Polymarket's 19% reflects the market's consistent view that Hormuz normalization by year-end is unlikely amid active regional escalation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Sam Meredith: Iran war: Yemen forces reclaim Red Sea port city of Mokha from Houthis"
    url: "https://www.cnbc.com/2026/10/06/iran-war-yemen-saudi-arabia-mokha-oil.html"
    published_at: "2026-10-06T00:00:00.000Z"
    retrieved_at: "2026-10-06T14:42:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
