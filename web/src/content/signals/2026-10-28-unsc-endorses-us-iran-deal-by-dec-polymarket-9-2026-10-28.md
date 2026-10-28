---
signal_id: "CMSIG2026102806"
signal_slug: "unsc-endorses-us-iran-deal-by-dec-polymarket-9-2026-10-28"
headline: "UNSC endorses US-Iran deal by Dec: Polymarket 9%"
semantic_title: "UN Security Council endorsing a US-Iran deal by December stays near long-shot"
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
  - "The Polymarket contract puts 9% odds on the UN Security Council passing a resolution endorsing a final US-Iran deal by December 2026."
  - "Iran's flat rejection of the Qatari plan is directionally consistent with this long-shot pricing, the market had already discounted a rapid resolution."
  - "The Strait of Hormuz Polymarket contract at 12% (CM-EVT-LCPV825X09) sits only marginally above this, indicating the market sees both a deal and reopening as near-equivalent long shots."
  - "Resolves via UMA oracle; a UNSC endorsement requires not just a deal but a formal Security Council vote, a higher bar than a bilateral ceasefire."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran publicly rejected Qatar's proposed seven-day peace plan as 'unacceptable,' escalating tensions even as regional mediators continued shuttle diplomacy."
    publisher: "Reuters, ynet Global"
    published_at: "2026-10-28T00:00:00.000Z"
    source_url: "https://www.ynetnews.com/article/bkbihrjazl"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters, ynet Global"
        source_url: "https://www.ynetnews.com/article/bkbihrjazl"
        retrieved_at: "2026-10-28T15:33:55+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 9% reflects broad skepticism that diplomacy can deliver a UNSC-endorsed deal before year-end, consistent with Iran's public rejection of the latest Qatari draft."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters, ynet Global: Report: Qatar presents Iran new 7-day peace plan to end war with US an"
    url: "https://www.ynetnews.com/article/bkbihrjazl"
    published_at: "2026-10-28T00:00:00.000Z"
    retrieved_at: "2026-10-28T15:33:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
