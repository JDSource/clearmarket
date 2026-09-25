---
signal_id: "CMSIG2026092506"
signal_slug: "strait-of-hormuz-normal-traffic-by-dec-31-polymarket-24-2026-09-25"
headline: "Strait of Hormuz normal traffic by Dec 31: Polymarket 24%"
semantic_title: "Strait of Hormuz back to normal by year-end holds below 25%"
telemetry: "Polymarket 24%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-25T03:49:19.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.24
  volume_24h_usd: 189909.79053200007
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only a 24% chance Strait of Hormuz traffic returns to normal by December 31, 2026."
  - "Iran's hardened public posture in New York aligns with the market's low-probability pricing, diplomats describing a 'phased deal' framework suggests a full reopening this year is unlikely."
  - "Separate Al-Monitor reporting of active US-Iran phased-deal talks is the lone upside catalyst, but the 24% price shows the market is not treating that as a near-term resolution."
  - "Resolves via Polymarket's UMA oracle; the definition of 'normal' Hormuz traffic is the critical settlement question, a partial reopening likely does not trigger resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran hardened its Hormuz stance at the UN General Assembly as New York diplomacy struggled for a breakthrough, with US and Iran reportedly discussing only a phased deal."
    publisher: "Hamza Hendawi"
    published_at: "2026-09-25T03:49:19.000Z"
    source_url: "https://www.thenationalnews.com/news/mena/2026/09/25/iran-hardens-hormuz-stance-as-new-york-diplomacy-struggles-for-breakthrough/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Hamza Hendawi"
        source_url: "https://www.thenationalnews.com/news/mena/2026/09/25/iran-hardens-hormuz-stance-as-new-york-diplomacy-struggles-for-breakthrough/"
        retrieved_at: "2026-09-25T07:47:46+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 24%; resolves via UMA oracle with 'normal traffic' as the settlement standard, creating potential ambiguity around partial reopening scenarios."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Hamza Hendawi: Iran hardens Hormuz stance as New York diplomacy struggles for breakth"
    url: "https://www.thenationalnews.com/news/mena/2026/09/25/iran-hardens-hormuz-stance-as-new-york-diplomacy-struggles-for-breakthrough/"
    published_at: "2026-09-25T03:49:19.000Z"
    retrieved_at: "2026-09-25T07:47:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
