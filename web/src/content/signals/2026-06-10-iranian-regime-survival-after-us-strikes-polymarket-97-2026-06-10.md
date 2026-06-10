---
signal_id: "CMSIG2026061002"
signal_slug: "iranian-regime-survival-after-us-strikes-polymarket-97-2026-06-10"
headline: "Iranian regime survival after US strikes: Polymarket 97%"
semantic_title: "Iranian regime survival consensus anchors near certainty"
telemetry: "Polymarket 97%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-10T02:07:10.000Z"
event_id: "CM-EVT-XYC4HDKBW3"
event_slug: "will-the-iranian-regime-survive-us-military-strikes-741"
event_question: "Will the Iranian regime survive any U.S. military strikes?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xefc69f5f48827e331957acbcc2339eb3b15e27e32453b8e6f29b5de67474c986"
  question_raw: "Will the Iranian regime survive U.S. military strikes?"
  current_price: 0.971
  volume_24h_usd: 10685.813842000001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices Iranian regime survival of US military strikes at 97%, near-certain even as exchanges escalate."
  - "Active tit-for-tat US-Iran strikes are consistent with this high survival probability; markets are not treating current exchanges as existential for the regime."
  - "The longer-horizon Polymarket contract on Iranian regime collapse by December 31, 2026 sits at only 14%, reinforcing the consensus that current strikes are limited in scope."
  - "Resolves via UMA oracle; regime survival likely requires continued state-functioning evidence rather than any single military outcome."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's Revolutionary Guards struck a US base in Jordan and 21 Gulf targets in retaliation for US strikes near the Strait of Hormuz."
    publisher: "rte.ie"
    published_at: "2026-06-10T02:07:10.000Z"
    source_url: "https://www.rte.ie/news/2026/0610/1577653-us-iran/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "rte.ie"
        source_url: "https://www.rte.ie/news/2026/0610/1577653-us-iran/"
        retrieved_at: "2026-06-10T11:36:47+00:00"
  - type: "pm_response"
    notes: "Polymarket's 97% survival read and the separate 14% regime-collapse-by-year-end contract are internally consistent, both reflecting market conviction that current strikes are limited, not regime-ending."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "rte.ie: Iran targets US base in Jordan after Trump orders strikes"
    url: "https://www.rte.ie/news/2026/0610/1577653-us-iran/"
    published_at: "2026-06-10T02:07:10.000Z"
    retrieved_at: "2026-06-10T11:36:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
