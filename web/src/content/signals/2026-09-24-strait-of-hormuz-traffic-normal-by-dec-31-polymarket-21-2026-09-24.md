---
signal_id: "CMSIG2026092408"
signal_slug: "strait-of-hormuz-traffic-normal-by-dec-31-polymarket-21-2026-09-24"
headline: "Strait of Hormuz traffic normal by Dec 31: Polymarket 21%"
semantic_title: "Hormuz traffic returning to normal by year-end stays a long shot"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-24T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.21
  volume_24h_usd: 157821.07870800002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 21% on Strait of Hormuz traffic returning to normal by December 31, 2026, a long-shot probability."
  - "EU pressure on Iran to restore navigation is a new diplomatic signal, but the 21% Polymarket probability shows markets see a year-end resolution as unlikely."
  - "US-Iran talks described as 'still far apart' (Story 23) and Iran's vow of no surrender are consistent with the low Polymarket probability of a near-term Hormuz reopening."
  - "A companion Polymarket contract (CM-EVT-4CKJ2D3T77) prices only 12% on Iran ending uranium enrichment by December 31, confirming the market sees comprehensive Iran deal resolution as deeply unlikely in 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The EU urged Iran to halt strikes on neighbors and restore freedom of navigation in the Strait of Hormuz during talks with Iranian President Pezeshkian at the UN General Assembly."
    publisher: "iranintl.com"
    published_at: "2026-09-24T00:00:00.000Z"
    source_url: "https://www.iranintl.com/en/202609246695"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "iranintl.com"
        source_url: "https://www.iranintl.com/en/202609246695"
        retrieved_at: "2026-09-24T07:47:37+00:00"
  - type: "pm_response"
    notes: "Polymarket binary at 21%; EU diplomatic pressure is noted but the market remains firmly in the 'no resolution by year-end' camp on Hormuz traffic normalization."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "iranintl.com: EU urges Iran to halt strikes on neighbors, restore Hormuz navigation"
    url: "https://www.iranintl.com/en/202609246695"
    published_at: "2026-09-24T00:00:00.000Z"
    retrieved_at: "2026-09-24T07:47:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
