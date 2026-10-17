---
signal_id: "CMSIG2026101706"
signal_slug: "trump-putin-zelensky-together-before-2027-polymarket-3-2026-10-17"
headline: "Trump, Putin, Zelensky together before 2027: Polymarket 3%"
semantic_title: "Trump-Putin-Zelensky joint appearance stays a long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-17T00:00:00.000Z"
event_id: "CM-EVT-QP1YL1BSS0"
event_slug: "trump-putin-and-zelensky-seen-together-before-2027"
event_question: "Will Trump, Putin, and Zelensky be seen together before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa04dcb7b7f5a313d09e7728ca39835be4096da877ca5fbae5e3a36af239433c3"
  question_raw: "Trump, Putin, and Zelensky seen together before 2027?"
  current_price: 0.03
  volume_24h_usd: 68.43
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 3% odds on Trump, Russian President Vladimir Putin, and Ukrainian President Volodymyr Zelensky being seen together before 2027."
  - "Trump's sanctions waiver and public row with Zelensky are consistent with this near-zero probability: the market does not see a trilateral summit as a realistic near-term outcome."
  - "A companion Polymarket contract (CM-EVT-FNBRJ6KY59) at 7% on a formal Trump-Putin-Zelensky meeting shows some premium for a structured summit over an informal joint sighting, but both remain deeply discounted."
  - "Resolution is via Polymarket's UMA oracle; the 3% vs 7% spread between 'seen together' and 'meet together' reflects minimal incremental probability even for the weaker threshold."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump waived multiple Russia sanctions two days before they were set to take effect, deepening his dispute with Ukrainian President Volodymyr Zelensky."
    publisher: "Max Matza"
    published_at: "2026-10-17T00:00:00.000Z"
    source_url: "https://www.bbc.com/news/articles/cxr5yvzv7rp0o"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Max Matza"
        source_url: "https://www.bbc.com/news/articles/cxr5yvzv7rp0o"
        retrieved_at: "2026-10-17T11:57:10+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via UMA oracle; the near-identical pricing across both Trump-Putin-Zelensky contracts signals the market views diplomatic contact at any level as highly unlikely in 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Max Matza: Trump waives several Russia sanctions as row with Zelensky intensifies"
    url: "https://www.bbc.com/news/articles/cxr5yvzv7rp0o"
    published_at: "2026-10-17T00:00:00.000Z"
    retrieved_at: "2026-10-17T11:57:10+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
