---
signal_id: "CMSIG2026102504"
signal_slug: "dems-win-2026-senate-control-polymarket-66-2026-10-25"
headline: "Dems win 2026 Senate control: Polymarket 66%"
semantic_title: "Democrats favored to win Senate control in 2026 race"
telemetry: "Polymarket 66%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-25T02:00:00.000Z"
event_id: "CM-EVT-M9WJY06T90"
event_slug: "which-party-will-win-the-senate-in-2026"
event_question: "Which party will win control of the U.S. Senate in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x307a1ed89d60b61002dd5bbf00e1408c5ed2ab3fcdb056191ca7ef9bc34d38f3"
  question_raw: "Will the Democratic Party control the Senate after the 2026 Midterm elections?"
  current_price: 0.66
  volume_24h_usd: 64680.928675
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a 66% probability that Democrats win control of the U.S. Senate in the 2026 election."
  - "Obama's active campaign trail presence is consistent with Democrats being modest favorites, though the Polymarket contract predates this specific appearance."
  - "The Kalshi contract simultaneously puts only 65% on Republicans controlling at least one chamber, making a split Congress outcome plausible under both markets."
  - "Polymarket resolves via UMA oracle based on certified Senate composition post-election; contested seats or recounts could delay resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Former President Barack Obama campaigned for Democrats ahead of the midterms, attacking the Trump administration on the Iran war and high consumer prices."
    publisher: "Max Matza"
    published_at: "2026-10-25T02:00:00.000Z"
    source_url: "https://www.bbc.com/news/articles/cmj6jwe1j1gjo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Max Matza"
        source_url: "https://www.bbc.com/news/articles/cmj6jwe1j1gjo"
        retrieved_at: "2026-10-25T12:56:07+00:00"
  - type: "pm_response"
    notes: "Polymarket at 66% for a Democratic Senate majority, running against the Kalshi 65% Republican chamber contract, implies the market sees a House-only GOP scenario as the likeliest Republican path."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Max Matza: Obama attacks Trump as he campaigns for Democrats ahead of midterm ele"
    url: "https://www.bbc.com/news/articles/cmj6jwe1j1gjo"
    published_at: "2026-10-25T02:00:00.000Z"
    retrieved_at: "2026-10-25T12:56:07+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
