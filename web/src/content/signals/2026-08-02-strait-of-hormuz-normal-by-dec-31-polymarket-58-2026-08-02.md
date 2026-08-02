---
signal_id: "CMSIG2026080205"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-58-2026-08-02"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 58%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end stays near 50-50"
telemetry: "Polymarket 58%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-02T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.58
  volume_24h_usd: 235524.2087829999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices 58% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Trump's ceasefire signal and explicit mention of Hormuz reopening talks are consistent with the market moving above 50%, though Iran's warning of a decisive response keeps full pricing at bay."
  - "Trading volume on related Fed funds contracts surged sharply this session, indicating broader macro repricing linked to the oil supply picture."
  - "A separate contract on Iran agreeing to end uranium enrichment by December 31 sits at just 28% on Polymarket, highlighting the gap between a tactical pause and a durable deal."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "President Trump announced the US has agreed to cancel its Iran attack after deal parameters were reached, with Middle Eastern nations requesting time to finalize a Hormuz reopening agreement."
    publisher: "cbsnews.com"
    published_at: "2026-08-02T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/news/trump-iran-attack-framework-deal-war/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/trump-iran-attack-framework-deal-war/"
        retrieved_at: "2026-08-02T09:52:49+00:00"
  - type: "pm_response"
    notes: "Polymarket at 58% reflects cautious optimism: the ceasefire is real but the path to a signed, implemented Hormuz agreement by year-end remains uncertain."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: Trump signals deal to end Iran war may be imminent, agrees to \"cancel"
    url: "https://www.cbsnews.com/news/trump-iran-attack-framework-deal-war/"
    published_at: "2026-08-02T00:00:00.000Z"
    retrieved_at: "2026-08-02T09:52:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
