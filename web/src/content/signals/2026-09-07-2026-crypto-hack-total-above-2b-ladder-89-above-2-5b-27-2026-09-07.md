---
signal_id: "CMSIG2026090708"
signal_slug: "2026-crypto-hack-total-above-2b-ladder-89-above-2-5b-27-2026-09-07"
headline: "2026 crypto hack total above $2B: ladder 89%, above $2.5B: 27%"
semantic_title: "Total 2026 crypto hack value seen between $2B and $2.5B"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-07T00:00:00.000Z"
event_id: "CM-EVT-88PZ3D88F1"
event_slug: "total-crypto-hack-value-in-2026"
event_question: "Total 2026 crypto hack value (USD)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x86603700e75c78c377b49db69bf73af53ee56c0b64f7cbd7282683e01ee97393"
  question_raw: "Over $2.5B crypto hack value in 2026?"
  current_price: 0.27
  volume_24h_usd: 20.44
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Ladder prices total 2026 crypto hack value at 89% above $2.0B but only 27% above $2.5B, implying the market-implied range is $2.0-2.5B."
  - "The Liquid Network incident alone, at $320-405 million, is a material addition to the 2026 running total and is consistent with the above-$2.0B pricing."
  - "The sharp drop from 89% to 27% between the $2.0B and $2.5B strikes shows the market does not expect additional large hacks to push the total dramatically higher this year."
  - "Resolution depends on aggregated hack-value tallies across the full calendar year 2026; the Coldcard third-wave attacker (Story 34) is a separate incident adding further to the running total."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A hack on Liquid Network, a Bitcoin-linked sidechain, resulted in approximately $320-405 million in BTC withdrawn, adding to a string of major 2026 crypto security incidents."
    publisher: "straitstimes.com"
    published_at: "2026-09-07T00:00:00.000Z"
    source_url: "https://www.straitstimes.com/business/bitcoin-network-says-405-million-stolen-in-latest-crypto-hack"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "straitstimes.com"
        source_url: "https://www.straitstimes.com/business/bitcoin-network-says-405-million-stolen-in-latest-crypto-hack"
        retrieved_at: "2026-09-07T13:54:18+00:00"
  - type: "pm_response"
    notes: "This ladder covers cumulative 2026 hack value; the Liquid Network incident and Coldcard attacks are among the inputs that will determine resolution against the $2.0B and $2.5B strike levels."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "straitstimes.com: Bitcoin network says $405 million stolen in latest crypto hack | The S"
    url: "https://www.straitstimes.com/business/bitcoin-network-says-405-million-stolen-in-latest-crypto-hack"
    published_at: "2026-09-07T00:00:00.000Z"
    retrieved_at: "2026-09-07T13:54:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
