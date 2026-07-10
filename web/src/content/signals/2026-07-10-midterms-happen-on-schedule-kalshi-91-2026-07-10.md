---
signal_id: "CMSIG2026071003"
signal_slug: "midterms-happen-on-schedule-kalshi-91-2026-07-10"
headline: "Midterms happen on schedule: Kalshi 91%"
semantic_title: "Midterm elections on-schedule consensus holds firm"
telemetry: "Kalshi 91%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-10T02:15:30.000Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.91
  volume_24h_usd: 1228.43
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "The Kalshi prediction market puts 91% on midterm elections proceeding on schedule, resolving via The Washington Post."
  - "Trump's firing of EAC members is a significant institutional disruption, yet the Kalshi contract prices only a 9% chance elections are delayed or cancelled."
  - "A companion Kalshi contract on proof-of-citizenship requirements for federal voter registration sits at just 12%, suggesting markets see procedural pressure but not structural collapse."
  - "Resolution depends on The Washington Post confirming elections occur on the legally scheduled date; court challenges to the EAC firings could be a key wildcard before settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "President Trump fired all remaining members of the U.S. Election Assistance Commission, disabling the only federal agency solely devoted to election administration ahead of the midterms."
    publisher: "channelnewsasia.com"
    published_at: "2026-07-10T02:15:30.000Z"
    source_url: "https://www.channelnewsasia.com/world/trump-us-midterm-election-fires-election-assistance-commission-6245366"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "channelnewsasia.com"
        source_url: "https://www.channelnewsasia.com/world/trump-us-midterm-election-fires-election-assistance-commission-6245366"
        retrieved_at: "2026-07-10T10:49:37+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via The Washington Post; the 91% price implies markets are absorbing the EAC news as a governance stress, not an existential threat to the election calendar."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "channelnewsasia.com: Trump fires Election Assistance Commission members ahead of midterms -"
    url: "https://www.channelnewsasia.com/world/trump-us-midterm-election-fires-election-assistance-commission-6245366"
    published_at: "2026-07-10T02:15:30.000Z"
    retrieved_at: "2026-07-10T10:49:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
