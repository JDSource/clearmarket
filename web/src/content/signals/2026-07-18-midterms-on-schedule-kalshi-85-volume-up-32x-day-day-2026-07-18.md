---
signal_id: "CMSIG2026071803"
signal_slug: "midterms-on-schedule-kalshi-85-volume-up-32x-day-day-2026-07-18"
headline: "Midterms on schedule: Kalshi 85%; volume up 32x day/day"
semantic_title: "Midterm elections on-schedule consensus holds firm at 85 percent"
telemetry: "Kalshi 85%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-18T00:00:00.000Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.85
  volume_24h_usd: 1079.15
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi contract on midterm elections proceeding on schedule prices at 85%, with trading volume up 3,131% (32.3x) day over day."
  - "Despite Trump administration threats to election officials and claims of broad vulnerabilities, the market still puts only a 15% chance elections are disrupted or delayed."
  - "The volume surge signals the election-interference narrative is pulling fresh attention to this contract, even as the probability itself remains elevated."
  - "Resolves via The Washington Post confirming whether midterm elections are held on their scheduled date."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump and allies escalated attacks on US election security ahead of midterms, with DHS Secretary Mullin threatening funding cuts to non-compliant states."
    publisher: "dnyuz.com"
    published_at: "2026-07-18T00:00:00.000Z"
    source_url: "https://dnyuz.com/2026/07/18/trump-allies-seek-to-sow-mistrust-about-election-security-ahead-of-midterms/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "dnyuz.com"
        source_url: "https://dnyuz.com/2026/07/18/trump-allies-seek-to-sow-mistrust-about-election-security-ahead-of-midterms/"
        retrieved_at: "2026-07-18T09:20:01+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 85% with a 32x volume spike shows heightened engagement from election-threat news, but the market is not moving toward a disruption scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "dnyuz.com: Trump, allies seek to sow mistrust about election security ahead of mi"
    url: "https://dnyuz.com/2026/07/18/trump-allies-seek-to-sow-mistrust-about-election-security-ahead-of-midterms/"
    published_at: "2026-07-18T00:00:00.000Z"
    retrieved_at: "2026-07-18T09:20:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
