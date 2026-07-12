---
signal_id: "CMSIG2026071207"
signal_slug: "iranian-regime-falls-before-2027-polymarket-8-2026-07-12"
headline: "Iranian regime falls before 2027: Polymarket 8%"
semantic_title: "Iranian regime survival pricing holds despite US strike escalation"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-12T05:10:11.000Z"
event_id: "CM-EVT-QNQ4VPVP80"
event_slug: "will-the-iranian-regime-fall-by-the-end-of-2026"
event_question: "Will the Iranian regime fall before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbb4d51e6364066d92eb6f9b8413dd7193de70966736044463b205834805a1f3b"
  question_raw: "Will the Iranian regime fall before 2027?"
  current_price: 0.08
  volume_24h_usd: 33517.742997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 8% on the Iranian regime falling before 2027, via uma_oracle resolution, despite active US military strikes."
  - "Escalating US-Iran exchanges including strikes on Bushehr and Iranian missiles hitting Gulf states have not shifted the market to majority odds of regime collapse."
  - "A companion Polymarket contract (CM-EVT-BR5SMCCW00) prices 12% on Iran withdrawing from the NPT, consistent with a market that sees escalation but not existential regime threat."
  - "Resolves via uma_oracle; the definition of 'regime fall' is the key settlement edge case given Iran's current governmental continuity."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US strikes on Iranian military sites in Bushehr triggered Iranian ballistic missile strikes on Gulf states including Jordan, with Bitcoin falling sharply below $73K on geopolitical risk."
    publisher: "Editorial Team"
    published_at: "2026-07-12T05:10:11.000Z"
    source_url: "https://cryptobriefing.com/iran-bushehr-strikes-bitcoin-crypto-crash/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Editorial Team"
        source_url: "https://cryptobriefing.com/iran-bushehr-strikes-bitcoin-crypto-crash/"
        retrieved_at: "2026-07-12T09:47:51+00:00"
  - type: "pm_response"
    notes: "Polymarket contract; cross-checking CM-EVT-YQ6BFV3GX1 at 5% for Iranian nuclear test and CM-EVT-RV9Z73GLB0 at 5% for nuclear weapon development shows the market treats regime survival as the baseline even under active conflict."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Editorial Team: Iranian state TV reports projectile strikes on military sites in Bushe"
    url: "https://cryptobriefing.com/iran-bushehr-strikes-bitcoin-crypto-crash/"
    published_at: "2026-07-12T05:10:11.000Z"
    retrieved_at: "2026-07-12T09:47:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
