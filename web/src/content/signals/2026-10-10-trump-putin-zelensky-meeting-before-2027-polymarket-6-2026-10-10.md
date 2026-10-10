---
signal_id: "CMSIG2026101005"
signal_slug: "trump-putin-zelensky-meeting-before-2027-polymarket-6-2026-10-10"
headline: "Trump-Putin-Zelensky meeting before 2027: Polymarket 6%"
semantic_title: "Trump, Putin, Zelensky meeting before 2027 stays near 6 percent"
telemetry: "Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-10T00:00:00.000Z"
event_id: "CM-EVT-FNBRJ6KY59"
event_slug: "trump-putin-and-zelensky-meet-together-before-2027"
event_question: "Will Trump, Putin, and Zelensky meet together before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe96fd18679de58fa286f10b49d93f46829243cd105d74ce5d18eae0dd973b204"
  question_raw: "Trump, Putin, and Zelensky meet together before 2027?"
  current_price: 0.06
  volume_24h_usd: 115.769472
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market prices a Trump-Putin-Zelensky in-person meeting before 2027 at 6%."
  - "The reported breakdown between Trump and Zelensky over the diesel deal makes a tripartite summit even less likely near term; the 6% level is consistent with that deterioration."
  - "A companion Polymarket contract on Trump, Putin, and Zelensky being seen together (CM-EVT-QP1YL1BSS0) also sits at 6%, confirming cross-market alignment."
  - "Resolution via uma_oracle requires documented evidence of all three leaders meeting together before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A US official said Trump cut the Russian diesel deal with Putin after Zelensky ignored Trump's requests, deepening the Kyiv-Washington rift."
    publisher: "Barak Ravid"
    published_at: "2026-10-10T00:00:00.000Z"
    source_url: "https://www.axios.com/2026/10/10/trump-zelensky-putin-diesel-deal-war"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Barak Ravid"
        source_url: "https://www.axios.com/2026/10/10/trump-zelensky-putin-diesel-deal-war"
        retrieved_at: "2026-10-10T07:47:51+00:00"
  - type: "pm_response"
    notes: "Polymarket at 6%; resolves via uma_oracle on a confirmed joint appearance of all three leaders."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Barak Ravid: U.S. official: Trump cut deal with Putin after Zelensky ignored his re"
    url: "https://www.axios.com/2026/10/10/trump-zelensky-putin-diesel-deal-war"
    published_at: "2026-10-10T00:00:00.000Z"
    retrieved_at: "2026-10-10T07:47:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
