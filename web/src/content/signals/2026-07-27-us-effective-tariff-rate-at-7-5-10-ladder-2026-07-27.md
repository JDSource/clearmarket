---
signal_id: "CMSIG2026072704"
signal_slug: "us-effective-tariff-rate-at-7-5-10-ladder-2026-07-27"
headline: "US effective tariff rate at 7.5-10%: ladder"
semantic_title: "US effective tariff rate seen landing in the 7.5-10 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-27T00:00:00.000Z"
event_id: "CM-EVT-8P2Y9LGSL3"
event_slug: "kxefftariff-26jul30"
event_question: "US effective tariff rate (customs duties / nominal imports)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXEFFTARIFF-26JUL30-T10"
  question_raw: "Will the US effective tariff rate (customs duties collected ÷ nominal imports of goods, represented by B235RC1Q027SBEA ÷ A255RC1Q027SBEA) for Q2 2026 be above 10%?"
  current_price: 0.05
  volume_24h_usd: 40.6
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics- Employment Situation"
  resolves_at: "2026-08-06T14:00:00Z"
bullets:
  - "Ladder prices the US effective tariff rate most likely in the 7.5-10.0% range: 63% above 7.5% but only 5% above 10.0%."
  - "New tariffs on 80-plus countries are consistent with the ladder moving above the 7.5% threshold, but markets are not pricing a breakout above 10%."
  - "The sharp cliff from 63% to 5% between 7.5% and 10.0% suggests markets see the new round as incremental, not a step-change in the effective rate."
  - "Ladder resolves via customs duties collected divided by nominal import value; partial exemptions or legal challenges could cap the realized rate well below 10%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump imposed new tariffs on more than 80 countries effective Friday, reigniting global trade tensions in an already inflationary environment."
    publisher: "ABC News"
    published_at: "2026-07-27T00:00:00.000Z"
    source_url: "https://abcnews.com/Business/trumps-sweeping-new-tariffs-wallet/story?id=135050974"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/Business/trumps-sweeping-new-tariffs-wallet/story?id=135050974"
        retrieved_at: "2026-07-28T10:30:26+00:00"
  - type: "pm_response"
    notes: "Ladder distribution; the 92% above 5.0% confirms some tariff regime is fully priced in, but the tail above 10% remains very thin at 5%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: What Trump's sweeping new tariffs mean for your wallet - ABC News"
    url: "https://abcnews.com/Business/trumps-sweeping-new-tariffs-wallet/story?id=135050974"
    published_at: "2026-07-27T00:00:00.000Z"
    retrieved_at: "2026-07-28T10:30:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
