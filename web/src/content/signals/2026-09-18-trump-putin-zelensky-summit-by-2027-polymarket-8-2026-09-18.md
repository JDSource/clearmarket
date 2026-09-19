---
signal_id: "CMSIG2026091805"
signal_slug: "trump-putin-zelensky-summit-by-2027-polymarket-8-2026-09-18"
headline: "Trump-Putin-Zelensky summit by 2027: Polymarket 8%"
semantic_title: "Trump-Putin-Zelensky summit before 2027 stays a long shot"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-18T00:00:00.000Z"
event_id: "CM-EVT-QP1YL1BSS0"
event_slug: "trump-putin-and-zelensky-seen-together-before-2027"
event_question: "Will Trump, Putin, and Zelensky be seen together before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa04dcb7b7f5a313d09e7728ca39835be4096da877ca5fbae5e3a36af239433c3"
  question_raw: "Trump, Putin, and Zelensky seen together before 2027?"
  current_price: 0.08
  volume_24h_usd: 43.555257
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract puts only an 8% chance that Trump, Putin, and Zelensky appear together before 2027."
  - "Trump signing Russia sanctions into law is a hawkish signal that makes a tripartite diplomatic summit more, not less, difficult near-term."
  - "The market is not treating the sanctions bill as a bridge to peace talks; the 8% probability is consistent with the hardened posture."
  - "Resolves via uma_oracle; the companion Polymarket contract on Putin remaining president sits at 95% probability, removing leadership-change tail risk from the equation."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "President Trump signed a Russia sanctions bill into law on September 18, 2026, granting himself sweeping new tariff powers while Russia-Ukraine fighting continued."
    publisher: "reuters.com"
    published_at: "2026-09-18T00:00:00.000Z"
    source_url: "https://www.reuters.com/world/us/trump-signs-russia-sanctions-bill-into-law-2026-09-18/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "reuters.com"
        source_url: "https://www.reuters.com/world/us/trump-signs-russia-sanctions-bill-into-law-2026-09-18/"
        retrieved_at: "2026-09-19T07:47:13+00:00"
  - type: "pm_response"
    notes: "The Polymarket contract at 8% reflects a market that sees little diplomatic convergence despite Trump's stated openness to Russia negotiations."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "reuters.com: Trump signs Russia sanctions bill into law | Reuters"
    url: "https://www.reuters.com/world/us/trump-signs-russia-sanctions-bill-into-law-2026-09-18/"
    published_at: "2026-09-18T00:00:00.000Z"
    retrieved_at: "2026-09-19T07:47:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
