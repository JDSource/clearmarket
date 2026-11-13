---
signal_id: "CMSIG2026111307"
signal_slug: "trump-ceases-to-be-president-before-2027-polymarket-2-2026-11-13"
headline: "Trump ceases to be president before 2027: Polymarket 2%"
semantic_title: "Trump leaving office before 2027 stays near certain not to happen"
telemetry: "Polymarket 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-13T05:00:45.000Z"
event_id: "CM-EVT-ZW6ZK09DB1"
event_slug: "trump-out-as-president-before-2027"
event_question: "Will Donald Trump cease to be President before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48b0b0bca515f68fccf95af4793dbd0edbfec1f8ec6e8df2c0f69ba74f8c4722"
  question_raw: "Trump out as President before 2027?"
  current_price: 0.024
  volume_24h_usd: 121935.787237
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Donald Trump ceasing to be president before 2027 sits at 2%, pricing the outcome as a near-impossibility."
  - "Democratic congressional oversight now resumes, including subpoena power over the Justice Department, but the market treats this as insufficient to threaten Trump's tenure before year-end."
  - "The 2% pricing reflects that impeachment, removal, or resignation within roughly six weeks of the settlement date faces near-insurmountable procedural and political barriers even with a new Congress."
  - "Resolution is via UMA oracle and requires Trump to formally leave the presidency for any reason before the 2027 settlement date."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A Democrat-led Congress is set to scrutinize the Justice Department, which has functioned as an extension of the White House under Republican-controlled congressional oversight for nearly two years."
    publisher: "Eric Tucker and Alanna Durkin Richer"
    published_at: "2026-11-13T05:00:45.000Z"
    source_url: "https://apnews.com/article/justice-department-congress-fbi-trump-e121c4420d0010b9ba7e8003407d304a"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Eric Tucker and Alanna Durkin Richer"
        source_url: "https://apnews.com/article/justice-department-congress-fbi-trump-e121c4420d0010b9ba7e8003407d304a"
        retrieved_at: "2026-11-13T07:47:48+00:00"
  - type: "pm_response"
    notes: "Polymarket at 2% via UMA oracle; pricing unchanged by midterm Democratic gains per current data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Eric Tucker and Alanna Durkin Richer: Trump's Justice Department faces a new era of scrutiny under a Democra"
    url: "https://apnews.com/article/justice-department-congress-fbi-trump-e121c4420d0010b9ba7e8003407d304a"
    published_at: "2026-11-13T05:00:45.000Z"
    retrieved_at: "2026-11-13T07:47:48+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
