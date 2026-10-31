---
signal_id: "CMSIG2026103003"
signal_slug: "core-cpi-annual-rate-seen-at-2-8-2-9-kalshi-ladder-2026-10-30"
headline: "Core CPI annual rate seen at 2.8-2.9%: Kalshi ladder"
semantic_title: "Core CPI for 2026 seen settling near 2.8 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-30T09:00:00.000Z"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Core CPI year-over-year rate for year ending 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.9"
  question_raw: "Will the rate of core CPI inflation be above 2.9% for the year ending in November 2026?"
  current_price: 0.24
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "Kalshi ladder implies a core CPI year-over-year rate near 2.8-2.9%, with 60% pricing above 2.8% but only 24% above 2.9%."
  - "News coverage flags inflation running above 2% as a political headwind for midterms; the ladder's distribution is consistent with that narrative."
  - "The sharp drop from 60% above 2.8% to 24% above 2.9% shows the market sees limited upside risk beyond the current run rate."
  - "Resolution is via the named BLS core CPI print; the ladder collapses quickly above 3.0% (only 16%), suggesting the market does not price a re-acceleration."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Pre-midterm economic coverage highlights persistent inflation above the Fed's 2% target alongside continued GDP growth."
    publisher: "Max Zahn"
    published_at: "2026-10-30T09:00:00.000Z"
    source_url: "https://abcnews.com/Business/us-economy-midterm-elections/story?id=137478975"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Max Zahn"
        source_url: "https://abcnews.com/Business/us-economy-midterm-elections/story?id=137478975"
        retrieved_at: "2026-10-31T07:48:23+00:00"
  - type: "pm_response"
    notes: "Kalshi's core CPI ladder reflects a market consensus clustered around 2.8-2.9% for the full year, with tails sharply discounted on either side."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Max Zahn: What to know about the US economy as midterm elections near"
    url: "https://abcnews.com/Business/us-economy-midterm-elections/story?id=137478975"
    published_at: "2026-10-30T09:00:00.000Z"
    retrieved_at: "2026-10-31T07:48:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
