---
signal_id: "CMSIG2026071301"
signal_slug: "us-invade-iran-by-2027-polymarket-18-2026-07-13"
headline: "US invade Iran by 2027: Polymarket 18%"
semantic_title: "US-Iran invasion pricing wavers amid active Gulf combat"
telemetry: "Polymarket 18%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-13T06:50:28.000Z"
event_id: "CM-EVT-WD982793G1"
event_slug: "will-the-us-invade-iran-before-2027"
event_question: "Will the U.S. invade Iran before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5db999fad322cea2914535aae5517060c3f80ad6d8c0231cde2124a434d16846"
  question_raw: "Will the U.S. invade Iran before 2027?"
  current_price: 0.18
  volume_24h_usd: 152652.35095500003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 18% on a US ground invasion of Iran before 2027, despite active US air strikes across dozens of Iranian sites."
  - "Markets distinguish air-strike campaign from full invasion; current news is consistent with limited kinetic engagement, not occupation."
  - "Companion Polymarket contract on Iranian regime survival has no active price, leaving the invasion-vs-regime-change spread unresolved."
  - "Resolves via Polymarket's UMA oracle; contract language likely turns on ground troop deployment, not air strikes alone."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US and Iranian forces exchanged strikes across the Gulf as Iran declared the Strait of Hormuz closed and widened attacks on Gulf states including Oman."
    publisher: "straitstimes.com"
    published_at: "2026-07-13T06:50:28.000Z"
    source_url: "https://www.straitstimes.com/world/iran-escalates-attacks-on-us-bases-in-gulf-states-warns-of-more-incidents-in-strait"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "straitstimes.com"
        source_url: "https://www.straitstimes.com/world/iran-escalates-attacks-on-us-bases-in-gulf-states-warns-of-more-incidents-in-strait"
        retrieved_at: "2026-07-13T10:56:18+00:00"
  - type: "pm_response"
    notes: "Polymarket at 18% prices the invasion scenario as a tail risk, not a base case, even as fourth-round US strikes and Hormuz closure dominate headlines."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "straitstimes.com: Iran widens attacks on US bases in Gulf, Hormuz tensions lift oil pric"
    url: "https://www.straitstimes.com/world/iran-escalates-attacks-on-us-bases-in-gulf-states-warns-of-more-incidents-in-strait"
    published_at: "2026-07-13T06:50:28.000Z"
    retrieved_at: "2026-07-13T10:56:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
