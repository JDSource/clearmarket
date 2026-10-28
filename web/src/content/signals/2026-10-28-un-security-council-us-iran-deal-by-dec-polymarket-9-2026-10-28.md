---
signal_id: "CMSIG2026102805"
signal_slug: "un-security-council-us-iran-deal-by-dec-polymarket-9-2026-10-28"
headline: "UN Security Council US-Iran deal by Dec: Polymarket 9%"
semantic_title: "UN Security Council endorsing a US-Iran deal stays a long shot"
telemetry: "Polymarket 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T00:00:00.000Z"
event_id: "CM-EVT-1B57MJ14Q5"
event_slug: "will-the-unsc-adopt-a-resolution-endorsing-the-final-us-iran-deal-by-date"
event_question: "Will the UN Security Council pass a resolution endorsing a final U.S.-Iran deal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0c7245047183848e41555dc9a5ccc14c970a0711a3591bebc8310119cbae64c0"
  question_raw: "UNSC Resolution Endorsing Final U.S.-Iran Deal by December 31?"
  current_price: 0.09
  volume_24h_usd: 1.12
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket places 9% on the UN Security Council passing a resolution endorsing a final US-Iran deal by December, resolving via uma_oracle."
  - "Iran's rejection of the Qatari proposal as unacceptable is consistent with the Polymarket contract's deep discount; the market is not pricing a diplomatic breakthrough."
  - "Houthi attacks on Saudi oil facilities add a further military escalation layer that the 9% pricing appears to incorporate as a complicating factor."
  - "The Polymarket contract on Hormuz returning to normal by year-end at 12% (CM-EVT-LCPV825X09) trades slightly above the UN deal contract, implying the market sees a partial reopening as marginally more likely than a full formal settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran rejected Qatar's seven-day peace plan as unacceptable, refusing to compromise on nuclear talks as Houthi attacks on Saudi facilities escalate."
    publisher: "Reuters, ynet Global"
    published_at: "2026-10-28T00:00:00.000Z"
    source_url: "https://www.ynetnews.com/article/bkbihrjazl"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters, ynet Global"
        source_url: "https://www.ynetnews.com/article/bkbihrjazl"
        retrieved_at: "2026-10-28T14:49:33+00:00"
  - type: "pm_response"
    notes: "Polymarket at 9% on a UN-endorsed US-Iran deal reflects Iran's public rejection of Qatar's draft proposal and the absence of any agreed negotiating framework."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters, ynet Global: Report: Qatar presents Iran new 7-day peace plan to end war with US an"
    url: "https://www.ynetnews.com/article/bkbihrjazl"
    published_at: "2026-10-28T00:00:00.000Z"
    retrieved_at: "2026-10-28T14:49:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
