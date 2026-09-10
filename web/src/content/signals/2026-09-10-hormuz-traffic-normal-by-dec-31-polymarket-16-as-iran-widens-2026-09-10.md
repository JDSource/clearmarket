---
signal_id: "CMSIG2026091006"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-16-as-iran-widens-2026-09-10"
headline: "Hormuz traffic normal by Dec 31: Polymarket 16% as Iran widens strikes"
semantic_title: "Strait of Hormuz back to normal by year-end stays a long shot"
telemetry: "Polymarket 16%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-10T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.16
  volume_24h_usd: 287377.531145
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 sits at 16%, resolving via UMA oracle."
  - "Iran's decision to widen its maritime no-go zone beyond Hormuz is consistent with the 16% pricing: the market was already treating a year-end resolution as unlikely, and the escalation does nothing to improve those odds."
  - "A companion story shows Iran and the US exchanging tanker strikes in the Gulf of Oman in the largest maritime attack wave since the conflict began, reinforcing the low-probability read on a near-term normalization."
  - "Trump separately said the Iran war would end after the US midterms, a political timeline not yet priced into the Hormuz contract, which would require cessation of hostilities within roughly three months."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran struck ships and widened its maritime exclusion zone beyond the Strait of Hormuz, with the US and Iran exchanging tanker attacks in what was described as the biggest wave of shipping attacks since the conflict began."
    publisher: "malaymail.com"
    published_at: "2026-09-10T00:00:00.000Z"
    source_url: "https://www.malaymail.com/news/world/2026/09/10/iran-strikes-ships-widens-maritime-no-go-zone-beyond-hormuz/234617"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "malaymail.com"
        source_url: "https://www.malaymail.com/news/world/2026/09/10/iran-strikes-ships-widens-maritime-no-go-zone-beyond-hormuz/234617"
        retrieved_at: "2026-09-10T12:39:52+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on whether commercial Strait of Hormuz traffic returns to normal by December 31, 2026; Iran's zone-widening escalation is the key resolution risk."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "malaymail.com: Iran strikes ships, widens maritime no-go zone beyond Hormuz | Malay M"
    url: "https://www.malaymail.com/news/world/2026/09/10/iran-strikes-ships-widens-maritime-no-go-zone-beyond-hormuz/234617"
    published_at: "2026-09-10T00:00:00.000Z"
    retrieved_at: "2026-09-10T12:39:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
