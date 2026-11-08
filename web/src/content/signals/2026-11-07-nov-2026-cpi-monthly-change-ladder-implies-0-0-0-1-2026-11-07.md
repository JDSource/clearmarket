---
signal_id: "CMSIG2026110702"
signal_slug: "nov-2026-cpi-monthly-change-ladder-implies-0-0-0-1-2026-11-07"
headline: "Nov 2026 CPI monthly change: ladder implies 0.0-0.1%"
semantic_title: "CPI for November seen flat to slightly lower by consensus"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-07T21:00:00.000Z"
event_id: "CM-EVT-T57DHL6V48"
event_slug: "kxcpi-26nov"
event_question: "November 2026 CPI month-over-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26NOV-T0.1"
  question_raw: "Will CPI rise more than 0.1% in November 2026?"
  current_price: 0.37
  volume_24h_usd: 233.32
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-11T14:56:00Z"
bullets:
  - "Ladder implies the market-consensus November 2026 CPI monthly change lands in the 0.0-0.1% range: 60% above 0.0%, only 37% above 0.1%, and 73% above -0.1%."
  - "Bloomberg's forecast of a CPI cooldown is consistent with the ladder's heavy weighting toward flat-to-modest gains; trading volume surged 3,443% day-over-day, flagging strong fresh interest."
  - "The sharp drop from 60% at 0.0% to 10% at 0.2% shows the market sees minimal risk of an upside inflation surprise this month."
  - "Resolution uses the official BLS CPI release; any rounding near the 0.05% boundary could shift bracket outcomes significantly."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bloomberg reported US inflation likely cooled in October after two consecutive months of faster price gains, with goods and services prices expected to slow."
    publisher: "Vince Golle, Craig Stirling"
    published_at: "2026-11-07T21:00:00.000Z"
    source_url: "https://www.bloomberg.com/news/articles/2026-11-07/us-inflation-set-to-simmer-down-some-after-recent-pickup"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Vince Golle, Craig Stirling"
        source_url: "https://www.bloomberg.com/news/articles/2026-11-07/us-inflation-set-to-simmer-down-some-after-recent-pickup"
        retrieved_at: "2026-11-08T07:47:56+00:00"
  - type: "pm_response"
    notes: "Volume spike of 35.4x day-over-day confirms this ladder is drawing significant new attention ahead of the CPI print."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Vince Golle, Craig Stirling: US Inflation Set to Simmer Down Some After Recent Pickup"
    url: "https://www.bloomberg.com/news/articles/2026-11-07/us-inflation-set-to-simmer-down-some-after-recent-pickup"
    published_at: "2026-11-07T21:00:00.000Z"
    retrieved_at: "2026-11-08T07:47:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
