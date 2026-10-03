---
signal_id: "CMSIG2026100308"
signal_slug: "north-korea-invades-south-korea-before-2027-polymarket-1-2026-10-03"
headline: "North Korea invades South Korea before 2027: Polymarket 1%"
semantic_title: "North Korea invading South Korea before 2027 stays near zero"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-03T00:00:00.000Z"
event_id: "CM-EVT-GGMF8V7JH2"
event_slug: "will-north-korea-invade-south-korea-before-2027"
event_question: "Will North Korea invade South Korea before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84dc47b1dd9cd99a9217b92a95690729334b647650bb6bf676bb31c3db0d7f79"
  question_raw: "Will North Korea invade South Korea before 2027?"
  current_price: 0.014
  volume_24h_usd: 5.045872
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 1% on North Korea invading South Korea before 2027, resolving via UMA oracle."
  - "The missile launch and rising border tensions are consistent with provocation but the market does not treat them as a prelude to full invasion."
  - "Companion contract on Kim Jong Un losing power by December 31, 2026 sits at 4%, also on Polymarket via UMA oracle, suggesting regime continuity is the base case."
  - "Resolution via UMA oracle requires confirmed military invasion; missile tests and border incidents fall well short of the resolution threshold."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "North Korea launched a ballistic missile from the Wonsan area into the Sea of Japan amid rising tensions with Seoul over border mine blasts that wounded South Korean soldiers."
    publisher: "Reuters"
    published_at: "2026-10-03T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/oct/03/north-korea-launches-ballistic-missile-after-seoul-demands-apology-over-wounded-soldiers"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters"
        source_url: "https://www.theguardian.com/world/2026/oct/03/north-korea-launches-ballistic-missile-after-seoul-demands-apology-over-wounded-soldiers"
        retrieved_at: "2026-10-03T07:47:35+00:00"
  - type: "pm_response"
    notes: "Polymarket at 1% is unchanged in signal despite the live missile test, indicating the market draws a sharp distinction between provocation and invasion risk."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters: North Korea launches ballistic missile after Seoul demands apology ove"
    url: "https://www.theguardian.com/world/2026/oct/03/north-korea-launches-ballistic-missile-after-seoul-demands-apology-over-wounded-soldiers"
    published_at: "2026-10-03T00:00:00.000Z"
    retrieved_at: "2026-10-03T07:47:35+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
