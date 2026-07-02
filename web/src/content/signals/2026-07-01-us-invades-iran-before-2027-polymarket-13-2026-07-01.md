---
signal_id: "CMSIG2026070106"
signal_slug: "us-invades-iran-before-2027-polymarket-13-2026-07-01"
headline: "US invades Iran before 2027: Polymarket 13%"
semantic_title: "US Iran invasion pricing holds low as diplomacy advances"
telemetry: "Polymarket 13%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-01T08:38:25.000Z"
event_id: "CM-EVT-WD982793G1"
event_slug: "will-the-us-invade-iran-before-2027"
event_question: "Will the United States invade Iran before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5db999fad322cea2914535aae5517060c3f80ad6d8c0231cde2124a434d16846"
  question_raw: "Will the U.S. invade Iran before 2027?"
  current_price: 0.13
  volume_24h_usd: 49721.330948000024
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prediction market prices 13% on a US invasion of Iran before 2027."
  - "Qatar's 'positive progress' report and the Vance 'no return to war' statement are consistent with the low invasion probability, markets are not pricing imminent escalation."
  - "A companion Kalshi contract at 6% on the US recognizing Reza Pahlavi as Iran's leader signals markets see regime-change outcomes as even less likely than military action."
  - "Resolves via Polymarket's uma_oracle resolution process; the trigger requires a formal US military invasion, not airstrikes or proxy action."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US-Iran indirect talks in Doha concluded with Qatar reporting positive progress, with Vice President JD Vance signaling no return to war unless necessary and a communication channel established."
    publisher: "Al Jazeera Staff"
    published_at: "2026-07-01T08:38:25.000Z"
    source_url: "https://www.aljazeera.com/news/2026/7/1/us-iran-negotiations-whats-the-latest"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/7/1/us-iran-negotiations-whats-the-latest"
        retrieved_at: "2026-07-02T10:34:14+00:00"
  - type: "pm_response"
    notes: "Polymarket's 13% on US invasion of Iran reflects markets treating Doha diplomacy as a de-escalation signal, though the tail risk is non-trivial."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: US-Iran negotiations: What’s the latest? | US-Israel war on Iran News"
    url: "https://www.aljazeera.com/news/2026/7/1/us-iran-negotiations-whats-the-latest"
    published_at: "2026-07-01T08:38:25.000Z"
    retrieved_at: "2026-07-02T10:34:14+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
