---
signal_id: "CMSIG2026082005"
signal_slug: "gop-wins-georgia-senate-polymarket-7-2026-08-20"
headline: "GOP wins Georgia Senate: Polymarket 7%"
semantic_title: "Republican odds in Georgia Senate race stay near long-shot territory"
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
  volume_24h_usd: 1.85
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket puts only 7% on the Republican candidate winning the Georgia Senate election, resolving via UMA oracle."
  - "Focus group data showing economic anxiety among Georgia undecided voters aligns with the market's strong lean toward the Democratic candidate."
  - "A Kalshi contract at 92% prices the Georgia Senate race being decided by January 4, 2027, suggesting high confidence in a clean outcome timeline even if the seat itself is lopsided."
  - "The Ohio Senate Kalshi contract sits at 48%, nearly even, highlighting Georgia as an outlier, the economic anxiety story may matter far more in competitive races."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Focus groups in Iowa and Georgia show deep economic anxiety among undecided voters driving Senate race dynamics heading into the 2026 midterms."
    publisher: "nbcnews.com"
    published_at: "2026-08-20T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/politics/2026-election/focus-groups-deep-anxiety-economy-drives-undecided-voters-two-key-sena-rcna593115"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nbcnews.com"
        source_url: "https://www.nbcnews.com/politics/2026-election/focus-groups-deep-anxiety-economy-drives-undecided-voters-two-key-sena-rcna593115"
        retrieved_at: "2026-08-22T08:23:10+00:00"
  - type: "pm_response"
    notes: "Polymarket's 7% on a Republican Georgia Senate win represents a heavily one-sided pricing; the Kalshi timing contract at 92% adds confidence the race resolves on schedule."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nbcnews.com: Focus groups: Deep anxiety about the economy drives undecided voters i"
    url: "https://www.nbcnews.com/politics/2026-election/focus-groups-deep-anxiety-economy-drives-undecided-voters-two-key-sena-rcna593115"
    published_at: "2026-08-20T00:00:00.000Z"
    retrieved_at: "2026-08-22T08:23:10+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
