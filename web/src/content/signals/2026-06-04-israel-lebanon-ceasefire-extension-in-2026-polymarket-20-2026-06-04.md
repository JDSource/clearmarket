---
signal_id: "CMSIG2026060408"
signal_slug: "israel-lebanon-ceasefire-extension-in-2026-polymarket-20-2026-06-04"
headline: "Israel-Lebanon ceasefire extension in 2026: Polymarket 20%"
semantic_title: "Lebanon ceasefire extension announcement wavers at low odds"
telemetry: "Polymarket 20%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-04T13:27:25.000Z"
event_id: "CM-EVT-KFM6RVW5P7"
event_slug: "israel-announces-lebanon-ceasefire-extension-by"
event_question: "Israel announces Lebanon ceasefire extension in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x42973552f8bcfc9269fba8492766f2c20a22243cbba154cf695acaff88ec96c7"
  question_raw: "Israel announces Lebanon ceasefire extension by June 7?"
  current_price: 0.2
  volume_24h_usd: 44425.682103000014
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-07T00:00:00Z"
bullets:
  - "Polymarket prices 20% odds Israel formally announces a Lebanon ceasefire extension in 2026, resolving via UMA oracle."
  - "Hezbollah's rejection of the deal is consistent with the low probability: the plan requires Hezbollah compliance but the group holds veto power in practice."
  - "A companion Polymarket contract on Israeli forces entering Nabatieh by June 7 sits at 19% (CM-EVT-19YC0MGZP4), suggesting markets see continued military operations as slightly more likely than a ceasefire deal near-term."
  - "Israel-Lebanon normalization before 2027 sits at just 25% on Polymarket (CM-EVT-5TKXRL9KJ8), reflecting the same structural skepticism about durable resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Hezbollah leader Naim Qassem rejected the Israel-Lebanon ceasefire plan as 'shameful,' casting doubt on the US-brokered deal that Israel and the Lebanese government had agreed to."
    publisher: "middleeasteye.net"
    published_at: "2026-06-04T13:27:25.000Z"
    source_url: "https://www.middleeasteye.net/news/lebanon-israel-ceasefire-plan-doubt-hezbollah-rejection"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "middleeasteye.net"
        source_url: "https://www.middleeasteye.net/news/lebanon-israel-ceasefire-plan-doubt-hezbollah-rejection"
        retrieved_at: "2026-06-05T11:24:05+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on an official Israeli ceasefire extension announcement; Hezbollah's non-state status creates ambiguity in what counts as a qualifying agreement."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "middleeasteye.net: Lebanon-Israel ceasefire plans in doubt following Hezbollah's rejectio"
    url: "https://www.middleeasteye.net/news/lebanon-israel-ceasefire-plan-doubt-hezbollah-rejection"
    published_at: "2026-06-04T13:27:25.000Z"
    retrieved_at: "2026-06-05T11:24:05+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
