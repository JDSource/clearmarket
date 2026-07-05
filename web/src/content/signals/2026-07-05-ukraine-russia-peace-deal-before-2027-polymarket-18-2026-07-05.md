---
signal_id: "CMSIG2026070504"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-18-2026-07-05"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 18%"
semantic_title: "Ukraine-Russia peace deal by 2027 consensus holds skeptical"
telemetry: "Polymarket 18%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-05T08:06:15.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.18
  volume_24h_usd: 19608.685139999998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices an 18% probability that Ukraine signs a peace deal with Russia before 2027, resolved via UMA oracle."
  - "Trump's offer to mediate and the Kremlin's positive characterization of the call are notable diplomatic signals, but the market prices them as far from decisive."
  - "A companion Polymarket contract (CM-EVT-S5MX1GCV08) puts only 10% on Ukraine agreeing not to join NATO before 2027, suggesting the market sees both a deal and a NATO concession as unlikely."
  - "The NATO summit context is reinforced by a separate Polymarket contract (CM-EVT-FD56H0NQ25) at 99% for Trump attending the NATO summit, with volume up 2,721% day over day, the summit is the proximate catalyst the market is watching."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump offered to help end the Ukraine war in a phone call with Putin, which the Kremlin described as businesslike and constructive ahead of the NATO summit."
    publisher: "AFP  and  Reuters"
    published_at: "2026-07-05T08:06:15.000Z"
    source_url: "https://www.aljazeera.com/news/2026/7/5/trump-offers-to-help-end-ukraine-war-in-long-call-with-putin-kremlin-says"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AFP  and  Reuters"
        source_url: "https://www.aljazeera.com/news/2026/7/5/trump-offers-to-help-end-ukraine-war-in-long-call-with-putin-kremlin-says"
        retrieved_at: "2026-07-05T10:07:52+00:00"
  - type: "pm_response"
    notes: "Polymarket binary contract resolving via UMA oracle; the 18% price reflects sustained skepticism that diplomatic rhetoric translates to a signed agreement within the horizon."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AFP  and  Reuters: Trump offers to help end Russia-Ukraine war in Putin call, Kremlin say"
    url: "https://www.aljazeera.com/news/2026/7/5/trump-offers-to-help-end-ukraine-war-in-long-call-with-putin-kremlin-says"
    published_at: "2026-07-05T08:06:15.000Z"
    retrieved_at: "2026-07-05T10:07:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
