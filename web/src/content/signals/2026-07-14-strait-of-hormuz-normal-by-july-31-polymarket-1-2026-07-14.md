---
signal_id: "CMSIG2026071405"
signal_slug: "strait-of-hormuz-normal-by-july-31-polymarket-1-2026-07-14"
headline: "Strait of Hormuz normal by July 31: Polymarket 1%"
semantic_title: "July Hormuz normalization nearly fully priced out after mutual strikes"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-14T09:22:36.000Z"
event_id: "CM-EVT-4J73Y3RD96"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-july-31"
event_question: "Will Strait of Hormuz traffic return to normal by July 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb8e6d129a06d0ccb21d7b32eb529ea455eddba3cf29bfa097112202cbdf5bf21"
  question_raw: "Strait of Hormuz traffic returns to normal by July 31?"
  current_price: 0.012
  volume_24h_usd: 507384.6706909999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by July 31 at just 1%, effectively fully pricing out near-term resolution."
  - "Active mutual strikes and Iran's vow to keep the strait closed are fully consistent with this near-zero probability."
  - "The 55-percentage-point gap between the July contract at 1% and the December contract at 56% maps a steep resolution timeline the market expects to stretch into late 2026."
  - "Resolves via Polymarket uma_oracle; any verifiable return to normal commercial transit volume would trigger resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US forces struck Iran and reimposed a naval blockade as Tehran vowed the Strait would stay closed until the US ends its aggression."
    publisher: "al-monitor.com"
    published_at: "2026-07-14T09:22:36.000Z"
    source_url: "https://www.al-monitor.com/originals/2026/07/us-launches-new-iran-strikes-reimposes-naval-blockade"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "al-monitor.com"
        source_url: "https://www.al-monitor.com/originals/2026/07/us-launches-new-iran-strikes-reimposes-naval-blockade"
        retrieved_at: "2026-07-15T10:00:10+00:00"
  - type: "pm_response"
    notes: "Polymarket at 1% for July 31 is the sharpest near-term read available; the contract and the news are in full alignment."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "al-monitor.com: US renews blockade, trades strikes with Iran over Hormuz strait - AL-M"
    url: "https://www.al-monitor.com/originals/2026/07/us-launches-new-iran-strikes-reimposes-naval-blockade"
    published_at: "2026-07-14T09:22:36.000Z"
    retrieved_at: "2026-07-15T10:00:10+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
