---
signal_id: "CMSIG2026092807"
signal_slug: "hormuz-traffic-back-to-normal-by-dec-31-polymarket-20-2026-09-28"
headline: "Hormuz traffic back to normal by Dec 31: Polymarket 20%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end stays at 20%"
telemetry: "Polymarket 20%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-28T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.2
  volume_24h_usd: 65924.281228
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 20% odds on Strait of Hormuz traffic returning to normal by December 31, keeping the outcome a long shot."
  - "Trump's rejection of Iran's latest proposal is consistent with this low probability; ongoing mediation has not moved the market toward a resolution."
  - "A related Kalshi contract (CM-EVT-34SYT4T2T1) puts just 2% on the U.S. reopening its embassy in Iran, underscoring the market's skepticism across diplomatic milestones."
  - "Resolution via Polymarket's UMA oracle; the December 31 deadline makes any late-stage deal extremely time-constrained given the current impasse."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Mediators continued brokering a U.S.-Iran deal even after Trump rejected Tehran's latest proposal, with talks ongoing through Qatari intermediaries."
    publisher: "Samy Magdy and Matthew Lee         Sept. 28, 2026  8:33 AM PT"
    published_at: "2026-09-28T00:00:00.000Z"
    source_url: "https://www.latimes.com/world-nation/story/2026-09-28/mediators-working-to-broker-u-s-iran-deal-even-after-trump-rejected-latest-tehran-proposal"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Samy Magdy and Matthew Lee         Sept. 28, 2026  8:33 AM PT"
        source_url: "https://www.latimes.com/world-nation/story/2026-09-28/mediators-working-to-broker-u-s-iran-deal-even-after-trump-rejected-latest-tehran-proposal"
        retrieved_at: "2026-10-01T07:47:27+00:00"
  - type: "pm_response"
    notes: "Polymarket holds Hormuz normalization at 20% with Iran talks stalled; the 2% embassy contract on Kalshi reinforces the broad diplomatic pessimism across venues."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Samy Magdy and Matthew Lee         Sept. 28, 2026  8:33 AM PT: Mediators working to broker U.S.-Iran deal even after Trump rejected l"
    url: "https://www.latimes.com/world-nation/story/2026-09-28/mediators-working-to-broker-u-s-iran-deal-even-after-trump-rejected-latest-tehran-proposal"
    published_at: "2026-09-28T00:00:00.000Z"
    retrieved_at: "2026-10-01T07:47:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
