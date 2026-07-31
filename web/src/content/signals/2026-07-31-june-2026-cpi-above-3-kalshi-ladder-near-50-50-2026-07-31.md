---
signal_id: "CMSIG2026073102"
signal_slug: "june-2026-cpi-above-3-kalshi-ladder-near-50-50-2026-07-31"
headline: "June 2026 CPI above 3%: Kalshi ladder near 50-50"
semantic_title: "US CPI above 3 percent for year ending June holds near 50%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-31T04:33:22.486Z"
event_id: "CM-EVT-XP5XZNK7W3"
event_slug: "kxcpiyoy-26jul"
event_question: "CPI inflation rate year ending June 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUL-T3.4"
  question_raw: "Will the rate of CPI inflation be above 3.4% for the year ending in July 2026?"
  current_price: 0.28
  volume_24h_usd: 4597.01
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-11-11T14:00:00Z"
bullets:
  - "Kalshi ladder implies June 2026 CPI in the 3.3-3.4% range: 98% above 3.0%, 59% above 3.3%, but only 28% above 3.4%."
  - "ABC News and AP both describe inflation as 'stubbornly high' amid the Iran war; the ladder's tight 3.3-3.4% implied range is consistent with elevated but not runaway readings."
  - "The sharp drop from 59% to 28% between the 3.3% and 3.4% strikes shows the market sees a hard ceiling just above 3.3%, not the kind of open-ended breakout that war-shock headlines often imply."
  - "Separately, a Kalshi binary on core CPI below 2.2% in 2026 sits at just 24%, reinforcing the ladder's message that inflation is stuck well above target."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US Q2 GDP grew at a sluggish 1.5% annualized rate as the Iran war fueled an inflation surge that slowed the economy more than expected."
    publisher: "ABC News"
    published_at: "2026-07-31T04:33:22.486Z"
    source_url: "https://abcnews.com/Business/government-report-show-us-economy-performed-amid-iran/story?id=135152547"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/Business/government-report-show-us-economy-performed-amid-iran/story?id=135152547"
        retrieved_at: "2026-07-31T10:34:33+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Bureau of Labor Statistics CPI release; the distribution is narrowly concentrated in the 3.3-3.4% band, reflecting the market's read of persistent but bounded inflation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: US economy slowed more than expected as the Iran war took hold"
    url: "https://abcnews.com/Business/government-report-show-us-economy-performed-amid-iran/story?id=135152547"
    published_at: "2026-07-31T04:33:22.486Z"
    retrieved_at: "2026-07-31T10:34:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
