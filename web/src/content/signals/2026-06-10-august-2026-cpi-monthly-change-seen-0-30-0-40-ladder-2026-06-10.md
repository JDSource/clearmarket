---
signal_id: "CMSIG2026061003"
signal_slug: "august-2026-cpi-monthly-change-seen-0-30-0-40-ladder-2026-06-10"
headline: "August 2026 CPI monthly change seen 0.30-0.40%: ladder"
semantic_title: "August CPI momentum wavers around the 0.3 to 0.4 percent band"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-10T00:00:00.000Z"
event_id: "CM-EVT-D057W6W251"
event_slug: "kxcpi-26aug"
event_question: "August 2026 CPI monthly change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26AUG-T0.4"
  question_raw: "Will CPI rise more than 0.4% in August 2026?"
  current_price: 0.45
  volume_24h_usd: 0.45
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-09-11T13:56:00Z"
bullets:
  - "CPI ladder implies August 2026 monthly change centered in the 0.30-0.40% range: 61% above 0.30% but only 45% above 0.40%."
  - "May's hot 0.47% monthly print is above the market's implied central tendency for August, suggesting the market does not fully expect the energy-driven surge to persist into late summer."
  - "The distribution still prices 35% above 0.50%, leaving a meaningful tail for continued elevated inflation if Iran-related energy shocks persist."
  - "Resolves via Bureau of Labor Statistics August CPI release; seasonal adjustment methodology and energy price path between now and August are the key settlement variables."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May CPI jumped 0.47% month-over-month seasonally adjusted, driven by supercore services, gasoline, and AI-driven electricity demand, reaching 4.25% year-over-year."
    publisher: "wolfstreet.com"
    published_at: "2026-06-10T00:00:00.000Z"
    source_url: "https://wolfstreet.com/2026/06/10/cpi-inflation-4-25-blows-by-2-year-treasury-yield-closes-in-on-10-year-treasury-driven-by-supercore-services-gasoline-electricity/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "wolfstreet.com"
        source_url: "https://wolfstreet.com/2026/06/10/cpi-inflation-4-25-blows-by-2-year-treasury-yield-closes-in-on-10-year-treasury-driven-by-supercore-services-gasoline-electricity/"
        retrieved_at: "2026-06-11T12:08:11+00:00"
  - type: "pm_response"
    notes: "Ladder distribution for August 2026 CPI monthly change centers on 0.30-0.40%, below May's 0.47% print, indicating the market expects some moderation but retains a 35% tail above 0.50%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "wolfstreet.com: CPI Inflation 4.25%, Blows by 2-Year Treasury Yield, Closes in on 10-Y"
    url: "https://wolfstreet.com/2026/06/10/cpi-inflation-4-25-blows-by-2-year-treasury-yield-closes-in-on-10-year-treasury-driven-by-supercore-services-gasoline-electricity/"
    published_at: "2026-06-10T00:00:00.000Z"
    retrieved_at: "2026-06-11T12:08:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
