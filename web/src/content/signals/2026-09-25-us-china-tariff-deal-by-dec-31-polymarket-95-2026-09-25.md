---
signal_id: "CMSIG2026092505"
signal_slug: "us-china-tariff-deal-by-dec-31-polymarket-95-2026-09-25"
headline: "US-China tariff deal by Dec 31: Polymarket 95%"
semantic_title: "US-China tariff agreement by year-end stays near full pricing"
telemetry: "Polymarket 95%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-25T00:00:00.000Z"
event_id: "CM-EVT-52GRJCHNR9"
event_slug: "us-x-china-tariff-agreement-by-december-31"
event_question: "Will the US and China reach a tariff agreement by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf9c12aa09c5317d1cf8d26d0dc100a69ecf70e5132e81ef078d5336f63923b5e"
  question_raw: "US x China tariff agreement by December 31?"
  current_price: 0.949
  volume_24h_usd: 9652.738538999998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices a 95% chance the US and China reach a tariff agreement by December 31, 2026."
  - "Xi's White House visit, the highest-profile diplomatic contact of the year, is consistent with near-full market pricing of a deal, even though the summit fell short of a complete breakthrough."
  - "The partial nature of the summit outcome did not push the Polymarket contract meaningfully below its near-ceiling level, suggesting the market treats a formal agreement as a formality given existing framework talks."
  - "Resolves via Polymarket's UMA oracle; the contract requires a formal tariff agreement, not merely a communique or freeze, a key edge case if only a partial deal is announced."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Xi Jinping received a red carpet welcome at the White House but did not secure all he wanted from the Trump summit, per BBC reporting."
    publisher: "bbc.co.uk"
    published_at: "2026-09-25T00:00:00.000Z"
    source_url: "https://www.bbc.co.uk/news/articles/cr93e4x7kdjjo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.co.uk"
        source_url: "https://www.bbc.co.uk/news/articles/cr93e4x7kdjjo"
        retrieved_at: "2026-09-25T07:47:46+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 95%; resolves via UMA oracle with a formal agreement required, not a press statement or interim framework."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.co.uk: Xi Jinping got the red carpet treatment from Trump - but not everythin"
    url: "https://www.bbc.co.uk/news/articles/cr93e4x7kdjjo"
    published_at: "2026-09-25T00:00:00.000Z"
    retrieved_at: "2026-09-25T07:47:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
