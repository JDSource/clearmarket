---
signal_id: "CMSIG2026091705"
signal_slug: "democrats-win-us-house-next-election-kalshi-89-2026-09-17"
headline: "Democrats win US House next election: Kalshi 89%"
semantic_title: "Democrats winning the House next election stays near 90 percent"
telemetry: "Kalshi 89%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-17T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.89
  volume_24h_usd: 169306.17
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi contract on Democrats winning the US House in the next election prices at 89%."
  - "The Supreme Court's decision to preserve mail-in ballot access is consistent with the market's strong Democratic lean heading into the midterms."
  - "A related Kalshi contract on the Clarity Act companion event CM-EVT-8NWCS8ZRW8 has no price, limiting cross-market reads on the legal landscape."
  - "The Kalshi contract resolves via the Library of Congress; official certification of House seat tallies is the settlement trigger."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Supreme Court blocked Trump's attempt to restrict mail-in ballots ahead of the 2026 midterms."
    publisher: "independent.co.uk"
    published_at: "2026-09-17T00:00:00.000Z"
    source_url: "https://www.independent.co.uk/news/world/americas/us-politics/trump-midterm-elections-mail-in-ballot-b3051433.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "independent.co.uk"
        source_url: "https://www.independent.co.uk/news/world/americas/us-politics/trump-midterm-elections-mail-in-ballot-b3051433.html"
        retrieved_at: "2026-09-17T13:04:18+00:00"
  - type: "pm_response"
    notes: "Kalshi at 89% resolves via Library of Congress; the SCOTUS mail-ballot ruling aligns with the market's heavily Democratic positioning."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "independent.co.uk: Trump failed to block mail-in ballots ahead of the midterms. What happ"
    url: "https://www.independent.co.uk/news/world/americas/us-politics/trump-midterm-elections-mail-in-ballot-b3051433.html"
    published_at: "2026-09-17T00:00:00.000Z"
    retrieved_at: "2026-09-17T13:04:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
