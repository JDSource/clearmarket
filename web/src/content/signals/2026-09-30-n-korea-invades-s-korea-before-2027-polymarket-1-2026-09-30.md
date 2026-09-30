---
signal_id: "CMSIG2026093008"
signal_slug: "n-korea-invades-s-korea-before-2027-polymarket-1-2026-09-30"
headline: "N. Korea invades S. Korea before 2027: Polymarket 1%"
semantic_title: "North Korea invading South Korea stays near zero odds"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-30T00:00:00.000Z"
event_id: "CM-EVT-GGMF8V7JH2"
event_slug: "will-north-korea-invade-south-korea-before-2027"
event_question: "Will North Korea invade South Korea before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84dc47b1dd9cd99a9217b92a95690729334b647650bb6bf676bb31c3db0d7f79"
  question_raw: "Will North Korea invade South Korea before 2027?"
  current_price: 0.014
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market puts only 1% on North Korea invading South Korea before 2027, despite the DMZ mine incident and Pyongyang's retaliation warning."
  - "The denial-plus-warning posture from Pyongyang is a familiar escalation pattern; the market is treating it as signaling behavior rather than a genuine invasion precursor."
  - "The companion Polymarket contract on Kim Jong Un no longer being Supreme Leader by December 31, 2026 sits at 4%, also a long shot, suggesting no regime instability is priced."
  - "Resolves via Polymarket's uma_oracle; an actual cross-border military incursion would be required for resolution, not a skirmish or mine incident alone."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "North Korea denied responsibility for a DMZ mine explosion and warned South Korea of retaliation, raising cross-border tensions on the peninsula."
    publisher: "Oh Seok-min"
    published_at: "2026-09-30T00:00:00.000Z"
    source_url: "https://en.yna.co.kr/view/AEN20260930000453315"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Oh Seok-min"
        source_url: "https://en.yna.co.kr/view/AEN20260930000453315"
        retrieved_at: "2026-09-30T07:47:19+00:00"
  - type: "pm_response"
    notes: "Polymarket at 1% puts near-zero odds on a North Korean invasion despite fresh DMZ tensions, treating the incident as below the threshold of genuine conflict risk."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Oh Seok-min: (2nd LD) N. Korea denies responsibility for DMZ mine blast, warns S. K"
    url: "https://en.yna.co.kr/view/AEN20260930000453315"
    published_at: "2026-09-30T00:00:00.000Z"
    retrieved_at: "2026-09-30T07:47:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
