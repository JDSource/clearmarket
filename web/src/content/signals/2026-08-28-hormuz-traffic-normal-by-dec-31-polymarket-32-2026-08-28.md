---
signal_id: "CMSIG2026082804"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-32-2026-08-28"
headline: "Hormuz traffic normal by Dec 31: Polymarket 32%"
semantic_title: "Strait of Hormuz returning to normal by year-end stays a long shot"
telemetry: "Polymarket 32%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-28T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.32
  volume_24h_usd: 76812.038683
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 32% chance Strait of Hormuz traffic returns to normal by December 31, resolved via UMA oracle."
  - "Qatar's mediation and Iran's willingness to draft conditions are positive signals, but the market assigns only roughly one-in-three odds of full restoration by year-end."
  - "Trump's concurrent rejection of the June MoU terms, reported separately, helps explain why the market stays well below 50% despite active diplomacy."
  - "Resolution requires verified normalization of shipping traffic through the Strait, not merely a diplomatic agreement, a higher bar that adds timeline risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Mediators are stepping up efforts to reopen the Strait of Hormuz, with Tehran agreeing to draft conditions for restoring normal traffic following a Qatari diplomatic intervention."
    publisher: "nbcnews.com"
    published_at: "2026-08-28T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/world/iran/iran-war-mediators-focus-reopening-strait-hormuz-rcna594850"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nbcnews.com"
        source_url: "https://www.nbcnews.com/world/iran/iran-war-mediators-focus-reopening-strait-hormuz-rcna594850"
        retrieved_at: "2026-08-28T19:51:53+00:00"
  - type: "pm_response"
    notes: "Polymarket at 32% reflects diplomatic progress tempered by Trump's hardened sanctions posture and the gap between talks and operational reopening."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nbcnews.com: Iran war mediators focus on reopening Strait of Hormuz"
    url: "https://www.nbcnews.com/world/iran/iran-war-mediators-focus-reopening-strait-hormuz-rcna594850"
    published_at: "2026-08-28T00:00:00.000Z"
    retrieved_at: "2026-08-28T19:51:53+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
