---
signal_id: "CMSIG2026061202"
signal_slug: "hormuz-normal-traffic-by-dec-31-polymarket-78-2026-06-12"
headline: "Hormuz normal traffic by Dec 31: Polymarket 78%"
semantic_title: "Hormuz traffic returning to normal by year-end commands wide consensus"
telemetry: "Polymarket 78%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-12T17:31:58.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will traffic through the Strait of Hormuz return to normal by December 31?"
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
  - "Polymarket prices Hormuz traffic returning to normal by December 31 at 78%, reflecting strong but not certain confidence."
  - "Trump's announcement of a signed deal and June 19 reopening date is directionally consistent with the 78% pricing, though market stops well short of certainty."
  - "The near-term companion Polymarket contract on Hormuz normalization by end of June sits at only 18%, flagging deep doubt about the June 19 timeline holding."
  - "Resolution is via IMF PortWatch shipping data; physical transit metrics, not diplomatic announcements, settle the contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump announced the Iran peace deal would be signed Sunday, with the Strait of Hormuz reopening scheduled for June 19."
    publisher: "euronews.com"
    published_at: "2026-06-12T17:31:58.000Z"
    source_url: "https://www.euronews.com/2026/06/12/iran-says-deal-with-us-closer-than-ever-as-trump-warns-tehran-to-get-act-together"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "euronews.com"
        source_url: "https://www.euronews.com/2026/06/12/iran-says-deal-with-us-closer-than-ever-as-trump-warns-tehran-to-get-act-together"
        retrieved_at: "2026-06-15T13:51:44+00:00"
  - type: "pm_response"
    notes: "Polymarket's 78% year-end versus 18% end-of-June gap reveals markets pricing diplomatic announcements as fragile, with normalization seen as a multi-month process."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "euronews.com: US President Donald Trump says Iran peace deal to be signed Sunday | E"
    url: "https://www.euronews.com/2026/06/12/iran-says-deal-with-us-closer-than-ever-as-trump-warns-tehran-to-get-act-together"
    published_at: "2026-06-12T17:31:58.000Z"
    retrieved_at: "2026-06-15T13:51:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
