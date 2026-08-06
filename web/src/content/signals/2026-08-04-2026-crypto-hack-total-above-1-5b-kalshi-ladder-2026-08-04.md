---
signal_id: "CMSIG2026080407"
signal_slug: "2026-crypto-hack-total-above-1-5b-kalshi-ladder-2026-08-04"
headline: "2026 crypto hack total above $1.5B: Kalshi ladder"
semantic_title: "Total 2026 crypto hack value odds favor $1.5B but short of $2B"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-04T00:00:00.000Z"
event_id: "CM-EVT-88PZ3D88F1"
event_slug: "total-crypto-hack-value-in-2026"
event_question: "Total 2026 crypto hack value"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x41a7dc4ce12ab8c4529c8e74023fac32b63404423867b789b49245635c0460b4"
  question_raw: "Over $2B crypto hack value in 2026?"
  current_price: 0.26
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Kalshi ladder prices 96% above $1.2B and 81% above $1.5B in total 2026 crypto hack value, but drops to only 26% above $2.0B."
  - "The Coldcard exploit, over $130M stolen with at least 15 attackers still active, is a major single-event contributor toward the $1.5B threshold, consistent with the 81% reading."
  - "The distribution's sharp drop from 81% at $1.5B to 26% at $2.0B shows the market views the Coldcard hack as material but unlikely alone to push the annual tally past $2.0B."
  - "The Bitcoin price ladder (CM-EVT-PFHRR5PCZ2) centers around $64,500-$65,000 for August 7, meaning the stolen BTC's dollar value is priced against a market not expecting a significant crash from the hack."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Hackers exploited a bug in Coldcard offline hardware wallets, stealing more than $130 million across multiple waves with at least 15 separate attackers identified."
    publisher: "Lorenzo Franceschi-Bicchierai"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Lorenzo Franceschi-Bicchierai"
        source_url: "https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/"
        retrieved_at: "2026-08-06T10:35:15+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Satoshi Index; the $1.5B-$2.0B corridor is the key zone of uncertainty with the Coldcard hack still actively ongoing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Lorenzo Franceschi-Bicchierai: Hackers steal over $130 million by exploiting bug in offline hardware"
    url: "https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-06T10:35:15+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
