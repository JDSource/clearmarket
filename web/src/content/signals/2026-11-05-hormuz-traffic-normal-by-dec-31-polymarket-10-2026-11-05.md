---
signal_id: "CMSIG2026110506"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-10-2026-11-05"
headline: "Hormuz traffic normal by Dec 31: Polymarket 10%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end stays a long shot"
telemetry: "Polymarket 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-05T13:20:11.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.1
  volume_24h_usd: 297230.607457
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 is priced at 10%, reflecting low confidence in a near-term resolution."
  - "The latest tanker incidents in the Persian Gulf are consistent with the low-odds pricing; active interdiction operations directly undercut any near-term normalization thesis."
  - "Trump acknowledged the Iran war hurt Republicans in the midterms, raising the political pressure to seek a resolution, but markets are not yet pricing any ceasefire pathway."
  - "Resolves via Polymarket's UMA oracle; the question hinges on a broadly accepted definition of 'normal' traffic, which adds judgment risk to settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's Islamic Revolutionary Guard Corps reported two oil tankers and a tugboat caught fire after using unauthorized routes through the Persian Gulf, with vessels struck by projectiles off Qatar's coast."
    publisher: "Ammanuel Desta"
    published_at: "2026-11-05T13:20:11.000Z"
    source_url: "https://www.justsecurity.org/163503/early-edition-november-5-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ammanuel Desta"
        source_url: "https://www.justsecurity.org/163503/early-edition-november-5-2026/"
        retrieved_at: "2026-11-05T16:02:36+00:00"
  - type: "pm_response"
    notes: "Polymarket at 10% reflects active conflict conditions; no companion contract with a price was available to build a term-structure comparison."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ammanuel Desta: Early Edition: November 5, 2026"
    url: "https://www.justsecurity.org/163503/early-edition-november-5-2026/"
    published_at: "2026-11-05T13:20:11.000Z"
    retrieved_at: "2026-11-05T16:02:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
