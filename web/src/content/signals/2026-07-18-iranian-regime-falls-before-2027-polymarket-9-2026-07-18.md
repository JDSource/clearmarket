---
signal_id: "CMSIG2026071806"
signal_slug: "iranian-regime-falls-before-2027-polymarket-9-2026-07-18"
headline: "Iranian regime falls before 2027: Polymarket 9%"
semantic_title: "Iranian regime survival anchors against fall-before-2027 at 9 percent"
telemetry: "Polymarket 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-18T01:01:30.000Z"
event_id: "CM-EVT-QNQ4VPVP80"
event_slug: "will-the-iranian-regime-fall-by-the-end-of-2026"
event_question: "Will the Iranian regime fall before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbb4d51e6364066d92eb6f9b8413dd7193de70966736044463b205834805a1f3b"
  question_raw: "Will the Iranian regime fall before 2027?"
  current_price: 0.09
  volume_24h_usd: 245082.367227
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices the Iranian regime falling before 2027 at 9%, a low-probability tail despite ongoing nightly US strikes."
  - "Seven nights of US airstrikes on infrastructure plus Iran's continued retaliation and escalatory warnings are consistent with a stressed but surviving regime scenario."
  - "The Kalshi contract on the US recognizing Reza Pahlavi as Iranian leader by 2026 sits at just 7%, corroborating the market's view that regime change is a remote outcome."
  - "Resolves via Polymarket's UMA oracle based on whether the current Iranian government ceases to hold power before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US struck Iran for a seventh consecutive night while Iranian forces launched retaliatory attacks and an adviser to the supreme leader warned of an offensive and destructive new phase."
    publisher: "ToI Staff"
    published_at: "2026-07-18T01:01:30.000Z"
    source_url: "https://www.timesofisrael.com/liveblog-july-18-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ToI Staff"
        source_url: "https://www.timesofisrael.com/liveblog-july-18-2026/"
        retrieved_at: "2026-07-18T09:20:01+00:00"
  - type: "pm_response"
    notes: "Polymarket at 9% and the parallel Kalshi Pahlavi contract at 7% jointly signal the market sees escalation as containable, not regime-ending, at current probability levels."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ToI Staff: US strikes Iran for seventh night in a row; Iranian forces launch reta"
    url: "https://www.timesofisrael.com/liveblog-july-18-2026/"
    published_at: "2026-07-18T01:01:30.000Z"
    retrieved_at: "2026-07-18T09:20:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
