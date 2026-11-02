---
signal_id: "CMSIG2026110106"
signal_slug: "senate-control-2026-polymarket-73-2026-11-01"
headline: "Senate control 2026: Polymarket 73%"
semantic_title: "Senate control odds lean toward one party but stay near 75 percent"
telemetry: "Polymarket 73%"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-11-01T20:35:48.000Z"
event_id: "CM-EVT-M9WJY06T90"
event_slug: "which-party-will-win-the-senate-in-2026"
event_question: "Which party will win control of the U.S. Senate in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x307a1ed89d60b61002dd5bbf00e1408c5ed2ab3fcdb056191ca7ef9bc34d38f3"
  question_raw: "Will the Democratic Party control the Senate after the 2026 Midterm elections?"
  current_price: 0.73
  volume_24h_usd: 855823.8760830001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Senate control for one party at 73%, reflecting genuine uncertainty as Trump campaigns for vulnerable seats."
  - "The Michigan Senate race (Rogers vs. El-Sayed) is described as tight in news coverage; the Kalshi contract (CM-EVT-5BB4SFW2V1) puts 77% on Michigan electing a governor and senator from the same party, suggesting market alignment with Democratic strength."
  - "The companion Democrats-win-all-four-core-Senate-races Polymarket contract (CM-EVT-P54SDG6NP7) at 69% implies Democrats are favored in the core contested set, even as overall Senate control remains uncertain."
  - "Polymarket resolves via uma_oracle after official results; last-minute candidate crossovers (Michigan Democrat Haley Stevens endorsed Republican Mike Rogers per news) add resolution risk if results are contested."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump is rallying for embattled Senate seats in the final days before the midterms, with Senate control hanging on a handful of competitive races."
    publisher: "Elissa Fitzgerald"
    published_at: "2026-11-01T20:35:48.000Z"
    source_url: "https://www.abc.net.au/news/2026-11-02/us-midterms-daily-news-briefing-trump-alaska-michigan/107326672"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Elissa Fitzgerald"
        source_url: "https://www.abc.net.au/news/2026-11-02/us-midterms-daily-news-briefing-trump-alaska-michigan/107326672"
        retrieved_at: "2026-11-02T07:48:26+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; the 73% reading reflects a Senate outcome that remains meaningfully contested even as House odds are far more settled."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Elissa Fitzgerald: US midterms briefing: Trump rallies for embattled Senate seats after H"
    url: "https://www.abc.net.au/news/2026-11-02/us-midterms-daily-news-briefing-trump-alaska-michigan/107326672"
    published_at: "2026-11-01T20:35:48.000Z"
    retrieved_at: "2026-11-02T07:48:26+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
