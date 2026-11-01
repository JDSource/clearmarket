---
signal_id: "CMSIG2026103005"
signal_slug: "democrats-win-senate-2026-polymarket-73-2026-10-30"
headline: "Democrats win Senate 2026: Polymarket 73%"
semantic_title: "Democrats favored to win Senate control after midterms"
telemetry: "Polymarket 73%"
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
  current_price: 0.73
  volume_24h_usd: 246061.71147699998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket puts Democratic control of the Senate at 73%, a strong but not overwhelming lean heading into election week."
  - "Politico's GOP wipeout framing is broadly consistent with prediction market pricing, the Senate is the closer of the two chambers in the market's view."
  - "Republicans controlling at least one chamber sits at 70% on a separate Kalshi contract, implying the House may be the more contested battleground."
  - "Resolution follows the Library of Congress certification of official congressional composition after the November election count is complete."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Politico's Inside Congress newsletter reports a potential GOP wipeout in the midterms could loosen President Donald Trump's grip on Congress."
    publisher: "Calen Razor"
    published_at: "2026-10-30T00:00:00.000Z"
    source_url: "https://www.politico.com/newsletters/inside-congress"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Calen Razor"
        source_url: "https://www.politico.com/newsletters/inside-congress"
        retrieved_at: "2026-11-01T07:48:20+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; cross-referencing with Kalshi's Republican chamber control contract at 70% reveals Senate and House are priced differently."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Calen Razor: Inside Congress Newsletter - POLITICO"
    url: "https://www.politico.com/newsletters/inside-congress"
    published_at: "2026-10-30T00:00:00.000Z"
    retrieved_at: "2026-11-01T07:48:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
