---
signal_id: "CMSIG2026100205"
signal_slug: "hormuz-back-to-normal-by-dec-31-polymarket-21-2026-10-02"
headline: "Hormuz back to normal by Dec 31: Polymarket 21%"
semantic_title: "Strait of Hormuz back to normal by year-end stays a long shot"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-02T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.21
  volume_24h_usd: 70615.204309
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 21% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "A third U.S. carrier group deploying and a tanker being hit in the Strait are consistent with the market's heavily pessimistic pricing on near-term normalization."
  - "At 21%, the market is pricing continued disruption through year-end as the dominant scenario, not a diplomatic off-ramp."
  - "Resolves via Polymarket's UMA oracle; the September 30 deadline version of the companion question has already lapsed, suggesting the market already priced one miss."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The U.S. is sending a third aircraft carrier strike group to the Middle East as Trump warns of new Iran strikes and a tanker was hit in the Strait of Hormuz."
    publisher: "Anniek Bao"
    published_at: "2026-10-02T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/10/02/us-iran-war-trump-hormuz-.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Anniek Bao"
        source_url: "https://www.cnbc.com/2026/10/02/us-iran-war-trump-hormuz-.html"
        retrieved_at: "2026-10-02T07:47:52+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; escalating U.S. military posture is broadly consistent with the 79% probability of continued disruption."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Anniek Bao: U.S. looks to boost Mideast buildup as Trump warns of new Iran strikes"
    url: "https://www.cnbc.com/2026/10/02/us-iran-war-trump-hormuz-.html"
    published_at: "2026-10-02T00:00:00.000Z"
    retrieved_at: "2026-10-02T07:47:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
