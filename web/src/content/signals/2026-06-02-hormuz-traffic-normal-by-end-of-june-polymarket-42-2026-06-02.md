---
signal_id: "CMSIG2026060207"
signal_slug: "hormuz-traffic-normal-by-end-of-june-polymarket-42-2026-06-02"
headline: "Hormuz traffic normal by end of June: Polymarket 42%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-02T13:35:29.000Z"
event_id: "CM-EVT-YPW93GCTK6"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-end-of-june"
event_question: "Will traffic through the Strait of Hormuz return to normal by the end of June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x348cd9adf4f6855f58bd9c6dbf9ff251c4142ef77233a5dc95c65b4b61cd2187"
  question_raw: "Strait of Hormuz traffic returns to normal by end of June?"
  current_price: 0.42
  volume_24h_usd: 301190.48171499977
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices 42% on Strait of Hormuz traffic returning to normal by end of June, versus 86% by December 31."
  - "Trump's one-week deal timeline would need to materialize rapidly to shift the near-term 42% toward the longer-dated 86%; the spread signals serious timeline doubt."
  - "Fraying ceasefire and stalled Iran talks reported elsewhere make the June 30 normalization window tight; the 44-point gap between June and December contracts reflects that uncertainty."
  - "Resolves via portwatch.imf.org shipping traffic data; normalization likely requires sustained passage rates returning to pre-conflict baselines."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump is trying to prevent Israel's Lebanon escalation from derailing an Iran deal, saying a memorandum of understanding could come within a week."
    publisher: "military.com"
    published_at: "2026-06-02T13:35:29.000Z"
    source_url: "https://www.military.com/trump-tries-to-stop-israels-lebanon-push-derailing-an-iran-deal"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "military.com"
        source_url: "https://www.military.com/trump-tries-to-stop-israels-lebanon-push-derailing-an-iran-deal"
        retrieved_at: "2026-06-03T01:50:17+00:00"
  - type: "pm_response"
    notes: "The 44-percentage-point spread between the June (42%) and December (86%) Polymarket Hormuz contracts quantifies the market's skepticism about Trump's one-week deal optimism."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "military.com: Trump Tries to Stop Israel’s Lebanon Push Derailing an Iran Deal"
    url: "https://www.military.com/trump-tries-to-stop-israels-lebanon-push-derailing-an-iran-deal"
    published_at: "2026-06-02T13:35:29.000Z"
    retrieved_at: "2026-06-03T01:50:17+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
