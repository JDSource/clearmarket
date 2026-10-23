---
signal_id: "CMSIG2026102303"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-10-23"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound stays near 4 to 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-23T10:05:57.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound following October 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.11
  volume_24h_usd: 65.66
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder implies the Fed funds upper bound at 4.0-4.25% after this week's meeting, with 74% above 4.0% but only 11% above 4.25%."
  - "Hot September inflation raised hike talk, but the market assigns only 11% odds to an upper bound above 4.25%, suggesting the news is not fully priced."
  - "A companion Kalshi ladder for a later meeting (CM-EVT-6BS28TS762) shows 99% above 3.75% but just 7% above 4.0%, implying the market expects rates to drift lower over time."
  - "Resolves via the official Federal Reserve statement; any dissent or guidance language shift could reprice near-term expectations rapidly."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Investors face a Federal Reserve meeting this week, with hot September inflation data rekindling rate-hike expectations and major AI earnings in focus."
    publisher: "investing.com"
    published_at: "2026-10-23T10:05:57.000Z"
    source_url: "https://www.investing.com/news/economy-news/earnings-flood-fed-meeting-pose-pivotal-tests-for-rickety-ai-market-rally-4968724"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/news/economy-news/earnings-flood-fed-meeting-pose-pivotal-tests-for-rickety-ai-market-rally-4968724"
        retrieved_at: "2026-10-23T13:03:13+00:00"
  - type: "pm_response"
    notes: "Kalshi ladders across two meeting horizons point to a peak near 4.0-4.25%, with later-dated odds already pricing a modest downward glide."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Earnings flood, Fed meeting pose pivotal tests for rickety AI market r"
    url: "https://www.investing.com/news/economy-news/earnings-flood-fed-meeting-pose-pivotal-tests-for-rickety-ai-market-rally-4968724"
    published_at: "2026-10-23T10:05:57.000Z"
    retrieved_at: "2026-10-23T13:03:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
