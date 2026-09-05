---
signal_id: "CMSIG2026090506"
signal_slug: "ukraine-cedes-territory-by-2026-polymarket-10-2026-09-05"
headline: "Ukraine cedes territory by 2026: Polymarket 10%"
semantic_title: "Ukraine ceding territory to Russia by year-end stays a long shot"
telemetry: "Polymarket 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-05T00:00:00.000Z"
event_id: "CM-EVT-XP7FFT2MC9"
event_slug: "will-ukraine-agree-to-cede-territory-to-russia-before-2027"
event_question: "Will Ukraine agree to cede territory to Russia by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x21bf9a7dae81b6bd51acae73185686ab8997b81b1401e4be10e114d472599c26"
  question_raw: "Will Ukraine agree to cede territory to Russia before 2027?"
  current_price: 0.1
  volume_24h_usd: 3158.6622490000004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 10% odds that Ukraine will agree to cede territory to Russia by end of 2026, resolving via UMA oracle."
  - "Despite the Witkoff-Kushner diplomatic mission, the market treats a territorial concession deal as a long shot, the peace push is not moving the needle to YES."
  - "Russia's rejection of Zelensky's proposed air truce and continued strikes during the envoys' visit reinforce the market's skeptical pricing."
  - "Companion Polymarket contract (CM-EVT-QP1YL1BSS0) puts just 7% on Trump, Putin, and Zelensky being seen together before 2027, suggesting the market sees summit-level engagement as even less likely than a territorial deal."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump envoys Steve Witkoff and Jared Kushner traveled to Moscow and Kyiv with a new proposal to end the Russia-Ukraine war."
    publisher: "france24.com"
    published_at: "2026-09-05T00:00:00.000Z"
    source_url: "https://www.france24.com/en/europe/20260905-trump-sends-envoys-to-moscow-and-kyiv-with-new-plan-to-end-the-war"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "france24.com"
        source_url: "https://www.france24.com/en/europe/20260905-trump-sends-envoys-to-moscow-and-kyiv-with-new-plan-to-end-the-war"
        retrieved_at: "2026-09-05T11:34:19+00:00"
  - type: "pm_response"
    notes: "Polymarket at 10% is fading the diplomatic optimism in the headlines; Russia's continued strikes are consistent with the low probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "france24.com: Trump sends envoys Witkoff and Kushner to Moscow and Kyiv with new pla"
    url: "https://www.france24.com/en/europe/20260905-trump-sends-envoys-to-moscow-and-kyiv-with-new-plan-to-end-the-war"
    published_at: "2026-09-05T00:00:00.000Z"
    retrieved_at: "2026-09-05T11:34:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
