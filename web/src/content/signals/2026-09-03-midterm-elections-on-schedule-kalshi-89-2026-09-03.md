---
signal_id: "CMSIG2026090307"
signal_slug: "midterm-elections-on-schedule-kalshi-89-2026-09-03"
headline: "Midterm elections on schedule: Kalshi 89%"
semantic_title: "Midterm elections on schedule holds near 90 percent"
telemetry: "Kalshi 89%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-03T19:27:06.638Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.89
  volume_24h_usd: 492.54
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi prices an 89% probability that the midterm elections happen on schedule, despite mounting logistical and legal turmoil over mail voting rules."
  - "Election officials' warnings of implementation impossibility and a federal court block on USPS mail rules do not appear to have shifted the market's strong base case for on-schedule elections."
  - "A separate Kalshi contract (CM-EVT-T5VXKJT451) puts only 48% on Republicans controlling at least one chamber after the midterms, reflecting a competitive election environment within the on-schedule baseline."
  - "Kalshi contract resolves via The Washington Post's official call on whether midterm elections occur as scheduled; a court-ordered postponement would be the key resolution trigger."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Election officials warned that implementing new Trump administration mail voting rules weeks before the November midterms would be 'virtually impossible,' as federal courts extended a block on the postal regulations."
    publisher: "CBS News"
    published_at: "2026-09-03T19:27:06.638Z"
    source_url: "https://www.cbsnews.com/news/mail-voting-rules-usps-election-officials-midterms/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "CBS News"
        source_url: "https://www.cbsnews.com/news/mail-voting-rules-usps-election-officials-midterms/"
        retrieved_at: "2026-09-04T12:28:22+00:00"
  - type: "pm_response"
    notes: "Kalshi hosts this on-schedule elections contract; the 89% read implies the market treats legal disruption to the timeline itself as a low-probability outcome despite the mail voting chaos."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "CBS News: Election officials raise alarm over implementing new mail voting rules"
    url: "https://www.cbsnews.com/news/mail-voting-rules-usps-election-officials-midterms/"
    published_at: "2026-09-03T19:27:06.638Z"
    retrieved_at: "2026-09-04T12:28:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
