---
signal_id: "CMSIG2026091206"
signal_slug: "us-invades-iran-before-2027-polymarket-15-2026-09-12"
headline: "US invades Iran before 2027: Polymarket 15%"
semantic_title: "US invasion of Iran before 2027 stays a long shot"
telemetry: "Polymarket 15%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-12T10:28:12.000Z"
event_id: "CM-EVT-WD982793G1"
event_slug: "will-the-us-invade-iran-before-2027"
event_question: "Will the U.S. invade Iran before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5db999fad322cea2914535aae5517060c3f80ad6d8c0231cde2124a434d16846"
  question_raw: "Will the U.S. invade Iran before 2027?"
  current_price: 0.15
  volume_24h_usd: 337252.67978999997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices the US invading Iran before 2027 at 15%, a clear long-shot read despite escalating proxy conflict."
  - "Iraqi militia drone attacks on Saudi infrastructure, traced to Iran-backed groups, represent direct conflict escalation, yet the market prices direct US military action as unlikely."
  - "The 15% Polymarket price alongside the 21% Strait of Hormuz normalization read (CM-EVT-LCPV825X09) paints a consistent picture: markets expect prolonged disruption but not full US-Iran war."
  - "Polymarket resolves via UMA oracle; resolution would require a confirmed US ground, air, or naval invasion of Iranian territory, not proxy conflict or airstrikes on third-party proxies."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran-backed Iraqi militias attacked the Saudi East-West pipeline, prompting Iraq to dismiss a military commander and scramble to contain regional fallout."
    publisher: "ABC News"
    published_at: "2026-09-12T10:28:12.000Z"
    source_url: "https://abcnews.com/International/wireStory/iraq-races-fallout-after-local-iran-backed-militias-136385727"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/International/wireStory/iraq-races-fallout-after-local-iran-backed-militias-136385727"
        retrieved_at: "2026-09-12T11:56:19+00:00"
  - type: "pm_response"
    notes: "Polymarket at 15% treats direct US-Iran military conflict as a tail risk even as proxy escalation intensifies across the region."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: Iraq races to contain fallout after local Iran-backed militias accused"
    url: "https://abcnews.com/International/wireStory/iraq-races-fallout-after-local-iran-backed-militias-136385727"
    published_at: "2026-09-12T10:28:12.000Z"
    retrieved_at: "2026-09-12T11:56:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
