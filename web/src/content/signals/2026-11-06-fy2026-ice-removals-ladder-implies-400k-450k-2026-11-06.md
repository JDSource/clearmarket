---
signal_id: "CMSIG2026110604"
signal_slug: "fy2026-ice-removals-ladder-implies-400k-450k-2026-11-06"
headline: "FY2026 ICE removals: ladder implies 400K-450K"
semantic_title: "ICE removals in FY2026 seen landing in 400K-450K range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-06T18:57:33.000Z"
event_id: "CM-EVT-F0MWBBP842"
event_slug: "kxdeportations-27jan01"
event_question: "FY2026 ICE removals total"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXDEPORTATIONS-27JAN01-T450000"
  question_raw: "Will the number of ICE removals be above 450000 in FY2026?"
  current_price: 0.46
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "the Statistical Review of World Energy"
  resolves_at: "2027-04-01T15:00:00Z"
bullets:
  - "Ladder puts 94% odds on removals exceeding 400,000 but only 46% on exceeding 450,000, implying the market consensus centers in the 400K-450K band."
  - "Miller's promotion as the architect of the administration's immigration crackdown is consistent with market pricing for a high but not record-breaking removal total."
  - "The sharp drop from 94% at 400K to 46% at 450K shows meaningful uncertainty about whether enforcement intensity will push into the upper range."
  - "Resolves via official ICE/DHS FY2026 removal statistics; fiscal year timing and reporting lag could affect settlement date."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump elevated Stephen Miller to chief of staff, signaling a doubling down on immigration enforcement policies that voters rejected in the midterms."
    publisher: "Maggie Haberman, Jonathan Swan, Tyler Pager, Chris Cameron, Karen Yourish"
    published_at: "2026-11-06T18:57:33.000Z"
    source_url: "https://www.nytimes.com/live/2026/11/06/us/trump-miller-wiles-chief-of-staff"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Maggie Haberman, Jonathan Swan, Tyler Pager, Chris Cameron, Karen Yourish"
        source_url: "https://www.nytimes.com/live/2026/11/06/us/trump-miller-wiles-chief-of-staff"
        retrieved_at: "2026-11-08T07:47:56+00:00"
  - type: "pm_response"
    notes: "Ladder data implies consensus around 400K-450K ICE removals for FY2026, pricing significant enforcement activity without certainty of an extreme outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Maggie Haberman, Jonathan Swan, Tyler Pager, Chris Cameron, Karen Yourish: Trump Elevates Stephen Miller, a Fiery Hard-Liner, to Chief of Staff"
    url: "https://www.nytimes.com/live/2026/11/06/us/trump-miller-wiles-chief-of-staff"
    published_at: "2026-11-06T18:57:33.000Z"
    retrieved_at: "2026-11-08T07:47:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
