---
signal_id: "CMSIG2026100107"
signal_slug: "hegseth-out-as-defense-sec-by-dec-31-polymarket-21-2026-10-01"
headline: "Hegseth out as Defense Sec by Dec 31: Polymarket 21%"
semantic_title: "Pete Hegseth out as Defense Secretary by year-end holds near 25%"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-01T00:00:00.000Z"
event_id: "CM-EVT-JWSH7Q94S8"
event_slug: "pete-hegseth-out-as-secretary-of-defense-by-december-31"
event_question: "Will Pete Hegseth be out as Secretary of Defense by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0fcfcfc35d71424c0693c717d2e3bc9b8992910835d124d80cd2f01498f1d3dc"
  question_raw: "Pete Hegseth out as Secretary of Defense by December 31?"
  current_price: 0.21
  volume_24h_usd: 1309.04
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 21% on Defense Secretary Pete Hegseth departing by December 31, 2026, a meaningful but minority probability."
  - "Taxpayer-funded ad spending and midterm campaign activity suggest the administration is focused on consolidation, not cabinet reshuffling, broadly consistent with the sub-25% pricing."
  - "No confirmed reporting of imminent Hegseth departure; the 21% price reflects accumulated background risk rather than a specific catalyst."
  - "Resolution via UMA oracle requires Hegseth to officially leave the role; acting or interim replacements would also satisfy the contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Trump administration is spending millions in taxpayer-funded promotional ads defending presidential policies ahead of the midterms."
    publisher: "Mariam Khan"
    published_at: "2026-10-01T00:00:00.000Z"
    source_url: "https://abcnews.com/Politics/trump-defends-spending-millions-taxpayer-funded-promotional-ads/story?id=136922737"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Mariam Khan"
        source_url: "https://abcnews.com/Politics/trump-defends-spending-millions-taxpayer-funded-promotional-ads/story?id=136922737"
        retrieved_at: "2026-10-04T07:47:36+00:00"
  - type: "pm_response"
    notes: "Polymarket at 21% is the only priced contract available; a separate contract for departure by July 31 has no price, leaving year-end as the only available market read on this cabinet tenure question."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Mariam Khan: Trump defends spending millions on taxpayer-funded promotional ads: 'F"
    url: "https://abcnews.com/Politics/trump-defends-spending-millions-taxpayer-funded-promotional-ads/story?id=136922737"
    published_at: "2026-10-01T00:00:00.000Z"
    retrieved_at: "2026-10-04T07:47:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
