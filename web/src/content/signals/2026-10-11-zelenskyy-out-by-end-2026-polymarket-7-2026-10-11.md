---
signal_id: "CMSIG2026101108"
signal_slug: "zelenskyy-out-by-end-2026-polymarket-7-2026-10-11"
headline: "Zelenskyy out by end 2026: Polymarket 7%"
semantic_title: "Odds on Zelenskyy exit by end of 2026 stay low"
telemetry: "Polymarket 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-11T00:00:00.000Z"
event_id: "CM-EVT-355Q75KD17"
event_slug: "zelenskyy-out-as-ukraine-president-before-2027"
event_question: "Will Zelenskyy be out as Ukraine president by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x51f624dbbf14f9edb575fef1be6f7a303751de70783fa144fce27b957452c803"
  question_raw: "Zelenskyy out as Ukraine president by end of 2026?"
  current_price: 0.07
  volume_24h_usd: 65831.815267
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 7% odds on Zelenskyy leaving the Ukrainian presidency by end of 2026."
  - "Despite Trump's public call for Zelenskyy's replacement, the market treats the outcome as a long shot, not a live probability."
  - "Zelenskyy's defiant response -- vowing continued refinery strikes -- reinforces his political durability as priced by the market."
  - "Companion Polymarket contract on Trump, Putin, and Zelenskyy meeting together before 2027 sits at 6%, suggesting no diplomatic off-ramp is priced either."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "President Donald Trump publicly called for a new Ukrainian president, while President Volodymyr Zelenskyy pushed back and vowed to continue striking Russian oil refineries."
    publisher: "cbsnews.com"
    published_at: "2026-10-11T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/news/zelenskyy-trump-new-ukrainian-president/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/zelenskyy-trump-new-ukrainian-president/"
        retrieved_at: "2026-10-11T14:35:49+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; at 7%, the market is effectively pricing Trump's pressure campaign as political noise rather than a structural threat to Zelenskyy's tenure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: Zelenskyy claps back after Trump calls for new Ukrainian president to"
    url: "https://www.cbsnews.com/news/zelenskyy-trump-new-ukrainian-president/"
    published_at: "2026-10-11T00:00:00.000Z"
    retrieved_at: "2026-10-11T14:35:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
