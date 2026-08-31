---
signal_id: "CMSIG2026083007"
signal_slug: "venezuela-presidential-election-kalshi-36-2026-08-30"
headline: "Venezuela presidential election: Kalshi 36%"
semantic_title: "Venezuela holding a presidential election stays near long-shot odds"
telemetry: "Kalshi 36%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-30T00:00:00.000Z"
event_id: "CM-EVT-F1G1G8F7P2"
event_slug: "kxelectvenezuela"
event_question: "When will Venezuela hold a presidential election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXELECTVENEZUELA-27JUN01"
  question_raw: "Will Venezuela hold a presidential election before Jun 1, 2027?"
  current_price: 0.36
  volume_24h_usd: 2.11
  arbitration_model: "kalshi_staff"
  resolution_source: "Fox News"
  resolves_at: "2027-06-01T14:00:00Z"
bullets:
  - "Kalshi puts 36% odds on Venezuela holding a presidential election, pricing the outcome as unlikely despite the new U.S.-Venezuela oil deal."
  - "Trump's diplomatic opening with Caracas is not yet translating into market confidence in democratic transition; the 36% print suggests skepticism about political reform as a deal condition."
  - "A companion Polymarket contract (CM-EVT-M49M1D05V5) puts only 9% on Trump endorsing opposition leader Maria Corina Machado for Venezuelan president, indicating markets do not expect the deal to come with a democratic push."
  - "Kalshi resolves via Fox News confirmation of an election; the contract's below-50% pricing implies markets view the Maduro government retaining power as the base case regardless of the oil agreement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump announced what he called the biggest oil deal in history with Venezuela and pledged it would lower U.S. gas prices, but timing and implementation details remain unclear."
    publisher: "TIME"
    published_at: "2026-08-30T00:00:00.000Z"
    source_url: "https://time.com/article/2026/08/29/trump-says-his-venezuela-oil-deal-will-lower-gas-prices-but-when-/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "TIME"
        source_url: "https://time.com/article/2026/08/29/trump-says-his-venezuela-oil-deal-will-lower-gas-prices-but-when-/"
        retrieved_at: "2026-08-31T15:47:21+00:00"
  - type: "pm_response"
    notes: "Kalshi at 36% on a Venezuelan election resolves via Fox News; the companion Polymarket Machado contract at 9% confirms markets are pricing an oil-for-access deal, not a regime-change deal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "TIME: Trump Promises His Venezuela Oil Deal Will Lower Gas Prices. But When?"
    url: "https://time.com/article/2026/08/29/trump-says-his-venezuela-oil-deal-will-lower-gas-prices-but-when-/"
    published_at: "2026-08-30T00:00:00.000Z"
    retrieved_at: "2026-08-31T15:47:21+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
