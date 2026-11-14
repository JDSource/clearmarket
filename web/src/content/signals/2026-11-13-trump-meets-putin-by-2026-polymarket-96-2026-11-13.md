---
signal_id: "CMSIG2026111305"
signal_slug: "trump-meets-putin-by-2026-polymarket-96-2026-11-13"
headline: "Trump meets Putin by 2026: Polymarket 96%"
semantic_title: "Trump meeting Putin by year-end stays heavily favored at 96 percent"
telemetry: "Polymarket 96%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-11-13T19:30:22.000Z"
event_id: "CM-EVT-TK9WNXXYF6"
event_slug: "trump-meets-with-putin-by"
event_question: "Will Trump meet with Putin by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x15ddba100cf49043ada06a98d63ac221cdca86da873485dcca72c174cb9cc300"
  question_raw: "Trump meets with Putin by December 31?"
  current_price: 0.96
  volume_24h_usd: 7590.351634000001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Trump meeting Putin by 2026 sits at 96%, near full pricing given the confirmed APEC summit."
  - "With a specific date and location now reported by multiple outlets, the Polymarket odds are consistent with an imminent resolution; the 4% residual reflects logistical or cancellation risk only."
  - "The companion Polymarket contract on Trump, Putin, and Zelensky meeting together before 2027 sits at just 4%, underscoring that Ukraine is not expected at the Shenzhen summit."
  - "Resolves via UMA oracle; the meeting must be confirmed as having occurred before the 2026 deadline."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Politico and multiple outlets confirm Trump, Xi, and Putin plan a trilateral summit on the sidelines of APEC in Shenzhen on November 18-19."
    publisher: "Phelim Kine, Daniella Cheslow, Owen Dahlkamp, Eric Bazail-Eimil, Gregory Svirnovskiy"
    published_at: "2026-11-13T19:30:22.000Z"
    source_url: "https://www.politico.com/news/foreign-affairs"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Phelim Kine, Daniella Cheslow, Owen Dahlkamp, Eric Bazail-Eimil, Gregory Svirnovskiy"
        source_url: "https://www.politico.com/news/foreign-affairs"
        retrieved_at: "2026-11-14T07:47:51+00:00"
  - type: "pm_response"
    notes: "Polymarket at 96% leaves almost no room for a no-resolution; the APEC summit reporting makes this effectively a timing question."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Phelim Kine, Daniella Cheslow, Owen Dahlkamp, Eric Bazail-Eimil, Gregory Svirnovskiy: Foreign Affairs: Latest News, Top Stories & Analysis - POLITICO"
    url: "https://www.politico.com/news/foreign-affairs"
    published_at: "2026-11-13T19:30:22.000Z"
    retrieved_at: "2026-11-14T07:47:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
