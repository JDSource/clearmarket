---
signal_id: "CMSIG2026111507"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-4-2026-11-15"
headline: "Hormuz traffic normal by Dec 31: Polymarket 4%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end stays a long shot"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-15T08:28:25.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.04
  volume_24h_usd: 36678.750851
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 prices at just 4%."
  - "The U.S. blockade taking effect today and tankers hitting mines are consistent with a market pricing near-zero chance of normalization within 46 days."
  - "A parallel Kalshi contract (CM-EVT-78FY38Z4R5) on Hormuz normalization by August 30, 2026 also priced at 4%, suggesting the market sees no near-term off-ramp at any horizon so far measured."
  - "Resolves via UMA oracle; 'normal traffic' definition and enforcement duration will be the key settlement ambiguity."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's Revolutionary Guard reported two oil tankers hit mines, and a U.S. blockade of Iranian port traffic in the Strait of Hormuz took effect November 15."
    publisher: "Berk Kutay Gokmen"
    published_at: "2026-11-15T08:28:25.000Z"
    source_url: "https://www.aa.com.tr/en/world/morning-briefing-nov-15-2026/4125489"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Berk Kutay Gokmen"
        source_url: "https://www.aa.com.tr/en/world/morning-briefing-nov-15-2026/4125489"
        retrieved_at: "2026-11-15T07:48:03+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 4%; resolves via UMA oracle; no intraday move claimed."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Berk Kutay Gokmen: Morning Briefing: Nov. 15, 2026"
    url: "https://www.aa.com.tr/en/world/morning-briefing-nov-15-2026/4125489"
    published_at: "2026-11-15T08:28:25.000Z"
    retrieved_at: "2026-11-15T07:48:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
