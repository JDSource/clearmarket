---
signal_id: "CMSIG2026072905"
signal_slug: "iranian-regime-falls-before-2027-polymarket-9-2026-07-29"
headline: "Iranian regime falls before 2027: Polymarket 9%"
semantic_title: "Iranian regime survival holds as long odds stay at 9%"
telemetry: "Polymarket 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-29T00:00:00.000Z"
event_id: "CM-EVT-QNQ4VPVP80"
event_slug: "will-the-iranian-regime-fall-by-the-end-of-2026"
event_question: "Will the Iranian regime fall before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbb4d51e6364066d92eb6f9b8413dd7193de70966736044463b205834805a1f3b"
  question_raw: "Will the Iranian regime fall before 2027?"
  current_price: 0.09
  volume_24h_usd: 145671.09416999997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 9% on the Iranian regime falling before 2027, despite an active ballistic missile exchange with U.S. forces."
  - "CENTCOM confirmed Iran fired on U.S. positions; the low 9% probability suggests markets do not view the current escalation as regime-threatening."
  - "A companion Polymarket contract prices a 24% chance the U.S. invades Iran before 2027, a higher bar that markets still treat as unlikely."
  - "Resolves via UMA oracle; the distinction between regime survival and U.S. invasion is key, as air-intercept operations alone are unlikely to trigger resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's IRGC fired multiple ballistic missiles at U.S. forces in the Middle East in what CENTCOM described as an attempted surprise attack; all missiles were intercepted."
    publisher: "aa.com.tr"
    published_at: "2026-07-29T00:00:00.000Z"
    source_url: "https://www.aa.com.tr/en/us-israel-iran-war/all-iranian-ballistic-missiles-intercepted-after-attempted-attack-on-us-forces-in-middle-east-centcom/4012019"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aa.com.tr"
        source_url: "https://www.aa.com.tr/en/us-israel-iran-war/all-iranian-ballistic-missiles-intercepted-after-attempted-attack-on-us-forces-in-middle-east-centcom/4012019"
        retrieved_at: "2026-07-29T10:35:12+00:00"
  - type: "pm_response"
    notes: "Polymarket covers both regime collapse at 9% and U.S. invasion at 24%, with the spread reflecting market skepticism that current strikes escalate to either outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aa.com.tr: All Iranian ballistic missiles intercepted after attempted attack on U"
    url: "https://www.aa.com.tr/en/us-israel-iran-war/all-iranian-ballistic-missiles-intercepted-after-attempted-attack-on-us-forces-in-middle-east-centcom/4012019"
    published_at: "2026-07-29T00:00:00.000Z"
    retrieved_at: "2026-07-29T10:35:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
