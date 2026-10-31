---
signal_id: "CMSIG2026103106"
signal_slug: "kansas-senate-seat-for-republicans-kalshi-49-2026-10-31"
headline: "Kansas Senate seat for Republicans: Kalshi 49%"
semantic_title: "Kansas Senate race stays near a coin flip"
telemetry: "Kalshi 49%"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-10-31T00:00:00.000Z"
event_id: "CM-EVT-S6Y29BSL46"
event_slug: "senateks-26"
event_question: "Will the Kansas Senate seat be won by the Republican candidate in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEKS-26-R"
  question_raw: "Will Republicans win the Senate race in Kansas?"
  current_price: 0.49
  volume_24h_usd: 339914.8
  arbitration_model: "kalshi_staff"
  resolution_source: "United States Congress"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "The Kalshi contract on the Republican candidate winning the Kansas Senate seat sits at 49%, effectively a coin flip."
  - "Justice Department subpoenas in multiple states and Trump's final-weekend rally schedule in Kansas signal both parties view this race as genuinely competitive."
  - "A Republican Kansas loss would significantly complicate GOP Senate retention; the 49% pricing reflects that binary uncertainty days before polls close."
  - "Resolves via the United States Congress; the Alaska Senate contract (CM-EVT-KQWMXB6NX7) at 31% for a new senator shows another competitive seat, adding to Senate math complexity."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The U.S. midterm campaign enters its final weekend with competitive Senate races, including Kansas, shaping which party controls the upper chamber."
    publisher: "yahoo.com"
    published_at: "2026-10-31T00:00:00.000Z"
    source_url: "https://www.yahoo.com/news/politics/articles/us-campaign-control-congress-enters-100758118.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "yahoo.com"
        source_url: "https://www.yahoo.com/news/politics/articles/us-campaign-control-congress-enters-100758118.html"
        retrieved_at: "2026-10-31T14:15:55+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via the United States Congress; the near-50% price is one of the tightest Senate race readings in the current market suite."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "yahoo.com: US campaign for control of Congress enters final weekend"
    url: "https://www.yahoo.com/news/politics/articles/us-campaign-control-congress-enters-100758118.html"
    published_at: "2026-10-31T00:00:00.000Z"
    retrieved_at: "2026-10-31T14:15:55+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
