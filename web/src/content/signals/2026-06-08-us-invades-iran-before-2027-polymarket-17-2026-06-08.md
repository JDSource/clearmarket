---
signal_id: "CMSIG2026060806"
signal_slug: "us-invades-iran-before-2027-polymarket-17-2026-06-08"
headline: "US invades Iran before 2027: Polymarket 17%"
semantic_title: "US invasion of Iran before 2027 holds at 17 percent"
telemetry: "Polymarket 17%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-08T07:16:28.000Z"
event_id: "CM-EVT-WD982793G1"
event_slug: "will-the-us-invade-iran-before-2027"
event_question: "Will the United States invade Iran before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5db999fad322cea2914535aae5517060c3f80ad6d8c0231cde2124a434d16846"
  question_raw: "Will the U.S. invade Iran before 2027?"
  current_price: 0.17
  volume_24h_usd: 123882.79982599999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 17% chance the United States directly invades Iran before 2027."
  - "Active Iran-Israel exchanges and IRGC energy asset threats are hawkish inputs, yet the market keeps direct US invasion well below one-in-five."
  - "The Iranian regime survival contract at 97% (Story 24 candidate) implies the market sees regime continuity as far more likely than US ground action."
  - "Resolves via Polymarket's uma_oracle based on credible reporting of a US ground or large-scale air invasion of Iranian territory."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran and Israel engaged in tit-for-tat missile and drone strikes on day 101 of the Iran war, with the IRGC threatening regional energy assets."
    publisher: "Sarah Shamim"
    published_at: "2026-06-08T07:16:28.000Z"
    source_url: "https://www.aljazeera.com/news/2026/6/8/iran-war-day-101-tensions-escalate-as-iran-and-israel-trade-air-attacks"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Sarah Shamim"
        source_url: "https://www.aljazeera.com/news/2026/6/8/iran-war-day-101-tensions-escalate-as-iran-and-israel-trade-air-attacks"
        retrieved_at: "2026-06-09T10:57:53+00:00"
  - type: "pm_response"
    notes: "Polymarket's 17% on US invasion sits alongside a 28% nuclear deal probability, bracketing a wide middle scenario of ongoing proxy conflict."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Sarah Shamim: Iran war day 101: Tensions escalate as Iran and Israel trade air attac"
    url: "https://www.aljazeera.com/news/2026/6/8/iran-war-day-101-tensions-escalate-as-iran-and-israel-trade-air-attacks"
    published_at: "2026-06-08T07:16:28.000Z"
    retrieved_at: "2026-06-09T10:57:53+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
