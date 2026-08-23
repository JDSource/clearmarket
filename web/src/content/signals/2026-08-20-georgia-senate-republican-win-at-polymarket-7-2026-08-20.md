---
signal_id: "CMSIG2026082007"
signal_slug: "georgia-senate-republican-win-at-polymarket-7-2026-08-20"
headline: "Georgia Senate: Republican win at Polymarket 7%"
semantic_title: "Georgia Senate Republican win remains a heavy long shot"
telemetry: "Polymarket 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-20T00:00:00.000Z"
event_id: "CM-EVT-301LWVGPR3"
event_slug: "georgia-senate-election-winner"
event_question: "Will the Georgia Senate election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x54e4e816cc5868e2f933c6bbc597e3313bdad382be3ecf7eaa4d8fa5c3f1a1bd"
  question_raw: "Will the Republicans win the Georgia Senate race in 2026?"
  current_price: 0.068
  volume_24h_usd: 3.21
  arbitration_model: "uma_oracle"
bullets:
  - "The Polymarket contract on the Republican candidate winning the Georgia Senate election sits at 7%."
  - "Focus group data showing voter anxiety about costs and the economy is consistent with the market's heavy lean against the Republican in Georgia."
  - "The Kalshi contract on the Georgia race being decided by January 4, 2027 sits at 92%, so the market expects a result, just not a Republican one."
  - "Resolution via UMA oracle for the winner market; the 92% resolution-timing contract resolves via United States Congress certification."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Focus groups in Iowa and Georgia show deep economic anxiety driving undecided voters in two key Senate races ahead of midterms."
    publisher: "nbcnews.com"
    published_at: "2026-08-20T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/politics/2026-election/focus-groups-deep-anxiety-economy-drives-undecided-voters-two-key-sena-rcna593115"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nbcnews.com"
        source_url: "https://www.nbcnews.com/politics/2026-election/focus-groups-deep-anxiety-economy-drives-undecided-voters-two-key-sena-rcna593115"
        retrieved_at: "2026-08-23T08:24:02+00:00"
  - type: "pm_response"
    notes: "Polymarket prices Georgia as a near-certain Democratic hold at 93% implied; Kalshi's 92% on timely resolution confirms the seat is expected to be called before the new Congress."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nbcnews.com: Focus groups: Deep anxiety about the economy drives undecided voters i"
    url: "https://www.nbcnews.com/politics/2026-election/focus-groups-deep-anxiety-economy-drives-undecided-voters-two-key-sena-rcna593115"
    published_at: "2026-08-20T00:00:00.000Z"
    retrieved_at: "2026-08-23T08:24:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
