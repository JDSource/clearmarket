---
signal_id: "CMSIG2026091205"
signal_slug: "strait-of-hormuz-normalizes-by-dec-31-polymarket-21-2026-09-12"
headline: "Strait of Hormuz normalizes by Dec 31: Polymarket 21%"
semantic_title: "Strait of Hormuz returning to normal by year-end stays below 25%"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-12T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.21
  volume_24h_usd: 118401.44973699999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 21% on Strait of Hormuz traffic returning to normal by December 31, keeping the outcome a long shot."
  - "Houthi seizure of the Red Sea coast and strategic islands, combined with the Saudi East-West pipeline shutdown from drone strikes, deepens the disruption narrative."
  - "The 21% pricing implies the market sees a roughly four-in-five chance that shipping disruption persists through year-end, consistent with escalating rather than de-escalating conflict."
  - "Polymarket resolves via UMA oracle; 'normal' traffic would need to be defined against a pre-conflict baseline, creating resolution ambiguity if partial recovery occurs."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Houthis seized Yemen's entire Red Sea coast and three strategic islands, tightening their grip on global shipping lanes."
    publisher: "channelnewsasia.com"
    published_at: "2026-09-12T00:00:00.000Z"
    source_url: "https://www.channelnewsasia.com/world/yemen-houthis-red-sea-shipping-iran-war-6379706"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "channelnewsasia.com"
        source_url: "https://www.channelnewsasia.com/world/yemen-houthis-red-sea-shipping-iran-war-6379706"
        retrieved_at: "2026-09-12T11:56:19+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 21% is directionally consistent with the news of Houthi expansion and pipeline closure, with no evidence of a normalizing path."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "channelnewsasia.com: Yemen's Houthis take over strait vital to global shipping - CNA"
    url: "https://www.channelnewsasia.com/world/yemen-houthis-red-sea-shipping-iran-war-6379706"
    published_at: "2026-09-12T00:00:00.000Z"
    retrieved_at: "2026-09-12T11:56:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
