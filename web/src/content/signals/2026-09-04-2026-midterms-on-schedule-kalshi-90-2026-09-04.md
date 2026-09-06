---
signal_id: "CMSIG2026090406"
signal_slug: "2026-midterms-on-schedule-kalshi-90-2026-09-04"
headline: "2026 midterms on schedule: Kalshi 90%"
semantic_title: "Midterm elections on schedule stays heavily favored at 90%"
telemetry: "Kalshi 90%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-04T11:53:10.540Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.9
  volume_24h_usd: 1219.37
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi prices 90% on the midterm elections happening on schedule, resolving via The Washington Post."
  - "Despite active litigation over mail-ballot rules and a Supreme Court appeal, prediction markets strongly dismiss the risk of the elections being delayed or cancelled."
  - "The mail-voting dispute is about ballot rules, not the election date itself; the market's 90% is consistent with courts blocking rules without blocking the election."
  - "Companion contract on SCOTUS barring post-Election-Day mail ballot counting (CM-EVT-8NWCS8ZRW8) has no live price, leaving the downstream ballot-counting risk unquantified."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump has asked the Supreme Court to lift a block on a USPS plan restricting mail-in voting, with a federal judge warning the rules could cause major disenfranchisement."
    publisher: "Hansi Lo Wang"
    published_at: "2026-09-04T11:53:10.540Z"
    source_url: "https://www.npr.org/2026/09/03/nx-s1-5955614/trump-mail-in-voting-ruling-court-usps"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Hansi Lo Wang"
        source_url: "https://www.npr.org/2026/09/03/nx-s1-5955614/trump-mail-in-voting-ruling-court-usps"
        retrieved_at: "2026-09-06T11:54:11+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via The Washington Post confirming elections occurred on the scheduled November 2026 date."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Hansi Lo Wang: What to know about the mail-in voting fight at the Supreme Court"
    url: "https://www.npr.org/2026/09/03/nx-s1-5955614/trump-mail-in-voting-ruling-court-usps"
    published_at: "2026-09-04T11:53:10.540Z"
    retrieved_at: "2026-09-06T11:54:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
