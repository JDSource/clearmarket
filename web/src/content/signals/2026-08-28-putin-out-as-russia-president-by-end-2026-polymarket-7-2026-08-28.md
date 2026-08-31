---
signal_id: "CMSIG2026082808"
signal_slug: "putin-out-as-russia-president-by-end-2026-polymarket-7-2026-08-28"
headline: "Putin out as Russia president by end-2026: Polymarket 7%"
semantic_title: "Putin leaving Russia's presidency by end of 2026 stays a long shot"
telemetry: "Polymarket 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-28T15:46:15.091Z"
event_id: "CM-EVT-5WJSMVBVS7"
event_slug: "putin-out-before-2027"
event_question: "Will Vladimir Putin no longer be President of Russia by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6bd56627aa21311850825edb27e53434a0e17a4f782be0086bc07f71eee00d0d"
  question_raw: "Putin out as President of Russia by December 31, 2026?"
  current_price: 0.07
  volume_24h_usd: 17812.810959000002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T18:30:00Z"
bullets:
  - "Polymarket puts just 7% odds on Putin no longer serving as Russian president by end-2026, with trading volume up 1,440% day over day, signaling a sharp spike in market attention."
  - "The SCO summit bringing Putin alongside Xi and Modi on the world stage is consistent with the market's strong view that Putin's hold on power remains intact through year-end."
  - "The volume surge without a meaningful move toward 50% suggests the SCO gathering and ongoing war are drawing attention but not shifting the consensus on Putin's political survival."
  - "Polymarket resolves via UMA oracle; departure by any means including death, resignation, or removal would trigger resolution, making the 7% price a composite of all removal scenarios."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Xi Jinping, Narendra Modi, and Vladimir Putin are set to meet at the SCO summit in Kyrgyzstan, with the bloc representing 3.4 billion people gathering against a backdrop of active conflict in Ukraine and the Middle East."
    publisher: "Anadolu Ajansı"
    published_at: "2026-08-28T15:46:15.091Z"
    source_url: "https://www.aa.com.tr/en/eurasia/xi-modi-putin-to-meet-in-kyrgyzstan-what-to-watch-at-sco-summit/4040106"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Anadolu Ajansı"
        source_url: "https://www.aa.com.tr/en/eurasia/xi-modi-putin-to-meet-in-kyrgyzstan-what-to-watch-at-sco-summit/4040106"
        retrieved_at: "2026-08-31T15:47:21+00:00"
  - type: "pm_response"
    notes: "Polymarket's 1,440% volume surge is the sharpest day-over-day trading increase in this batch, making it the strongest signal of fresh market interest even as the probability itself holds near a long shot."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Anadolu Ajansı: Xi, Modi, Putin to meet in Kyrgyzstan: What to watch at SCO summit"
    url: "https://www.aa.com.tr/en/eurasia/xi-modi-putin-to-meet-in-kyrgyzstan-what-to-watch-at-sco-summit/4040106"
    published_at: "2026-08-28T15:46:15.091Z"
    retrieved_at: "2026-08-31T15:47:21+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
