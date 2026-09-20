---
signal_id: "CMSIG2026092007"
signal_slug: "putin-out-as-russia-president-by-2026-polymarket-4-2026-09-20"
headline: "Putin out as Russia president by 2026: Polymarket 4%"
semantic_title: "Putin leaving the Russian presidency by end of 2026 stays a long shot"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-20T00:00:00.000Z"
event_id: "CM-EVT-5WJSMVBVS7"
event_slug: "putin-out-before-2027"
event_question: "Will Vladimir Putin no longer be President of Russia by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6bd56627aa21311850825edb27e53434a0e17a4f782be0086bc07f71eee00d0d"
  question_raw: "Putin out as President of Russia by December 31, 2026?"
  current_price: 0.04
  volume_24h_usd: 14543.172501
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T18:30:00Z"
bullets:
  - "Polymarket prices only a 4% chance Vladimir Putin is no longer President of Russia by end of 2026."
  - "Ukraine's largest-ever drone attack on Moscow is a significant escalation, yet the Polymarket contract shows the market treating Putin's removal as a deep tail event."
  - "The 4% pricing implies the attack, while symbolically significant, is not being read as a near-term threat to Russian political stability."
  - "Resolves via Polymarket's UMA oracle; the contract would resolve YES on any scenario in which Putin ceases to hold the presidency, including death, resignation, or removal."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukraine launched over 1,000 drones at Russia in what Moscow's mayor described as the largest-ever attack, killing two people and striking a Moscow oil refinery."
    publisher: "Al Jazeera Staff"
    published_at: "2026-09-20T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/9/20/mass-ukrainian-drone-attack-on-moscow-kills-two-russia-says"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/9/20/mass-ukrainian-drone-attack-on-moscow-kills-two-russia-says"
        retrieved_at: "2026-09-20T12:50:04+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 4% remains unmoved in headline terms by the drone escalation; no intraday price history is available to assess any shift from this level."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Mass Ukrainian drone attack on Moscow kills two, Russia says | Drone S"
    url: "https://www.aljazeera.com/news/2026/9/20/mass-ukrainian-drone-attack-on-moscow-kills-two-russia-says"
    published_at: "2026-09-20T00:00:00.000Z"
    retrieved_at: "2026-09-20T12:50:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
