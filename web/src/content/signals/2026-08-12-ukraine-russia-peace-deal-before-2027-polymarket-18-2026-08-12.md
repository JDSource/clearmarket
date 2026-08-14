---
signal_id: "CMSIG2026081206"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-18-2026-08-12"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 18%"
semantic_title: "Ukraine-Russia peace deal before 2027 stays a long shot"
telemetry: "Polymarket 18%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-12T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.18
  volume_24h_usd: 2390.081108
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 18% on Ukraine signing a peace deal with Russia before 2027."
  - "Zelenskyy's Patriot request signals Ukraine is planning for continued fighting, consistent with the low peace-deal probability."
  - "A companion Polymarket contract (CM-EVT-S5MX1GCV08) prices 8% on Ukraine agreeing not to join NATO, a key Russian demand, showing core gaps remain wide."
  - "Resolves via UMA oracle; a signed, publicly announced peace agreement between Ukraine and Russia would be required to settle yes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukrainian President Volodymyr Zelenskyy asked the US to sell Ukraine 10% of its Patriot missile stock to destroy Russian ballistic missiles, signaling continued war footing."
    publisher: "Nick Paton Walsh, Natalie Wright, Daria Tarasova-Markina, Victoria Butenko"
    published_at: "2026-08-12T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/08/12/world/patriots-ukraine-zelensky-interview-cnn-latam-intl"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Nick Paton Walsh, Natalie Wright, Daria Tarasova-Markina, Victoria Butenko"
        source_url: "https://www.cnn.com/2026/08/12/world/patriots-ukraine-zelensky-interview-cnn-latam-intl"
        retrieved_at: "2026-08-14T09:03:59+00:00"
  - type: "pm_response"
    notes: "Polymarket at 18% treats a pre-2027 deal as a long shot, with related NATO and three-way summit contracts corroborating the bleak diplomatic picture."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Nick Paton Walsh, Natalie Wright, Daria Tarasova-Markina, Victoria Butenko: Sell Ukraine 10% of US Patriots and ‘we will destroy all the Russians’"
    url: "https://www.cnn.com/2026/08/12/world/patriots-ukraine-zelensky-interview-cnn-latam-intl"
    published_at: "2026-08-12T00:00:00.000Z"
    retrieved_at: "2026-08-14T09:03:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
