---
signal_id: "CMSIG2026092406"
signal_slug: "trump-visits-iran-kalshi-3-2026-09-24"
headline: "Trump visits Iran: Kalshi 3%"
semantic_title: "Trump visiting Iran stays a long shot despite Xi summit"
telemetry: "Kalshi 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-24T00:00:00.000Z"
event_id: "CM-EVT-V9QGT2SSP7"
event_slug: "kxtrumpiran"
event_question: "Will Donald Trump visit Iran?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPIRAN-27JAN01"
  question_raw: "Will Donald Trump visit Iran before Jan 1, 2027?"
  current_price: 0.034
  volume_24h_usd: 20.64
  arbitration_model: "kalshi_staff"
  resolution_source: "The Guardian"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi prices the probability that Donald Trump visits Iran at just 3%."
  - "The Trump-Xi summit addresses Iran as a topic, but market pricing makes clear that a physical Trump visit to Iran is seen as a near-impossibility regardless of diplomatic momentum."
  - "Cross-reference: the Polymarket contract on Iran ending uranium enrichment by December 31 sits at 12%, suggesting the market also sees a comprehensive deal as unlikely this year."
  - "Resolves via The Guardian as the designated resolution source."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "President Donald Trump gave Chinese President Xi Jinping a rare airport welcome as the two leaders began a state visit focused on trade, artificial intelligence, and Iran."
    publisher: "france24.com"
    published_at: "2026-09-24T00:00:00.000Z"
    source_url: "https://www.france24.com/en/americas/20260924-trump-gives-xi-rare-airport-welcome-as-chinese-leader-begins-us-state-visit"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "france24.com"
        source_url: "https://www.france24.com/en/americas/20260924-trump-gives-xi-rare-airport-welcome-as-chinese-leader-begins-us-state-visit"
        retrieved_at: "2026-09-24T13:07:56+00:00"
  - type: "pm_response"
    notes: "Kalshi's 3% on a Trump Iran visit is a near-zero long shot; the 12% Polymarket enrichment-end contract (CM-EVT-4CKJ2D3T77) is the more liquid proxy for US-Iran diplomatic progress."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "france24.com: Trump gives Xi rare airport welcome as Chinese leader begins US state"
    url: "https://www.france24.com/en/americas/20260924-trump-gives-xi-rare-airport-welcome-as-chinese-leader-begins-us-state-visit"
    published_at: "2026-09-24T00:00:00.000Z"
    retrieved_at: "2026-09-24T13:07:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
