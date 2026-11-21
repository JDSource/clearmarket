---
signal_id: "CMSIG2026111903"
signal_slug: "trump-putin-zelensky-together-before-2027-polymarket-5-2026-11-19"
headline: "Trump, Putin, Zelensky together before 2027: Polymarket 5%"
semantic_title: "Trump-Putin-Zelensky summit stays a long shot at 5 percent"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-19T00:15:49.000Z"
event_id: "CM-EVT-QP1YL1BSS0"
event_slug: "trump-putin-and-zelensky-seen-together-before-2027"
event_question: "Will Trump, Putin, and Zelensky be seen together before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa04dcb7b7f5a313d09e7728ca39835be4096da877ca5fbae5e3a36af239433c3"
  question_raw: "Trump, Putin, and Zelensky seen together before 2027?"
  current_price: 0.051
  volume_24h_usd: 98.03
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only a 5% chance Trump, Putin, and Zelensky are seen together before 2027, resolves via UMA oracle."
  - "The Trump-Putin-Xi trilateral summit produced a peace declaration, but Zelensky's exclusion means the specific three-way market condition remains far from met."
  - "Ukraine allies warned at a Berlin meeting that the so-called Yalta format would not bring peace, adding political friction to any Zelensky inclusion scenario."
  - "The companion Polymarket contract on Ukraine ceding territory (CM-EVT-XP7FFT2MC9) also sits at just 3%, suggesting markets see the peace process stalling well short of a final settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump, Putin, and Xi Jinping issued a joint declaration on peace after 90-minute talks in China, but Zelensky was absent from the summit."
    publisher: "bbc.com"
    published_at: "2026-11-19T00:15:49.000Z"
    source_url: "https://www.bbc.com/news/live/cmlye926e2eet"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.com"
        source_url: "https://www.bbc.com/news/live/cmlye926e2eet"
        retrieved_at: "2026-11-21T07:47:41+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the summit news is concurrent with the 5% price, which the market is not moving toward despite headline diplomacy."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.com: Trump, Putin, and Xi issue 'joint declaration on peace' after 90-minut"
    url: "https://www.bbc.com/news/live/cmlye926e2eet"
    published_at: "2026-11-19T00:15:49.000Z"
    retrieved_at: "2026-11-21T07:47:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
