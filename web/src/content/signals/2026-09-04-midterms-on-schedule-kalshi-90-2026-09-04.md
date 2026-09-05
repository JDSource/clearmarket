---
signal_id: "CMSIG2026090404"
signal_slug: "midterms-on-schedule-kalshi-90-2026-09-04"
headline: "Midterms on schedule: Kalshi 90%"
semantic_title: "Midterm elections happening on schedule stays near certain"
telemetry: "Kalshi 90%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-04T00:00:00.000Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.9
  volume_24h_usd: 1645.66
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi prices 90% odds that the midterm elections happen on schedule, per The Washington Post as resolution source."
  - "North Carolina ballot distribution and ongoing court blocks on Trump mail-voting restrictions are consistent with elections proceeding; the market is not pricing meaningful disruption."
  - "Companion Kalshi contract (CM-EVT-T5VXKJT451) puts 48% on Republicans controlling at least one chamber after the midterms, near coin-flip odds for overall control."
  - "The on-schedule contract resolves via The Washington Post; a Supreme Court intervention altering the election timeline would be the key upset scenario."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "North Carolina began distributing mail-voting ballots, formally launching the 2026 US midterms as the Trump administration fights mail-ballot restrictions in court."
    publisher: "france24.com"
    published_at: "2026-09-04T00:00:00.000Z"
    source_url: "https://www.france24.com/en/americas/20260904-us-midterms-begin-with-chaos-over-mail-voting-crackdown"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "france24.com"
        source_url: "https://www.france24.com/en/americas/20260904-us-midterms-begin-with-chaos-over-mail-voting-crackdown"
        retrieved_at: "2026-09-05T11:34:19+00:00"
  - type: "pm_response"
    notes: "Kalshi at 90% on schedule reflects court battles being absorbed without the market pricing significant timeline risk."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "france24.com: US midterms start with North Carolina distributing mail-voting ballots"
    url: "https://www.france24.com/en/americas/20260904-us-midterms-begin-with-chaos-over-mail-voting-crackdown"
    published_at: "2026-09-04T00:00:00.000Z"
    retrieved_at: "2026-09-05T11:34:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
