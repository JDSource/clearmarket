---
signal_id: "CMSIG2026092208"
signal_slug: "trump-out-as-president-before-2027-polymarket-5-2026-09-22"
headline: "Trump out as president before 2027: Polymarket 5%"
semantic_title: "Trump leaving presidency before 2027 stays near zero at 5 percent"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-22T00:00:00.000Z"
event_id: "CM-EVT-ZW6ZK09DB1"
event_slug: "trump-out-as-president-before-2027"
event_question: "Will Donald Trump cease to be President before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48b0b0bca515f68fccf95af4793dbd0edbfec1f8ec6e8df2c0f69ba74f8c4722"
  question_raw: "Trump out as President before 2027?"
  current_price: 0.05
  volume_24h_usd: 47658.059626
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices the probability of Donald Trump ceasing to be president before 2027 at 5%."
  - "Iran's reported strategy of escalating to inflict political pain on Trump has not moved the Polymarket contract meaningfully off its low base."
  - "Sinking approval ratings on the economy and the Iran war, per the Reuters/Ipsos poll, add political pressure but are not translating into any serious market-priced removal risk."
  - "Resolves via uma oracle; the pre-2027 horizon means the contract covers only the remaining months of 2026, keeping the window narrow."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran is reportedly escalating the conflict to drive up oil prices and increase political pain for President Donald Trump ahead of the 2026 midterms."
    publisher: "Brian Bennett"
    published_at: "2026-09-22T00:00:00.000Z"
    source_url: "https://www.ms.now/news/trump-iran-war-midterms-pain"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Brian Bennett"
        source_url: "https://www.ms.now/news/trump-iran-war-midterms-pain"
        retrieved_at: "2026-09-22T13:03:08+00:00"
  - type: "pm_response"
    notes: "Polymarket at 5% on Trump leaving office before 2027 reflects market indifference to geopolitical pressure tactics despite a deteriorating approval backdrop."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Brian Bennett: ‘Pain for Trump’: Iran is trying to escalate the war before the midter"
    url: "https://www.ms.now/news/trump-iran-war-midterms-pain"
    published_at: "2026-09-22T00:00:00.000Z"
    retrieved_at: "2026-09-22T13:03:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
