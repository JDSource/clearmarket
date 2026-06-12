---
signal_id: "CMSIG2026061206"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-31-2026-06-12"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 31%"
semantic_title: "Ukraine-Russia peace deal before 2027 holds below majority at 31 percent"
telemetry: "Polymarket 31%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-12T00:08:52.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.31
  volume_24h_usd: 168160.203144
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 31% on Ukraine signing a peace deal with Russia before 2027, even as Kyiv pursues a deliberate pressure campaign."
  - "Ukrainian drone strikes on Russian refineries and industrial sites reflect an escalation strategy, which the market reads as prolonging rather than shortening the conflict timeline."
  - "The June 30 peace deal contract (CM-EVT-CM-EVT-91B1JBJW33) sits at just 4%, placing the full year-end probability at 31% against a near-zero near-term probability."
  - "Resolves via UMA oracle; a signed ceasefire or peace agreement between Ukraine and Russia must be publicly confirmed before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukraine is running a campaign of drone strikes on Russian infrastructure to pressure Putin toward negotiations by fall 2026, targeting his willingness to come to the table."
    publisher: "meduza.io"
    published_at: "2026-06-12T00:08:52.000Z"
    source_url: "https://meduza.io/amp/en/feature/2026/06/12/inside-ukraine-s-campaign-to-force-putin-to-the-negotiating-table-by-fall-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "meduza.io"
        source_url: "https://meduza.io/amp/en/feature/2026/06/12/inside-ukraine-s-campaign-to-force-putin-to-the-negotiating-table-by-fall-2026"
        retrieved_at: "2026-06-12T11:42:07+00:00"
  - type: "pm_response"
    notes: "Polymarket's 31% year-end versus 4% June 30 split shows the market sees a possible deal window only in the second half of 2026, consistent with Kyiv's stated fall-2026 pressure timeline."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "meduza.io: Inside Ukraine’s campaign to force Putin to the negotiating table by f"
    url: "https://meduza.io/amp/en/feature/2026/06/12/inside-ukraine-s-campaign-to-force-putin-to-the-negotiating-table-by-fall-2026"
    published_at: "2026-06-12T00:08:52.000Z"
    retrieved_at: "2026-06-12T11:42:07+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
