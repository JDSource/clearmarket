---
signal_id: "CMSIG2026092802"
signal_slug: "sept-payrolls-implied-90k-100k-kalshi-ladder-2026-09-28"
headline: "Sept payrolls implied 90K-100K: Kalshi ladder"
semantic_title: "September payrolls hold near 50/50 odds around 90K to 100K"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-28T06:22:53.000Z"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "September 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T100000"
  question_raw: "Will above 100000 jobs be added in September 2026?"
  current_price: 0.45
  volume_24h_usd: 4765.95
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Prediction market ladder implies September payrolls in the 90K-100K range, with 62% above 90K but only 45% above 100K, straddling the consensus 84K forecast."
  - "The wide analyst estimate band of 35K to 180K is reflected in the ladder's gradual probability decay; markets are not pricing a blowout print."
  - "Trading volume surged 738.8x day over day on this contract, the highest volume signal in today's batch, confirming NFP is the dominant near-term macro focus."
  - "A print above 125K (31% odds) would likely reinforce the Kalshi contract pricing 52% on a 4.25% Fed funds upper bound, tightening the October hike call."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Yields are rising sharply as market consensus for September NFP sits at 84,000, with a wide estimate range of 35,000 to 180,000."
    publisher: "fxstreet.com"
    published_at: "2026-09-28T06:22:53.000Z"
    source_url: "https://www.fxstreet.com/analysis/yields-rip-higher-as-focus-shifts-to-jobs-data-202609280622"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "fxstreet.com"
        source_url: "https://www.fxstreet.com/analysis/yields-rip-higher-as-focus-shifts-to-jobs-data-202609280622"
        retrieved_at: "2026-09-29T07:47:25+00:00"
  - type: "pm_response"
    notes: "Contract volume up 73,776% day over day; resolves via Bureau of Labor Statistics payrolls release for September 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "fxstreet.com: Yields rip higher as focus shifts to jobs data"
    url: "https://www.fxstreet.com/analysis/yields-rip-higher-as-focus-shifts-to-jobs-data-202609280622"
    published_at: "2026-09-28T06:22:53.000Z"
    retrieved_at: "2026-09-29T07:47:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
