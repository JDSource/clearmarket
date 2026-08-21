---
signal_id: "CMSIG2026081907"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-29-2026-08-19"
headline: "Hormuz traffic normal by Dec 31: Polymarket 29%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end near 25 percent"
telemetry: "Polymarket 29%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-19T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.29
  volume_24h_usd: 121319.82586700002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract puts 29% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "The UAE embargo follows missile attacks and compounds the Hormuz disruption; Polymarket pricing treats a full normalization this year as unlikely but not negligible."
  - "Trump separately threatened economic consequences on countries aiding Iran, adding another escalation layer the market has not priced as resolvable near-term."
  - "Resolves via Polymarket UMA oracle; defining what constitutes normal traffic is a key settlement ambiguity given ongoing partial flows."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The UAE imposed an indefinite trade embargo on Iran after missile strikes, further escalating Persian Gulf tensions and disrupting regional trade flows."
    publisher: "Al Jazeera Staff"
    published_at: "2026-08-19T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/8/19/uae-imposes-indefinite-trade-embargo-on-iran-over-alleged-missile-attacks"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/8/19/uae-imposes-indefinite-trade-embargo-on-iran-over-alleged-missile-attacks"
        retrieved_at: "2026-08-21T08:35:01+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 29% price implies the market treats Gulf de-escalation before year-end as a low-probability scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: UAE imposes indefinite trade embargo on Iran over alleged missile atta"
    url: "https://www.aljazeera.com/news/2026/8/19/uae-imposes-indefinite-trade-embargo-on-iran-over-alleged-missile-attacks"
    published_at: "2026-08-19T00:00:00.000Z"
    retrieved_at: "2026-08-21T08:35:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
