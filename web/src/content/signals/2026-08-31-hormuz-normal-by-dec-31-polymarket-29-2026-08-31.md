---
signal_id: "CMSIG2026083104"
signal_slug: "hormuz-normal-by-dec-31-polymarket-29-2026-08-31"
headline: "Hormuz normal by Dec 31: Polymarket 29%"
semantic_title: "Strait of Hormuz reopening by year-end stays below 30 percent"
telemetry: "Polymarket 29%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-31T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.29
  volume_24h_usd: 65893.814973
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 29% on the Strait of Hormuz returning to normal traffic by December 31, resolving via UMA oracle."
  - "Trump's vow to hit Iran hard and Tehran keeping the strait shut is consistent with the market's low-odds view on near-term reopening."
  - "Iran's conditional ceasefire offer provides some diplomatic optionality, but the 29% price suggests markets treat it as a long shot."
  - "No near-term Hormuz contract with a price was available for comparison, but the year-end 29% price already reflects a protracted standoff scenario."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump vowed to hit Iran hard after the first US-Iran exchange of fire in weeks, while Iran said it would return to a ceasefire if the US does."
    publisher: "channelnewsasia.com"
    published_at: "2026-08-31T00:00:00.000Z"
    source_url: "https://www.channelnewsasia.com/world/trump-vows-hit-back-hard-after-first-exchange-fire-iran-in-weeks-6352671"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "channelnewsasia.com"
        source_url: "https://www.channelnewsasia.com/world/trump-vows-hit-back-hard-after-first-exchange-fire-iran-in-weeks-6352671"
        retrieved_at: "2026-09-01T13:00:06+00:00"
  - type: "pm_response"
    notes: "Polymarket at 29% on full Hormuz normalization by year-end; the conditional ceasefire offer from Iran has not materially shifted the odds."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "channelnewsasia.com: Trump vows to hit back 'hard' after first exchange of fire with Iran i"
    url: "https://www.channelnewsasia.com/world/trump-vows-hit-back-hard-after-first-exchange-fire-iran-in-weeks-6352671"
    published_at: "2026-08-31T00:00:00.000Z"
    retrieved_at: "2026-09-01T13:00:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
