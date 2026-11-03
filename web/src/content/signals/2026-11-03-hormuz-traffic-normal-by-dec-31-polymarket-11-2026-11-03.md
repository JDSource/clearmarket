---
signal_id: "CMSIG2026110306"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-11-2026-11-03"
headline: "Hormuz traffic normal by Dec 31: Polymarket 11%"
semantic_title: "Strait of Hormuz traffic returning to normal stays a long shot"
telemetry: "Polymarket 11%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-03T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.11
  volume_24h_usd: 140945.778974
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts Strait of Hormuz traffic returning to normal by December 31 at just 11%, a strong long-shot read despite diplomatic optimism."
  - "US strikes on Qeshm Island and ongoing indirect talks are pulling in opposite directions; the market is pricing the military escalation as the dominant signal."
  - "Companion Polymarket contract on Israel reopening its embassy in Iran sits at 4%, consistent with the market view that normalization remains very distant."
  - "Resolution via Polymarket UMA oracle; definition of 'normal' traffic levels is a key settlement edge case given ongoing blockade and transit restrictions."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US forces conducted defensive strikes on Iran's Qeshm Island near the Strait of Hormuz as Vance voiced optimism about a diplomatic deal."
    publisher: "Jonathan Yerushalmy"
    published_at: "2026-11-03T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/nov/03/us-strikes-irans-qeshm-island"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jonathan Yerushalmy"
        source_url: "https://www.theguardian.com/world/2026/nov/03/us-strikes-irans-qeshm-island"
        retrieved_at: "2026-11-03T07:48:22+00:00"
  - type: "pm_response"
    notes: "Polymarket at 11% on Hormuz normalization is consistent with the broader Iran deal skepticism reflected across multiple companion contracts in this cycle."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jonathan Yerushalmy: US reportedly strikes Iran’s Qeshm Island as Vance voices optimism abo"
    url: "https://www.theguardian.com/world/2026/nov/03/us-strikes-irans-qeshm-island"
    published_at: "2026-11-03T00:00:00.000Z"
    retrieved_at: "2026-11-03T07:48:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
