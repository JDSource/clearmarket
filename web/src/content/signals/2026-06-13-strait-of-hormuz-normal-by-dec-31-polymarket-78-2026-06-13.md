---
signal_id: "CMSIG2026061302"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-78-2026-06-13"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 78%"
semantic_title: "Hormuz full-year reopening consensus holds near 78 percent"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-13T03:47:45.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Strait of Hormuz traffic normalization by Dec 31 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.78
  volume_24h_usd: 289674.7514719999
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Hormuz traffic returning to normal by December 31 at 78%, reflecting moderate confidence in a year-end resolution."
  - "Near-term Hormuz contracts tell a different story: normal by June 15 at 1%, normal by June 30 at 18%, confirming the market sees a deal as unlikely to reopen the strait immediately."
  - "The spread between June 30 (18%) and December 31 (78%) implies the market prices in a multi-month gap between any deal signing and full traffic restoration."
  - "Resolves via IMF PortWatch data at portwatch.imf.org; traffic must return to pre-conflict baseline levels."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US and Iranian officials describe a landmark accord in its final stages, with Pakistan mediating and sanctions relief on the table."
    publisher: "Balaram Menon"
    published_at: "2026-06-13T03:47:45.000Z"
    source_url: "https://gulfnews.com/world/mena/end-of-war-in-sight-as-us-and-iran-close-in-on-landmark-accord-1.500572912"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Balaram Menon"
        source_url: "https://gulfnews.com/world/mena/end-of-war-in-sight-as-us-and-iran-close-in-on-landmark-accord-1.500572912"
        retrieved_at: "2026-06-13T10:25:37+00:00"
  - type: "pm_response"
    notes: "Polymarket's term structure across three Hormuz contracts shows sharp timeline doubt: the market credits a deal eventually but not imminently."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Balaram Menon: Landmark US, Iran Accord in Final Stage: Pakistan Mediation, Drone Inte"
    url: "https://gulfnews.com/world/mena/end-of-war-in-sight-as-us-and-iran-close-in-on-landmark-accord-1.500572912"
    published_at: "2026-06-13T03:47:45.000Z"
    retrieved_at: "2026-06-13T10:25:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
