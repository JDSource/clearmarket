---
signal_id: "CMSIG2026100806"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-18-2026-10-08"
headline: "Hormuz traffic normal by Dec 31: Polymarket 18%"
semantic_title: "Strait of Hormuz reopening by year-end stays a long shot"
telemetry: "Polymarket 18%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-08T03:15:10.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.18
  volume_24h_usd: 64510.304863
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by December 31 at just 18%, a clear long-shot assessment."
  - "Active tanker attacks off Qatar and Iran's declared closure intent are consistent with this low probability; the Iran-Oman route agreement is not yet shifting the market."
  - "Brent crude above 100 dollars reported alongside the Hormuz disruption is the cross-market read confirming traders treat closure risk as real."
  - "Polymarket resolves via UMA oracle; 'normal traffic' definition will be the key settlement edge, partial resumption may not qualify."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A tanker was attacked off Qatar as Iran claimed the Hormuz shipping route would be closed, even as an Iran-Oman framework on routes was reported."
    publisher: "Mark Saunokonoko"
    published_at: "2026-10-08T03:15:10.000Z"
    source_url: "https://www.theguardian.com/world/2026/oct/08/tanker-attacked-qatar-coast-strait-of-hormuz-iran-oil-price"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Mark Saunokonoko"
        source_url: "https://www.theguardian.com/world/2026/oct/08/tanker-attacked-qatar-coast-strait-of-hormuz-iran-oil-price"
        retrieved_at: "2026-10-08T07:48:09+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 18%; pricing is broadly consistent with the tanker attack and Iran closure rhetoric dominating the Iran-Oman diplomatic signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Mark Saunokonoko: Tanker attacked off Qatar as Iran claims route transporting oil throug"
    url: "https://www.theguardian.com/world/2026/oct/08/tanker-attacked-qatar-coast-strait-of-hormuz-iran-oil-price"
    published_at: "2026-10-08T03:15:10.000Z"
    retrieved_at: "2026-10-08T07:48:09+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
