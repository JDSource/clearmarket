---
signal_id: "CMSIG2026090708"
signal_slug: "over-2b-crypto-hacked-in-2026-polymarket-89-2026-09-07"
headline: "Over $2B crypto hacked in 2026: Polymarket 89%"
semantic_title: "Total 2026 crypto hack value above $2B stays heavily favored"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-07T03:37:00.000Z"
event_id: "CM-EVT-88PZ3D88F1"
event_slug: "total-crypto-hack-value-in-2026"
event_question: "Total 2026 crypto hack value (USD)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x86603700e75c78c377b49db69bf73af53ee56c0b64f7cbd7282683e01ee97393"
  question_raw: "Over $2.5B crypto hack value in 2026?"
  current_price: 0.27
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Prediction market ladder prices 89% odds that total 2026 crypto hack value exceeds $2 billion, with only 27% above $2.5 billion."
  - "The $405 million Liquid Network exploit, net of the $270 million returned, adds materially to the 2026 running total and is consistent with the above-$2B consensus."
  - "The sharp drop from 89% at $2B to 27% at $2.5B and just 5% at $3B reveals the market does not expect a single catastrophic event to push totals far above the threshold."
  - "Resolution tracks cumulative reported crypto hack losses for calendar year 2026; partial recoveries like the Liquid white-hat return complicate gross versus net accounting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A $405 million exploit hit the Liquid Bitcoin network, with white-hat actors later returning approximately 85% of the stolen funds."
    publisher: "straitstimes.com"
    published_at: "2026-09-07T03:37:00.000Z"
    source_url: "https://www.straitstimes.com/business/bitcoin-network-says-405-million-stolen-in-latest-crypto-hack"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "straitstimes.com"
        source_url: "https://www.straitstimes.com/business/bitcoin-network-says-405-million-stolen-in-latest-crypto-hack"
        retrieved_at: "2026-09-09T12:40:02+00:00"
  - type: "pm_response"
    notes: "The ladder distribution implies the $2B threshold is near-certain but the $2.5B level remains a minority scenario, signaling market confidence that hack pace is elevated but not runaway."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "straitstimes.com: Bitcoin network says $405 million stolen in latest crypto hack | The S"
    url: "https://www.straitstimes.com/business/bitcoin-network-says-405-million-stolen-in-latest-crypto-hack"
    published_at: "2026-09-07T03:37:00.000Z"
    retrieved_at: "2026-09-09T12:40:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
