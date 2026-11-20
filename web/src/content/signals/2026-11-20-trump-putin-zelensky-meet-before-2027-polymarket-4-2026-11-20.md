---
signal_id: "CMSIG2026112005"
signal_slug: "trump-putin-zelensky-meet-before-2027-polymarket-4-2026-11-20"
headline: "Trump, Putin, Zelensky meet before 2027: Polymarket 4%"
semantic_title: "Trump, Putin, and Zelensky meeting before 2027 stays a long shot"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-20T02:35:44.000Z"
event_id: "CM-EVT-FNBRJ6KY59"
event_slug: "trump-putin-and-zelensky-meet-together-before-2027"
event_question: "Will Trump, Putin, and Zelensky meet together before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe96fd18679de58fa286f10b49d93f46829243cd105d74ce5d18eae0dd973b204"
  question_raw: "Trump, Putin, and Zelensky meet together before 2027?"
  current_price: 0.042
  volume_24h_usd: 1040.796185
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 4% on Trump, Putin, and Zelensky meeting together before 2027."
  - "The trilateral summit excluded Zelensky entirely; the peace declaration contained no mention of Ukraine peace terms, consistent with the market's low odds."
  - "A companion Polymarket contract (CM-EVT-QP1YL1BSS0) on Trump, Putin, and Zelensky being seen together prices identically at 4%, showing no spread between the two formulations."
  - "Resolves via UMA oracle; requires all three leaders to meet in the same setting, a threshold the Shenzhen summit did not meet."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump, Putin, and Xi met in Shenzhen and issued a peace declaration, but the summit produced no concrete action on Ukraine and Zelensky was absent."
    publisher: "Lucia Stein, Bang Xiao, Patrick Martin"
    published_at: "2026-11-20T02:35:44.000Z"
    source_url: "https://www.abc.net.au/news/2026-11-20/key-takeaways-from-trump-xi-putin-meeting/107407564"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Lucia Stein, Bang Xiao, Patrick Martin"
        source_url: "https://www.abc.net.au/news/2026-11-20/key-takeaways-from-trump-xi-putin-meeting/107407564"
        retrieved_at: "2026-11-20T07:47:31+00:00"
  - type: "pm_response"
    notes: "Polymarket at 4% on the trilateral Zelensky meeting; the market treats Ukraine inclusion in summit diplomacy as a remote near-term prospect."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Lucia Stein, Bang Xiao, Patrick Martin: Trump-Xi-Putin meeting delivers peace declaration but no action on Ukr"
    url: "https://www.abc.net.au/news/2026-11-20/key-takeaways-from-trump-xi-putin-meeting/107407564"
    published_at: "2026-11-20T02:35:44.000Z"
    retrieved_at: "2026-11-20T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
