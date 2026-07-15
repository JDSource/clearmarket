---
signal_id: "CMSIG2026071504"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-56-2026-07-15"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 56%"
semantic_title: "Hormuz normalcy by year-end sits at a bare majority after blockade returns"
telemetry: "Polymarket 56%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-15T03:25:34.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.56
  volume_24h_usd: 16544.881223
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by December 31 at 56%, a slim majority."
  - "US reimposing the blockade and Iran threatening total energy export halt represent a clear escalation, yet the contract holds above 50%."
  - "Companion Polymarket contract CM-EVT-4J73Y3RD96 prices normalization by July 31 at just 1%, confirming the market sees no near-term resolution."
  - "Resolves via Polymarket's uma_oracle; the December 31 horizon gives roughly five months for a diplomatic or military resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US reimposed its naval blockade on Iranian ports after Tehran attacked ships in the Strait of Hormuz, with Iran threatening to halt all Middle East energy exports."
    publisher: "apnews.com"
    published_at: "2026-07-15T03:25:34.000Z"
    source_url: "https://apnews.com/article/iran-us-hormuz-strait-war-july-15-2026-b7c592f269d822407dd6b5641602bf25"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/iran-us-hormuz-strait-war-july-15-2026-b7c592f269d822407dd6b5641602bf25"
        retrieved_at: "2026-07-15T10:00:10+00:00"
  - type: "pm_response"
    notes: "Polymarket at 56% for year-end normalization is consistent with the market treating the blockade as prolonged but not permanent."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: US military reimposes its blockade of Iranian ports | AP News"
    url: "https://apnews.com/article/iran-us-hormuz-strait-war-july-15-2026-b7c592f269d822407dd6b5641602bf25"
    published_at: "2026-07-15T03:25:34.000Z"
    retrieved_at: "2026-07-15T10:00:10+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
