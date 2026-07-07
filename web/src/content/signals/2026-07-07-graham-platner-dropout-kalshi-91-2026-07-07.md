---
signal_id: "CMSIG2026070704"
signal_slug: "graham-platner-dropout-kalshi-91-2026-07-07"
headline: "Graham Platner dropout: Kalshi 91%"
semantic_title: "Platner dropout consensus hardens after assault allegation"
telemetry: "Kalshi 91%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-07T00:00:00.000Z"
event_id: "CM-EVT-5YRQP7DDC2"
event_slug: "kxplatnerdropout-26"
event_question: "Will Graham Platner drop out?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPLATNERDROPOUT-26"
  question_raw: "Will Graham Platner drop out of the 2026 United States Senate election in Maine before Jul 14, 2026?"
  current_price: 0.906
  volume_24h_usd: 1932612.07
  arbitration_model: "kalshi_staff"
  resolution_source: "Fox News"
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi prediction market prices a 91% probability that Graham Platner drops out of the Maine Democratic Senate race."
  - "The allegation and rapid endorsement withdrawals are consistent with the near-consensus dropout pricing on Kalshi."
  - "The Maine Senate seat is considered a must-win for Democrats in the 2026 cycle, making candidate instability a material party-level risk."
  - "Kalshi resolves via Fox News reporting on Platner's withdrawal; a formal suspension or exit statement is the settlement trigger, not polling or primary results."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A sexual assault allegation against Maine Democratic Senate candidate Graham Platner prompted prominent supporters to pull endorsements, threatening a must-win Democratic race."
    publisher: "KIMBERLEE KRUESI and NICHOLAS RICCARDI Associated Press"
    published_at: "2026-07-07T00:00:00.000Z"
    source_url: "https://lite.aol.com/news/world/story/0001/20260707/061e18bdd180928bbcd94b18a52f4ec9"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "KIMBERLEE KRUESI and NICHOLAS RICCARDI Associated Press"
        source_url: "https://lite.aol.com/news/world/story/0001/20260707/061e18bdd180928bbcd94b18a52f4ec9"
        retrieved_at: "2026-07-07T10:52:00+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Fox News confirmation of Platner's dropout; at 91% the market has near-fully priced a withdrawal following the Politico report."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "KIMBERLEE KRUESI and NICHOLAS RICCARDI Associated Press: Democrats begin pulling Platner endorsements after Maine candidate fac"
    url: "https://lite.aol.com/news/world/story/0001/20260707/061e18bdd180928bbcd94b18a52f4ec9"
    published_at: "2026-07-07T00:00:00.000Z"
    retrieved_at: "2026-07-07T10:52:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
