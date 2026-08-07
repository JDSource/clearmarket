---
signal_id: "CMSIG2026080408"
signal_slug: "2026-crypto-hack-total-above-1-5b-ladder-76-2026-08-04"
headline: "2026 crypto hack total above $1.5B: ladder 76%"
semantic_title: "Total 2026 crypto hack value favored above $1.5B"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-04T00:00:00.000Z"
event_id: "CM-EVT-88PZ3D88F1"
event_slug: "total-crypto-hack-value-in-2026"
event_question: "Total 2026 crypto hack value (USD)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x41a7dc4ce12ab8c4529c8e74023fac32b63404423867b789b49245635c0460b4"
  question_raw: "Over $2B crypto hack value in 2026?"
  current_price: 0.26
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Prediction market ladder prices 76% odds that total 2026 crypto hack value exceeds $1.5 billion, with 26% above $2.0 billion."
  - "The Coldcard breach, confirmed above $130 million and still ongoing at time of reporting, adds directly to the running 2026 total that the ladder is pricing."
  - "Trading volume on a related contract (CM-EVT-PQDW14N7X2) surged 2,865% day over day, a measured signal that the Coldcard hack is drawing significant fresh attention to crypto-security markets."
  - "At 96% above $1.2 billion, the ladder already treats the lower threshold as near-certain; the question is whether the Coldcard losses plus prior hacks push the total through $2.0 billion by year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Hackers stole over $130 million by exploiting a firmware bug in Coldcard hardware wallets, with at least 15 attackers involved and the exploit still live."
    publisher: "Lorenzo Franceschi-Bicchierai"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Lorenzo Franceschi-Bicchierai"
        source_url: "https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/"
        retrieved_at: "2026-08-07T08:53:43+00:00"
  - type: "pm_response"
    notes: "Ladder pricing from prediction market strikes; resolution methodology unspecified but tracks aggregate reported hack values across 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Lorenzo Franceschi-Bicchierai: Hackers steal over $130 million by exploiting bug in offline hardware"
    url: "https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-07T08:53:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
