---
signal_id: "CMSIG2026070102"
signal_slug: "iranian-regime-fall-before-2027-polymarket-10-2026-07-01"
headline: "Iranian regime fall before 2027: Polymarket 10%"
semantic_title: "Iranian regime survival pricing fractures toward resilience"
telemetry: "Polymarket 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-01T00:00:00.000Z"
event_id: "CM-EVT-QNQ4VPVP80"
event_slug: "will-the-iranian-regime-fall-by-the-end-of-2026"
event_question: "Will the Iranian regime fall before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbb4d51e6364066d92eb6f9b8413dd7193de70966736044463b205834805a1f3b"
  question_raw: "Will the Iranian regime fall before 2027?"
  current_price: 0.1
  volume_24h_usd: 58148.263679
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 10% on the Iranian regime falling before 2027, despite ongoing and intensifying US military strikes."
  - "Markets are not pricing regime change even as strikes expand geographically, suggesting capital-weighted consensus sees the conflict as degrading but not toppling the government."
  - "Kalshi at 7% on the US recognizing Reza Pahlavi as Iranian leader reinforces that prediction markets see regime transition as a tail scenario."
  - "Resolves via UMA oracle; the fall of the regime would require broadly recognized loss of governmental control, a high bar given current intelligence assessments."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US and Iran exchanged escalating attacks including expanded US strikes and Iranian missile and drone fire against regional US allies."
    publisher: "al-monitor.com"
    published_at: "2026-07-01T00:00:00.000Z"
    source_url: "https://www.al-monitor.com/originals/2026/07/iran-us-escalate-gulf-release-american-signals-path-climb-down"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "al-monitor.com"
        source_url: "https://www.al-monitor.com/originals/2026/07/iran-us-escalate-gulf-release-american-signals-path-climb-down"
        retrieved_at: "2026-07-17T09:53:11+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; low probability persists even as military exchanges broaden in scope and geography."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "al-monitor.com: Iran and US step up attacks, release of American in dispute - AL-MONIT"
    url: "https://www.al-monitor.com/originals/2026/07/iran-us-escalate-gulf-release-american-signals-path-climb-down"
    published_at: "2026-07-01T00:00:00.000Z"
    retrieved_at: "2026-07-17T09:53:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
