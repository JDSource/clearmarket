---
signal_id: "CMSIG2026091907"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-18-2026-09-19"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 18%"
semantic_title: "Strait of Hormuz back to normal by December stays unlikely"
telemetry: "Polymarket 18%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-19T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.18
  volume_24h_usd: 7577.96187
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 18% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Houthi territorial gains and continued disruption of Saudi oil exports are consistent with the market's strong skepticism about a near-term normalization."
  - "Separately, a US blockade of Iranian ports described in adjacent reporting reinforces the structural disruption narrative underpinning this pricing."
  - "Resolution via uma_oracle; the contract's definition of 'normal' traffic levels is the key edge case, as partial recoveries may not meet the threshold."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Houthi forces in Yemen have captured strategic territory and are disrupting Saudi oil exports, threatening the global energy trade and broader Middle East stability."
    publisher: "The Christian Science Monitor"
    published_at: "2026-09-19T00:00:00.000Z"
    source_url: "https://www.csmonitor.com/World/Middle-East/2026/0919/houthis-yemen-saudi-iran-trump-oil"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Christian Science Monitor"
        source_url: "https://www.csmonitor.com/World/Middle-East/2026/0919/houthis-yemen-saudi-iran-trump-oil"
        retrieved_at: "2026-09-19T12:14:43+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via uma_oracle; at 18% the contract prices persistent regional disruption as the base case through year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Christian Science Monitor: Iran-backed Houthis are on the march in Yemen, risking Middle East sta"
    url: "https://www.csmonitor.com/World/Middle-East/2026/0919/houthis-yemen-saudi-iran-trump-oil"
    published_at: "2026-09-19T00:00:00.000Z"
    retrieved_at: "2026-09-19T12:14:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
