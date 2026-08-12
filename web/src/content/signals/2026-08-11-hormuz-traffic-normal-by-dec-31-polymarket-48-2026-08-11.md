---
signal_id: "CMSIG2026081105"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-48-2026-08-11"
headline: "Hormuz traffic normal by Dec 31: Polymarket 48%"
semantic_title: "Hormuz normalization odds hold near 50% as blockade hardens"
telemetry: "Polymarket 48%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-11T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.48
  volume_24h_usd: 223078.49461400005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 48% chance Strait of Hormuz traffic normalizes by December 31, unchanged from near-even pricing amid escalating blockade enforcement."
  - "U.S. firing on a vessel and Iran's 'clear message' that the strait stays shut are consistent with the market's refusal to price a clear resolution."
  - "The near-50% reading means the market is neither pricing a clean diplomatic breakthrough nor a permanent shutdown through year-end."
  - "Resolves via Polymarket's UMA oracle; as previously noted, the standard is likely a return to pre-crisis traffic volumes, not a political announcement alone."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The U.S. military fired on a ship violating its Hormuz blockade, and Trump reiterated claims of total U.S. control even as Iran signaled the strait would stay shut."
    publisher: "independent.co.uk"
    published_at: "2026-08-11T00:00:00.000Z"
    source_url: "https://www.independent.co.uk/news/world/middle-east/iran-us-war-live-trump-hormuz-nuclear-deal-oil-news-b3030821.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "independent.co.uk"
        source_url: "https://www.independent.co.uk/news/world/middle-east/iran-us-war-live-trump-hormuz-nuclear-deal-oil-news-b3030821.html"
        retrieved_at: "2026-08-12T09:07:43+00:00"
  - type: "pm_response"
    notes: "Polymarket is the sole priced venue; duplicate wires on this contract reflect multiple distinct news catalysts all landing at the same 48% price."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "independent.co.uk: Iran-US war latest: Trump claims total control of Hormuz as he demands"
    url: "https://www.independent.co.uk/news/world/middle-east/iran-us-war-live-trump-hormuz-nuclear-deal-oil-news-b3030821.html"
    published_at: "2026-08-11T00:00:00.000Z"
    retrieved_at: "2026-08-12T09:07:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
