---
signal_id: "CMSIG2026082308"
signal_slug: "kansas-senate-seat-republican-win-kalshi-81-2026-08-23"
headline: "Kansas Senate seat Republican win: Kalshi 81%"
semantic_title: "Kansas Senate seat stays heavily favored for Republicans"
telemetry: "Kalshi 81%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-23T08:41:09.387Z"
event_id: "CM-EVT-S6Y29BSL46"
event_slug: "senateks-26"
event_question: "Will the Kansas Senate seat be won by the Republican candidate in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEKS-26-R"
  question_raw: "Will Republicans win the Senate race in Kansas?"
  current_price: 0.81
  volume_24h_usd: 174.88
  arbitration_model: "kalshi_staff"
  resolution_source: "United States Congress"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi puts 81% on the Republican candidate winning the Kansas Senate seat, resolves via the United States Congress."
  - "The Democratic Senate-majority narrative is not reflected in Kansas; the market firmly prices it as a Republican hold."
  - "The New Mexico Senate seat Kalshi contract (CM-EVT-ZD0C3KWW30) sits at 98% for Republicans, anchoring the upper bound of safe GOP territory."
  - "The Democratic leader internal dynamics Kalshi contract (CM-EVT-W0LJLH97L8) at 20% suggests limited internal pressure on Senate Democratic leadership despite midterm uncertainty."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Democrats are pursuing a path to recapture the Senate in the 2026 midterms, relying on competitive races across several states."
    publisher: "Ken Thomas in Washington and Siobhan Hughes in Mitchell, S.D."
    published_at: "2026-08-23T08:41:09.387Z"
    source_url: "https://www.wsj.com/politics/policy/democrats-senate-midterm-election-odds-9844b4aa"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ken Thomas in Washington and Siobhan Hughes in Mitchell, S.D."
        source_url: "https://www.wsj.com/politics/policy/democrats-senate-midterm-election-odds-9844b4aa"
        retrieved_at: "2026-08-24T08:42:17+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via the United States Congress on the certified winner of the Kansas Senate general election."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ken Thomas in Washington and Siobhan Hughes in Mitchell, S.D.: Why Democrats Still Have a Shot at Winning the Senate"
    url: "https://www.wsj.com/politics/policy/democrats-senate-midterm-election-odds-9844b4aa"
    published_at: "2026-08-23T08:41:09.387Z"
    retrieved_at: "2026-08-24T08:42:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
