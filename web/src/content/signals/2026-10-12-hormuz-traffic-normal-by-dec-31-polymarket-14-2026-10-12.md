---
signal_id: "CMSIG2026101208"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-14-2026-10-12"
headline: "Hormuz traffic normal by Dec 31: Polymarket 14%"
semantic_title: "Strait of Hormuz returning to normal by year-end stays unlikely"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-12T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.14
  volume_24h_usd: 109187.801766
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 14% on Strait of Hormuz traffic returning to normal by December 31, reflecting low confidence in a near-term Iran de-escalation."
  - "Tehran's rejection of the US proposal and its escalation threat are consistent with the market's skeptical 14% pricing on normalization."
  - "Parallel Switzerland talks between Vice President JD Vance and Foreign Minister Abbas Araghchi represent a competing diplomatic signal, but the Polymarket contract is not pricing that path as likely."
  - "A companion Kalshi contract on the US recognizing Reza Pahlavi as Iran's leader sits at 4%, confirming markets see no rapid resolution of the underlying conflict."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran rejected a US proposal to end the Iran-US war and threatened major escalation, including strikes on regional data centers and cables."
    publisher: "Debjit Sinha"
    published_at: "2026-10-12T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/news/international/us/iran-us-war-tehran-rejects-donald-trump-administrations-proposal-to-end-war-threatens-major-escalation-by-striking-regional-data-center-cables/articleshow/134880148.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Debjit Sinha"
        source_url: "https://economictimes.indiatimes.com/news/international/us/iran-us-war-tehran-rejects-donald-trump-administrations-proposal-to-end-war-threatens-major-escalation-by-striking-regional-data-center-cables/articleshow/134880148.cms"
        retrieved_at: "2026-10-12T07:49:04+00:00"
  - type: "pm_response"
    notes: "The Polymarket Hormuz contract resolves via uma_oracle based on verified shipping data; Iran's escalation threats make the 14% pricing consistent with reported conditions."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Debjit Sinha: Iran-US War: Tehran rejects Donald Trump administration's proposal to"
    url: "https://economictimes.indiatimes.com/news/international/us/iran-us-war-tehran-rejects-donald-trump-administrations-proposal-to-end-war-threatens-major-escalation-by-striking-regional-data-center-cables/articleshow/134880148.cms"
    published_at: "2026-10-12T00:00:00.000Z"
    retrieved_at: "2026-10-12T07:49:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
