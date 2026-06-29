---
signal_id: "CMSIG2026062604"
signal_slug: "scotus-strikes-birthright-order-polymarket-94-2026-06-26"
headline: "SCOTUS strikes birthright order: Polymarket 94%"
semantic_title: "SCOTUS striking birthright citizenship order solidifies near certainty"
telemetry: "Polymarket 94%"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-06-26T18:09:18.000Z"
event_id: "CM-EVT-4HHYC680N8"
event_slug: "scotus-strikes-down-trumps-birthright-citizenship-eo"
event_question: "Will SCOTUS strike down Trump's Birthright Citizenship Executive Order?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x12609f33bc603cb234db2af1d502d143587b697bdc479ddb9344401dbf987914"
  question_raw: "SCOTUS strikes down Trump's Birthright Citizenship EO?"
  current_price: 0.936
  volume_24h_usd: 308.329997
  arbitration_model: "uma_oracle"
  resolution_source: "whitehouse.gov"
  resolves_at: "2026-08-31T00:00:00Z"
bullets:
  - "Polymarket prices the Supreme Court striking down Trump's birthright citizenship executive order at 94%, resolving via whitehouse.gov."
  - "Pre-ruling coverage noting broad legal consensus against the order aligns with the market's near-certain pricing against it."
  - "A companion Kalshi contract prices the order coming into effect by December 31 at just 7%, consistent with the 94% strike-down probability on Polymarket."
  - "Polymarket's FTC commissioner firing case resolves at 95% in Trump's favor, highlighting that the market differentiates sharply between executive-power wins and constitutional overreach."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Supreme Court is expected to rule imminently on Trump's executive order attempting to end birthright citizenship."
    publisher: "ABC News"
    published_at: "2026-06-26T18:09:18.000Z"
    source_url: "https://abcnews.com/Politics/faq-birthright-citizenship-ahead-supreme-courts-ruling/story?id=134215675"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/Politics/faq-birthright-citizenship-ahead-supreme-courts-ruling/story?id=134215675"
        retrieved_at: "2026-06-29T01:46:24+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via whitehouse.gov; cross-venue Kalshi at 7% on order taking effect confirms directional alignment."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: What to know about birthright citizenship ahead of Supreme Court's rul"
    url: "https://abcnews.com/Politics/faq-birthright-citizenship-ahead-supreme-courts-ruling/story?id=134215675"
    published_at: "2026-06-26T18:09:18.000Z"
    retrieved_at: "2026-06-29T01:46:24+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
