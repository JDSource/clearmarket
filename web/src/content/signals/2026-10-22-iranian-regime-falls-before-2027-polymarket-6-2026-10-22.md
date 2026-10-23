---
signal_id: "CMSIG2026102208"
signal_slug: "iranian-regime-falls-before-2027-polymarket-6-2026-10-22"
headline: "Iranian regime falls before 2027: Polymarket 6%"
semantic_title: "Iranian regime falling before 2027 remains priced as a long shot"
telemetry: "Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-22T23:00:00.000Z"
event_id: "CM-EVT-QNQ4VPVP80"
event_slug: "will-the-iranian-regime-fall-by-the-end-of-2026"
event_question: "Will the Iranian regime fall before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbb4d51e6364066d92eb6f9b8413dd7193de70966736044463b205834805a1f3b"
  question_raw: "Will the Iranian regime fall before 2027?"
  current_price: 0.06
  volume_24h_usd: 89870.75334
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market puts just 6% odds on the Iranian regime falling before 2027, pricing survival as the overwhelming base case."
  - "Despite US military strikes already having occurred and Trump threatening escalation, the market prices regime collapse as a remote outcome, consistent with Iran's stated deterrence strategy."
  - "Iran's retention of missile and drone stockpiles, noted in WSJ reporting, supports the market's view that the regime retains enough capacity to survive a limited US campaign."
  - "Resolves via Polymarket's UMA oracle; the definition of regime 'falling', leadership change, collapse of state institutions, or loss of territorial control, is a material resolution risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Reports indicate Trump is considering new strikes on Iran after the midterm elections, while Iranian officials say their goal is regime preservation and imposing enough regional cost to deter prolonged US operations."
    publisher: "Amir Soltanzadeh, Wesley Rahn"
    published_at: "2026-10-22T23:00:00.000Z"
    source_url: "https://www.dw.com/en/is-iran-ready-for-another-major-us-attack-after-midterm-elections/a-79734082"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Amir Soltanzadeh, Wesley Rahn"
        source_url: "https://www.dw.com/en/is-iran-ready-for-another-major-us-attack-after-midterm-elections/a-79734082"
        retrieved_at: "2026-10-23T13:03:13+00:00"
  - type: "pm_response"
    notes: "Polymarket at 6% prices Iranian regime survival as the near-certain base case even as US escalation threats intensify post-midterms."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Amir Soltanzadeh, Wesley Rahn: Trump has threatened to escalate his Iran war after the US midterm ele"
    url: "https://www.dw.com/en/is-iran-ready-for-another-major-us-attack-after-midterm-elections/a-79734082"
    published_at: "2026-10-22T23:00:00.000Z"
    retrieved_at: "2026-10-23T13:03:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
