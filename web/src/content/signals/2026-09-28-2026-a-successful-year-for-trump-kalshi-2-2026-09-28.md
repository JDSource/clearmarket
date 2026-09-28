---
signal_id: "CMSIG2026092808"
signal_slug: "2026-a-successful-year-for-trump-kalshi-2-2026-09-28"
headline: "2026 a successful year for Trump: Kalshi 2%"
semantic_title: "Markets put long odds against 2026 being a successful year for Trump"
telemetry: "Kalshi 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-28T00:00:00.000Z"
event_id: "CM-EVT-W81X57LB82"
event_slug: "kxtrumpbullcasecombo-27dec"
event_question: "Will 2026 be a successful year for Trump?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPBULLCASECOMBO-27DEC-26"
  question_raw: "Will the bull case for Trump occur in 2026?"
  current_price: 0.025
  volume_24h_usd: 2.37
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-12-31T15:00:00Z"
bullets:
  - "Kalshi puts only 2% on 2026 being a successful year for Trump, resolving via Bureau of Labor Statistics data."
  - "Reports of the worst-ever GOP midterm outlook and record-low Trump approval are consistent with the contract's near-zero pricing."
  - "The BLS resolution source suggests the contract may be tied to an economic metric rather than a political judgment, which is worth noting for settlement risk."
  - "Companion Polymarket contracts price Republican incumbents winning safe districts at 95-96%, showing the market distinguishes between Trump's national brand and safe-seat outcomes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US media reports the GOP midterm outlook is described as the worst ever, with Trump's approval weighing on Republican candidates and farmers among those turning away from the party."
    publisher: "Park Jaehyeon"
    published_at: "2026-09-28T00:00:00.000Z"
    source_url: "https://news.sbs.co.kr/english/article.do?news_id=N1008771924"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Park Jaehyeon"
        source_url: "https://news.sbs.co.kr/english/article.do?news_id=N1008771924"
        retrieved_at: "2026-09-28T07:47:41+00:00"
  - type: "pm_response"
    notes: "Kalshi resolves via Bureau of Labor Statistics, suggesting an economic benchmark defines 'successful', traders should confirm the exact resolution criteria before positioning."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Park Jaehyeon: GOP Midterm Outlook 'Worst Ever' Due to Trump Undertow, Even Farmers T"
    url: "https://news.sbs.co.kr/english/article.do?news_id=N1008771924"
    published_at: "2026-09-28T00:00:00.000Z"
    retrieved_at: "2026-09-28T07:47:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
