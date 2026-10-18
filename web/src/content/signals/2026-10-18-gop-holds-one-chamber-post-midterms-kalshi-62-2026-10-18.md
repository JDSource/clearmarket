---
signal_id: "CMSIG2026101805"
signal_slug: "gop-holds-one-chamber-post-midterms-kalshi-62-2026-10-18"
headline: "GOP holds one chamber post-midterms: Kalshi 62%"
semantic_title: "Republicans holding at least one chamber stays favored near 62 percent"
telemetry: "Kalshi 62%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-18T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.62
  volume_24h_usd: 25077.3
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices a 62% probability that Republicans will control at least one chamber of Congress after the 2026 midterms."
  - "Trump's record-low 33% approval in the Washington Post poll is a bearish signal for Republicans, yet the Kalshi contract still favors GOP retaining at least one chamber."
  - "A companion Kalshi contract prices a 90% probability that Democrats win the US House, implying markets expect a split outcome: Democrats take the House, Republicans keep the Senate."
  - "Resolves via Bureau of Labor Statistics certification of congressional results; the 62% GOP figure reflects the structural Senate map advantage, not presidential approval."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A Washington Post poll showed President Donald Trump's approval at a record low of 33%, with 66% disapproving, giving Democrats a clear midterm edge with the election 16 days away."
    publisher: "Dan Balz"
    published_at: "2026-10-18T00:00:00.000Z"
    source_url: "https://www.washingtonpost.com/politics/2026/10/18/trump-approval-hits-record-low-handing-democrats-clear-midterm-edge/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Dan Balz"
        source_url: "https://www.washingtonpost.com/politics/2026/10/18/trump-approval-hits-record-low-handing-democrats-clear-midterm-edge/"
        retrieved_at: "2026-10-18T12:25:52+00:00"
  - type: "pm_response"
    notes: "Kalshi binary at 62% for Republicans holding at least one chamber; read alongside the 90% Democratic House win contract, the implied split Congress scenario emerges clearly."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Dan Balz: Trump approval hits record low, handing Democrats a clear midterm edge"
    url: "https://www.washingtonpost.com/politics/2026/10/18/trump-approval-hits-record-low-handing-democrats-clear-midterm-edge/"
    published_at: "2026-10-18T00:00:00.000Z"
    retrieved_at: "2026-10-18T12:25:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
