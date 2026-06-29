---
signal_id: "CMSIG2026062802"
signal_slug: "us-invasion-of-iran-before-2027-polymarket-14-2026-06-28"
headline: "US invasion of Iran before 2027: Polymarket 14%"
semantic_title: "US Iran invasion by 2027 consensus wavers at low probability"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-28T02:00:00.000Z"
event_id: "CM-EVT-WD982793G1"
event_slug: "will-the-us-invade-iran-before-2027"
event_question: "Will the United States invade Iran before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5db999fad322cea2914535aae5517060c3f80ad6d8c0231cde2124a434d16846"
  question_raw: "Will the U.S. invade Iran before 2027?"
  current_price: 0.14
  volume_24h_usd: 47862.38134400001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 14% on the US invading Iran before 2027, despite active bilateral strikes and ceasefire breakdown."
  - "Market is at odds with the escalatory tone of the news; pricing implies markets treat ongoing strikes as contained, not an invasion precursor."
  - "Companion Polymarket contract on European allies (France, UK, Germany) striking Iran by June 30 is at 0%, suggesting no coalition broadening priced in."
  - "Resolves via UMA oracle; 'invasion' likely requires ground forces or a formal declaration, not air strikes alone."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran launched a crushing retaliatory response after fresh US strikes, with both sides accusing each other of ceasefire violations."
    publisher: "TOI World Desk  / TIMESOFINDIA.COM /  Updated: Jun 28, 2026, 12:07 IST"
    published_at: "2026-06-28T02:00:00.000Z"
    source_url: "https://timesofindia.indiatimes.com/world/middle-east/us-iran-conflict-escalates-tehran-hits-back-with-crushing-response-after-trumps-fresh-strikes-key-developments/articleshow/132044398.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "TOI World Desk  / TIMESOFINDIA.COM /  Updated: Jun 28, 2026, 12:07 IST"
        source_url: "https://timesofindia.indiatimes.com/world/middle-east/us-iran-conflict-escalates-tehran-hits-back-with-crushing-response-after-trumps-fresh-strikes-key-developments/articleshow/132044398.cms"
        retrieved_at: "2026-06-29T12:28:56+00:00"
  - type: "pm_response"
    notes: "Polymarket's 14% on invasion reflects a consensus that current exchanges remain below the threshold of full military escalation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "TOI World Desk  / TIMESOFINDIA.COM /  Updated: Jun 28, 2026, 12:07 IST: US-Iran conflict escalates: Tehran hits back with 'crushing response'"
    url: "https://timesofindia.indiatimes.com/world/middle-east/us-iran-conflict-escalates-tehran-hits-back-with-crushing-response-after-trumps-fresh-strikes-key-developments/articleshow/132044398.cms"
    published_at: "2026-06-28T02:00:00.000Z"
    retrieved_at: "2026-06-29T12:28:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
