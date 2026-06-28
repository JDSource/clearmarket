---
signal_id: "CMSIG2026062606"
signal_slug: "scotus-strikes-birthright-eo-polymarket-94-2026-06-26"
headline: "SCOTUS strikes birthright EO: Polymarket 94%"
semantic_title: "SCOTUS birthright citizenship order strike-down nears full pricing"
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
  volume_24h_usd: 826.8121850000001
  arbitration_model: "uma_oracle"
  resolution_source: "whitehouse.gov"
  resolves_at: "2026-08-31T00:00:00Z"
bullets:
  - "Polymarket prices SCOTUS striking down the birthright citizenship executive order at 94%, with trading volume up 3,642% day over day."
  - "The Supreme Court ruling is imminent; the surge in volume signals fresh capital entering the contract as the decision approaches."
  - "The companion Kalshi contract (CM-EVT-JZ03HX93V0) prices the executive order actually coming into effect at only 6%, directly consistent with the 94% strike-down read."
  - "Resolves via whitehouse.gov; a ruling that blocks the order from taking effect would settle the Polymarket contract YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Supreme Court is expected next week to rule on President Trump's executive order attempting to end birthright citizenship."
    publisher: "ABC News"
    published_at: "2026-06-26T18:09:18.000Z"
    source_url: "https://abcnews.com/Politics/faq-birthright-citizenship-ahead-supreme-courts-ruling/story?id=134215675"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/Politics/faq-birthright-citizenship-ahead-supreme-courts-ruling/story?id=134215675"
        retrieved_at: "2026-06-28T10:24:59+00:00"
  - type: "pm_response"
    notes: "Polymarket at 94% with a 37x volume spike reflects pre-ruling positioning; the Kalshi complement at 6% enforces internal consistency."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: What to know about birthright citizenship ahead of Supreme Court's rul"
    url: "https://abcnews.com/Politics/faq-birthright-citizenship-ahead-supreme-courts-ruling/story?id=134215675"
    published_at: "2026-06-26T18:09:18.000Z"
    retrieved_at: "2026-06-28T10:24:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
