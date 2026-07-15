---
signal_id: "CMSIG2026071407"
signal_slug: "new-house-winner-sc-6-by-deadline-kalshi-92-2026-07-14"
headline: "New House winner SC-6 by deadline: Kalshi 92%"
semantic_title: "South Carolina 6th District new House winner nears full pricing"
telemetry: "Kalshi 92%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-14T18:40:37.000Z"
event_id: "CM-EVT-HT8B6GN884"
event_slug: "kxhouserace-sc06-26"
event_question: "Will a new House winner be elected in South Carolina's 6th Congressional District by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-SC06-26-D"
  question_raw: "Will Democratic win the House race for SC-06?"
  current_price: 0.923
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a new House winner being elected in South Carolina's 6th Congressional District at 92%."
  - "Darline Graham Nordone's Senate swearing-in confirms the vacancy, making an election procedurally necessary and consistent with 92% pricing."
  - "The 8% residual likely reflects uncertainty around timeline rather than whether an election will occur at all."
  - "Resolves via Library of Congress; a certified election result by the stated deadline is the settlement trigger."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Darline Graham Nordone was sworn in as US senator replacing her late brother Lindsey Graham, vacating South Carolina's 6th Congressional District seat."
    publisher: "usatoday.com"
    published_at: "2026-07-14T18:40:37.000Z"
    source_url: "https://www.usatoday.com/story/news/politics/elections/2026/07/14/darline-graham-nordone-swearing-in-south-carolina-senate-lindsey/90916631007/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "usatoday.com"
        source_url: "https://www.usatoday.com/story/news/politics/elections/2026/07/14/darline-graham-nordone-swearing-in-south-carolina-senate-lindsey/90916631007/"
        retrieved_at: "2026-07-15T10:00:10+00:00"
  - type: "pm_response"
    notes: "Kalshi at 92% is consistent with the vacancy now being formally confirmed; resolution depends on the Library of Congress certification."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "usatoday.com: Sen. Darline Graham Nordone sworn in, replacing late brother Lindsey"
    url: "https://www.usatoday.com/story/news/politics/elections/2026/07/14/darline-graham-nordone-swearing-in-south-carolina-senate-lindsey/90916631007/"
    published_at: "2026-07-14T18:40:37.000Z"
    retrieved_at: "2026-07-15T10:00:10+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
