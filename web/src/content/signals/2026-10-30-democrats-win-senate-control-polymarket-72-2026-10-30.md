---
signal_id: "CMSIG2026103004"
signal_slug: "democrats-win-senate-control-polymarket-72-2026-10-30"
headline: "Democrats win Senate control: Polymarket 72%"
semantic_title: "Democrats favored to take Senate control in 2026 midterms"
telemetry: "Polymarket 72%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-30T00:00:00.000Z"
event_id: "CM-EVT-M9WJY06T90"
event_slug: "which-party-will-win-the-senate-in-2026"
event_question: "Which party will win control of the U.S. Senate in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x307a1ed89d60b61002dd5bbf00e1408c5ed2ab3fcdb056191ca7ef9bc34d38f3"
  question_raw: "Will the Democratic Party control the Senate after the 2026 Midterm elections?"
  current_price: 0.72
  volume_24h_usd: 376714.84805100004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "The Polymarket contract on Democrats winning Senate control in 2026 sits at 72%, via UMA oracle."
  - "Politico's framing of a possible GOP wipeout is directionally consistent with the market's clear Democratic lean."
  - "A companion Kalshi contract (CM-EVT-T5VXKJT451) puts Republicans holding at least one chamber at 70%, the two are compatible if Democrats take the Senate but Republicans retain the House."
  - "Resolution via UMA oracle, settled by official congressional composition after all 2026 races are called."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Politico reports a potential GOP midterm wipeout could loosen Trump's grip, with Democrats targeting Senate control."
    publisher: "Calen Razor"
    published_at: "2026-10-30T00:00:00.000Z"
    source_url: "https://www.politico.com/newsletters/inside-congress"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Calen Razor"
        source_url: "https://www.politico.com/newsletters/inside-congress"
        retrieved_at: "2026-10-31T07:48:23+00:00"
  - type: "pm_response"
    notes: "Polymarket at 72% for Democratic Senate control aligns with the Kalshi Republican chamber-hold contract at 70%, implying the market's base case is a split Congress."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Calen Razor: Inside Congress Newsletter - POLITICO"
    url: "https://www.politico.com/newsletters/inside-congress"
    published_at: "2026-10-30T00:00:00.000Z"
    retrieved_at: "2026-10-31T07:48:23+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
