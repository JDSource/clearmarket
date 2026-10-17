---
signal_id: "CMSIG2026101602"
signal_slug: "fed-cut-above-25bp-this-year-kalshi-3-2026-10-16"
headline: "Fed cut above 25bp this year: Kalshi 3%"
semantic_title: "Odds on outsized Fed rate cut this year stay near long-shot"
telemetry: "Kalshi 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-16T00:00:00.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.029
  volume_24h_usd: 14.51
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract on a Fed rate cut greater than 25 basis points in 2026 sits at just 3%."
  - "With PPI at 6.3% and CPI at 3.7%, the inflation backdrop is squarely inconsistent with easing, the market's near-zero cut probability aligns with the data, not against it."
  - "Warsh's refusal to prejudge meetings leaves the rate path open, but the Kalshi cut contract reflects near-unanimous market conviction that policy moves higher, not lower."
  - "Resolution via the Federal Reserve's own rate decision makes this a clean binary; any cut above 25bp before year-end resolves YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh held cards close on policy as September PPI rose 6.3% annually and September CPI printed 3.7%, reigniting rate hike speculation."
    publisher: "Lim Hui Jie"
    published_at: "2026-10-16T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/10/16/cnbc-daily-open-warsh-holds-cards-close-on-fed-policy-but-inflation-numbers-may-tip-his-hand.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Lim Hui Jie"
        source_url: "https://www.cnbc.com/2026/10/16/cnbc-daily-open-warsh-holds-cards-close-on-fed-policy-but-inflation-numbers-may-tip-his-hand.html"
        retrieved_at: "2026-10-17T07:47:54+00:00"
  - type: "pm_response"
    notes: "Kalshi at 3% on a jumbo cut is consistent across all Fed-related contracts this cycle, the market is firmly positioned for tightening, not easing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Lim Hui Jie: CNBC Daily Open: Warsh holds cards close on Fed policy, but inflation"
    url: "https://www.cnbc.com/2026/10/16/cnbc-daily-open-warsh-holds-cards-close-on-fed-policy-but-inflation-numbers-may-tip-his-hand.html"
    published_at: "2026-10-16T00:00:00.000Z"
    retrieved_at: "2026-10-17T07:47:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
