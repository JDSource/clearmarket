---
signal_id: "CMSIG2026091905"
signal_slug: "trump-greenland-deal-by-dec-31-polymarket-95-2026-09-19"
headline: "Trump-Greenland deal by Dec 31: Polymarket 95%"
semantic_title: "Trump-Greenland deal by year-end stays heavily favored"
telemetry: "Polymarket 95%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-19T00:00:00.000Z"
event_id: "CM-EVT-M8SXSN1YS7"
event_slug: "trump-x-greenland-deal-signed-by-december-31"
event_question: "Will a Trump-Greenland deal be signed by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6a7aed00fae37de19e0b789a6b50a7475ff1afa898c50b9da11ca733a23199fa"
  question_raw: "Trump x Greenland deal signed by December 31?"
  current_price: 0.954
  volume_24h_usd: 139988.76515099997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 95% odds on a Trump-Greenland deal being signed by December 31, 2026."
  - "The news confirms a deal framework exists, which is consistent with near-full pricing, the market treats the sovereignty dispute as a semantic issue, not a deal-breaker."
  - "Companion contracts on a US invasion of Greenland (3%) and a US-Denmark military clash (2%) remain at very low levels, suggesting markets see this as a diplomatic arrangement, not a conflict."
  - "Resolution via uma_oracle; the key edge case is whether the formal signing of a security cooperation agreement meets the contract's definition of a 'deal.'"
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Greenland and Denmark stated that a US security deal struck with Trump will not cede sovereignty, while Trump declared permanent US control over Greenland security."
    publisher: "Stine Jacobsen"
    published_at: "2026-09-19T00:00:00.000Z"
    source_url: "https://www.reuters.com/world/europe/greenland-denmark-say-us-deal-will-not-cede-sovereignty-2026-09-19/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Stine Jacobsen"
        source_url: "https://www.reuters.com/world/europe/greenland-denmark-say-us-deal-will-not-cede-sovereignty-2026-09-19/"
        retrieved_at: "2026-09-19T12:14:43+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via uma_oracle at 95%; the sovereignty framing dispute between Copenhagen and Washington does not appear to register as a material risk to contract resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Stine Jacobsen: Greenland, Denmark say US deal will not cede sovereignty | Reuters"
    url: "https://www.reuters.com/world/europe/greenland-denmark-say-us-deal-will-not-cede-sovereignty-2026-09-19/"
    published_at: "2026-09-19T00:00:00.000Z"
    retrieved_at: "2026-09-19T12:14:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
