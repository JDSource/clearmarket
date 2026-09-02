---
signal_id: "CMSIG2026090205"
signal_slug: "us-debt-default-by-2027-polymarket-2-2026-09-02"
headline: "US debt default by 2027: Polymarket 2%"
semantic_title: "US debt default by 2027 stays priced as a remote tail risk"
telemetry: "Polymarket 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-02T00:00:00.000Z"
event_id: "CM-EVT-4K3BQFVQD9"
event_slug: "us-defaults-on-debt-by-2027"
event_question: "Will the United States default on its debt by 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5b9cb2fbdfb50eae19a1fdd228487ff797fab1539a1e74565b5e6ad3b586368b"
  question_raw: "US defaults on debt by 2027?"
  current_price: 0.02
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on a US debt default by 2027 sits at 2%, pricing the event as a near-impossibility despite the $40 trillion milestone."
  - "The debt headline is alarming in framing, but the market is not moving off near-zero: high debt and high borrowing costs are not the same as default risk."
  - "The government shutdown contract simultaneously sitting at 3% on Kalshi reinforces the broader message, markets are treating fiscal stress as chronic, not acute."
  - "Resolution via UMA oracle; a technical default or missed Treasury payment would resolve YES, a continuing series of deficit spending would not."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US national debt has topped $40 trillion as borrowing costs rise, with Trump's fiscal record diverging sharply from pledged restraint."
    publisher: "jgiesler"
    published_at: "2026-09-02T00:00:00.000Z"
    source_url: "https://srnnews.com/trump-pledged-fiscal-restraint-instead-debt-tops-40-trillion-as-borrowing-costs-rise/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "jgiesler"
        source_url: "https://srnnews.com/trump-pledged-fiscal-restraint-instead-debt-tops-40-trillion-as-borrowing-costs-rise/"
        retrieved_at: "2026-09-02T12:29:02+00:00"
  - type: "pm_response"
    notes: "Polymarket at 2% directly contradicts any narrative that debt-ceiling or fiscal trajectory concerns are driving near-term default pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "jgiesler: Trump pledged fiscal restraint. Instead, debt tops $40 trillion as bor"
    url: "https://srnnews.com/trump-pledged-fiscal-restraint-instead-debt-tops-40-trillion-as-borrowing-costs-rise/"
    published_at: "2026-09-02T00:00:00.000Z"
    retrieved_at: "2026-09-02T12:29:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
