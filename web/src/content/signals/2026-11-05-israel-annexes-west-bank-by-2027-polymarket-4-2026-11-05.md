---
signal_id: "CMSIG2026110506"
signal_slug: "israel-annexes-west-bank-by-2027-polymarket-4-2026-11-05"
headline: "Israel annexes West Bank by 2027: Polymarket 4%"
semantic_title: "Israeli West Bank annexation before 2027 stays a long shot"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-05T00:00:00.000Z"
event_id: "CM-EVT-FZLNPNYSY4"
event_slug: "will-israel-annex-west-bank-territory-before-2027"
event_question: "Will Israel annex West Bank territory before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x794fbb668b14dacd636ff47a39e2294148420577e38278e11adf14655ad6cfe0"
  question_raw: "Will Israel annex West Bank territory before 2027?"
  current_price: 0.04
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract puts only 4% odds on Israel annexing West Bank territory before 2027."
  - "Smotrich's annexation call drew immediate pushback from the UAE, a normalization partner, consistent with the market's heavy discount on near-term action."
  - "The Polymarket contract on Israel-Saudi normalization before 2027 sits at 6%, suggesting the market sees any major annexation move as even more likely to torpedo regional diplomacy."
  - "Resolves via Polymarket's UMA oracle; partial administrative steps versus formal annexation would be the key settlement distinction."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Israeli Finance Minister Bezalel Smotrich called to annex most of the West Bank, drawing a public rebuke from the UAE."
    publisher: "link.cfr.org"
    published_at: "2026-11-05T00:00:00.000Z"
    source_url: "https://link.cfr.org/public/41421755"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "link.cfr.org"
        source_url: "https://link.cfr.org/public/41421755"
        retrieved_at: "2026-11-05T07:48:08+00:00"
  - type: "pm_response"
    notes: "Polymarket prices West Bank annexation before 2027 at just 4%, fading the minister's public statement as rhetorical rather than actionable policy."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "link.cfr.org: Across the Globe"
    url: "https://link.cfr.org/public/41421755"
    published_at: "2026-11-05T00:00:00.000Z"
    retrieved_at: "2026-11-05T07:48:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
