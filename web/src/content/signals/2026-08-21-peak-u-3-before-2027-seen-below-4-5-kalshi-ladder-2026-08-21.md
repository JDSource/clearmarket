---
signal_id: "CMSIG2026082103"
signal_slug: "peak-u-3-before-2027-seen-below-4-5-kalshi-ladder-2026-08-21"
headline: "Peak U-3 before 2027 seen below 4.5%: Kalshi ladder"
semantic_title: "Peak unemployment before 2027 stays a long shot above 4.5 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-21T00:00:00.000Z"
event_id: "CM-EVT-RBY62SKLC0"
event_slug: "kxu3max-27"
event_question: "Peak U-3 unemployment before 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3MAX-27-4.5"
  question_raw: "How high will unemployment get before 2027?"
  current_price: 0.26
  volume_24h_usd: 2.7
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-09T15:00:00Z"
bullets:
  - "Kalshi ladder puts only 26% odds on unemployment exceeding 4.5% before 2027; probability collapses further at higher strikes."
  - "The 'functionally unemployed' analysis conflicts with the ladder, which gives only 4-5% to a spike above 6.0%."
  - "The market is not pricing the bearish labor narrative; the distribution is heavily skewed toward the sub-4.5% outcome."
  - "Companion August U-3 ladder (CM-EVT-CN1M891289) implies 4.1-4.2% for the next print, offering a near-term anchor to the longer-horizon view."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "An economic analysis found nearly 25% of U.S. workers are functionally unemployed, arguing the headline 4.1% July rate understates labor-market weakness."
    publisher: "cbsnews.com"
    published_at: "2026-08-21T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/news/functional-unemployment-us-labor-market-analysis/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/functional-unemployment-us-labor-market-analysis/"
        retrieved_at: "2026-08-24T08:42:17+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves on the highest BLS U-3 reading recorded before 2027; resolution source unspecified in data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: Nearly 25% of U.S. workers are \"functionally unemployed,\" economic ana"
    url: "https://www.cbsnews.com/news/functional-unemployment-us-labor-market-analysis/"
    published_at: "2026-08-21T00:00:00.000Z"
    retrieved_at: "2026-08-24T08:42:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
