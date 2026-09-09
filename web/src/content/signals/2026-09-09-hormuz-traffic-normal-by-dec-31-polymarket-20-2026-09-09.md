---
signal_id: "CMSIG2026090906"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-20-2026-09-09"
headline: "Hormuz traffic normal by Dec 31: Polymarket 20%"
semantic_title: "Strait of Hormuz normal traffic by year-end stays unlikely"
telemetry: "Polymarket 20%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-09T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.2
  volume_24h_usd: 285753.469388
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 20% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Active US-Iran military exchanges, tanker strikes and retaliatory attacks on Jordan, are consistent with this low-normalization pricing."
  - "A companion Polymarket contract (CM-EVT-BR5SMCCW00) puts 11% on Iran withdrawing from the NPT before 2027, signaling broader escalation risk remains priced but not dominant."
  - "Resolution via Polymarket UMA oracle; 'normal' traffic likely requires verified passage of commercial tankers at pre-conflict volumes through the strait."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran attacked US warships and a base in Jordan after the US military destroyed five Iranian oil tankers, deepening the Hormuz impasse."
    publisher: "nbcnews.com"
    published_at: "2026-09-09T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/world/iran/us-strikes-iranian-tankers-attempted-missile-attacks-navy-warship-rcna596699"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nbcnews.com"
        source_url: "https://www.nbcnews.com/world/iran/us-strikes-iranian-tankers-attempted-missile-attacks-navy-warship-rcna596699"
        retrieved_at: "2026-09-09T12:40:02+00:00"
  - type: "pm_response"
    notes: "Polymarket at 20% is the primary normalization pricing reference; cross-referencing the NPT withdrawal contract reveals a market pricing sustained conflict without full escalation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nbcnews.com: Iran attacks American warships and base after U.S. sinks five Iranian"
    url: "https://www.nbcnews.com/world/iran/us-strikes-iranian-tankers-attempted-missile-attacks-navy-warship-rcna596699"
    published_at: "2026-09-09T00:00:00.000Z"
    retrieved_at: "2026-09-09T12:40:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
