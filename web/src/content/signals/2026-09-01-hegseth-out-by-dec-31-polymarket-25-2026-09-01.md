---
signal_id: "CMSIG2026090105"
signal_slug: "hegseth-out-by-dec-31-polymarket-25-2026-09-01"
headline: "Hegseth out by Dec 31: Polymarket 25%"
semantic_title: "Hegseth out as Defense Secretary by December stays near 25 percent"
telemetry: "Polymarket 25%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-01T03:16:49.000Z"
event_id: "CM-EVT-JWSH7Q94S8"
event_slug: "pete-hegseth-out-as-secretary-of-defense-by-december-31"
event_question: "Will Pete Hegseth be out as Secretary of Defense by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0fcfcfc35d71424c0693c717d2e3bc9b8992910835d124d80cd2f01498f1d3dc"
  question_raw: "Pete Hegseth out as Secretary of Defense by December 31?"
  current_price: 0.25
  volume_24h_usd: 11268.266219
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 25% on Pete Hegseth leaving as Secretary of Defense by December 31, resolving via UMA oracle."
  - "Driscoll's resignation amid friction with Hegseth is a concrete signal of Pentagon tension, and trading volume on this contract rose 1,799% day over day."
  - "The surge in volume indicates fresh market attention on the Hegseth exit question following the Driscoll news."
  - "At 25%, the market does not treat Hegseth's departure as a base case, but the volume spike suggests the Driscoll exit is viewed as a meaningful new data point."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US Army Secretary Dan Driscoll resigned after months of friction with Pete Hegseth, as US-Iran hostilities resumed in the Hormuz region."
    publisher: "gulfnews.com"
    published_at: "2026-09-01T03:16:49.000Z"
    source_url: "https://gulfnews.com/world/mena/us-iran-war-hormuz-oil-flows-rebound-to-two-thirds-as-trump-warns-of-more-strikes-on-tehran-us-army-secretary-driscoll-resigns-1.500658835"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "gulfnews.com"
        source_url: "https://gulfnews.com/world/mena/us-iran-war-hormuz-oil-flows-rebound-to-two-thirds-as-trump-warns-of-more-strikes-on-tehran-us-army-secretary-driscoll-resigns-1.500658835"
        retrieved_at: "2026-09-01T13:00:06+00:00"
  - type: "pm_response"
    notes: "Polymarket at 25% with volume up roughly 19x day over day; the Driscoll resignation is drawing significant fresh trading interest in the Hegseth contract."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "gulfnews.com: US-Iran war: Hormuz oil flows rebound to two-thirds as Trump warns of"
    url: "https://gulfnews.com/world/mena/us-iran-war-hormuz-oil-flows-rebound-to-two-thirds-as-trump-warns-of-more-strikes-on-tehran-us-army-secretary-driscoll-resigns-1.500658835"
    published_at: "2026-09-01T03:16:49.000Z"
    retrieved_at: "2026-09-01T13:00:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
