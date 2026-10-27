---
signal_id: "CMSIG2026102708"
signal_slug: "republican-wins-fl-27-house-seat-kalshi-67-2026-10-27"
headline: "Republican wins FL-27 House seat: Kalshi 67%"
semantic_title: "FL-27 House seat stays near a coin flip as Democrats eye pickup"
telemetry: "Kalshi 67%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-27T00:00:00.000Z"
event_id: "CM-EVT-RTW7ZKGKR3"
event_slug: "kxhouserace-fl27-26"
event_question: "Will the Republican or Democratic candidate win the FL-27 House seat in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL27-26-R"
  question_raw: "Will Republican win the House race for FL-27?"
  current_price: 0.67
  volume_24h_usd: 1141.23
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "The Kalshi prediction market puts 67% odds on the Republican candidate winning the FL-27 House seat, a meaningful but not dominant lead."
  - "Democratic optimism about a congressional sweep is at odds with Kalshi pricing FL-27 at only 67% Republican, making it one of the more competitive seats in the cycle."
  - "The companion Kalshi contract on Democrats winning the full House (CM-EVT-FV8MR86S63) at 91% implies FL-27 is one of the seats keeping the House competitive even in a Democratic wave."
  - "Resolves via the Library of Congress per the named resolution source following certified results after November 3."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Democrats entered the final week of the midterm campaign eyeing a congressional sweep with competitive House seats including Florida's 27th district in focus."
    publisher: "Frankie TAGGART"
    published_at: "2026-10-27T00:00:00.000Z"
    source_url: "https://www.yahoo.com/news/politics/articles/democrats-eye-election-wins-could-014041656.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Frankie TAGGART"
        source_url: "https://www.yahoo.com/news/politics/articles/democrats-eye-election-wins-could-014041656.html"
        retrieved_at: "2026-10-27T13:54:00+00:00"
  - type: "pm_response"
    notes: "Kalshi at 67% flags FL-27 as a genuine swing seat, consistent with its inclusion in Democratic pickup target lists heading into Election Day."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Frankie TAGGART: Democrats eye election wins that could upend Trump presidency"
    url: "https://www.yahoo.com/news/politics/articles/democrats-eye-election-wins-could-014041656.html"
    published_at: "2026-10-27T00:00:00.000Z"
    retrieved_at: "2026-10-27T13:54:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
