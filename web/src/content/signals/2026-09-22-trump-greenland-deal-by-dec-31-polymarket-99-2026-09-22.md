---
signal_id: "CMSIG2026092204"
signal_slug: "trump-greenland-deal-by-dec-31-polymarket-99-2026-09-22"
headline: "Trump-Greenland deal by Dec 31: Polymarket 99%"
semantic_title: "Trump-Greenland deal by December nears full pricing at 99 percent"
telemetry: "Polymarket 99%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-09-22T00:00:00.000Z"
event_id: "CM-EVT-M8SXSN1YS7"
event_slug: "trump-x-greenland-deal-signed-by-december-31"
event_question: "Will a Trump-Greenland deal be signed by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6a7aed00fae37de19e0b789a6b50a7475ff1afa898c50b9da11ca733a23199fa"
  question_raw: "Trump x Greenland deal signed by December 31?"
  current_price: 0.994
  volume_24h_usd: 46358.857532
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market prices a Trump-Greenland deal signed by December 31 at 99%, essentially treating the outcome as resolved."
  - "Reuters reporting that the three parties are set to sign the deal is fully consistent with the near-certain Polymarket pricing, leaving almost no gap between news and market."
  - "The companion Polymarket contract on a US invasion of Greenland sits at just 3%, confirming the market views the diplomatic path as the overwhelmingly likely resolution."
  - "Resolves via Polymarket's uma_oracle resolution mechanism upon confirmation of a signed deal."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Reuters reports that the US, Denmark, and Greenland are set to sign an Arctic sovereignty deal, ending months of standoff."
    publisher: "Jacob Grønholt-Pedersen"
    published_at: "2026-09-22T00:00:00.000Z"
    source_url: "https://www.reuters.com/world/europe/trump-denmark-greenland-sign-deal-bid-end-arctic-standoff-2026-09-22/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jacob Grønholt-Pedersen"
        source_url: "https://www.reuters.com/world/europe/trump-denmark-greenland-sign-deal-bid-end-arctic-standoff-2026-09-22/"
        retrieved_at: "2026-09-22T07:47:31+00:00"
  - type: "pm_response"
    notes: "Polymarket at 99% had already priced this outcome; the Reuters signing report is the news catching up to a market that was near-fully committed well in advance."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jacob Grønholt-Pedersen: Trump, Denmark, Greenland to sign deal in bid to end Arctic standoff |"
    url: "https://www.reuters.com/world/europe/trump-denmark-greenland-sign-deal-bid-end-arctic-standoff-2026-09-22/"
    published_at: "2026-09-22T00:00:00.000Z"
    retrieved_at: "2026-09-22T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
