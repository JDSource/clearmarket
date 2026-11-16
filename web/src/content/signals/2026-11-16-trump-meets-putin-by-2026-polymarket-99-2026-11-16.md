---
signal_id: "CMSIG2026111607"
signal_slug: "trump-meets-putin-by-2026-polymarket-99-2026-11-16"
headline: "Trump meets Putin by 2026: Polymarket 99%"
semantic_title: "Trump meeting Putin by 2026 nears full pricing"
telemetry: "Polymarket 99%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-11-16T04:16:17.000Z"
event_id: "CM-EVT-TK9WNXXYF6"
event_slug: "trump-meets-with-putin-by"
event_question: "Will Trump meet with Putin by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x15ddba100cf49043ada06a98d63ac221cdca86da873485dcca72c174cb9cc300"
  question_raw: "Trump meets with Putin by December 31?"
  current_price: 0.989
  volume_24h_usd: 4051.76562
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 99% on Trump meeting Putin by 2026, via UMA oracle, with the summit confirmed for November 19."
  - "China's official confirmation of the Xi-Trump-Putin trilateral at APEC makes the Polymarket contract effectively fully priced at 99%."
  - "The Trump-Putin-Zelensky together contract (CM-EVT-QP1YL1BSS0) sits at just 4%, showing the market cleanly separates a Putin meeting from a broader peace summit including Ukrainian President Volodymyr Zelenskyy."
  - "Polymarket's 1% residual on Putin no longer being president of Russia by year-end (CM-EVT-5WJSMVBVS7) is consistent with the near-certain summit read."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "China confirmed a historic Xi-Trump-Putin trilateral summit at APEC in Shenzhen on November 19, covering nuclear non-proliferation, the Middle East, and trade."
    publisher: "WATARU SUZUKI"
    published_at: "2026-11-16T04:16:17.000Z"
    source_url: "https://asia.nikkei.com/politics/international-relations/apec/apec-china-5-things-to-know-about-xi-jinping-s-diplomatic-show"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "WATARU SUZUKI"
        source_url: "https://asia.nikkei.com/politics/international-relations/apec/apec-china-5-things-to-know-about-xi-jinping-s-diplomatic-show"
        retrieved_at: "2026-11-16T07:48:02+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; with summit confirmed for November 19, the 1% residual reflects only exotic tail scenarios such as last-minute cancellation or force majeure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "WATARU SUZUKI: APEC China: 5 things to know about Xi Jinping's diplomatic show"
    url: "https://asia.nikkei.com/politics/international-relations/apec/apec-china-5-things-to-know-about-xi-jinping-s-diplomatic-show"
    published_at: "2026-11-16T04:16:17.000Z"
    retrieved_at: "2026-11-16T07:48:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
