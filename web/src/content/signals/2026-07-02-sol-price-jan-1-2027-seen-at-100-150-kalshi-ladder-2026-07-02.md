---
signal_id: "CMSIG2026070208"
signal_slug: "sol-price-jan-1-2027-seen-at-100-150-kalshi-ladder-2026-07-02"
headline: "SOL price Jan 1, 2027 seen at $100-$150: Kalshi ladder"
semantic_title: "Solana end-2026 price consensus anchors in the 100 to 150 dollar range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-02T05:22:54.000Z"
event_id: "CM-EVT-24BW6LVF51"
event_slug: "kxsold26-27jan0100"
event_question: "SOL price on January 1, 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSOLD26-27JAN0100-T149.99"
  question_raw: "SOL price  on Jan 1, 2027?"
  current_price: 0.26
  volume_24h_usd: 9.51
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-01T05:05:00Z"
bullets:
  - "Kalshi ladder prices 50% above $100 but only 26% above $150, placing the market-implied SOL year-end price in the $100-$150 range."
  - "Solana's roughly 16% weekly gain is consistent with the distribution leaning toward the lower half of the $100-$150 band rather than higher strikes."
  - "A separate Kalshi contract puts just 2% on Solana ending 2026 above $500, confirming the ladder's sharp drop-off above $150 as the consensus view."
  - "Resolves via CF Benchmarks price feed on January 1, 2027; the settlement uses the CF Benchmarks reference rate, not spot exchange prices."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin climbed back above $60,000 after Fed Chair Warsh said inflation risks had declined, with Solana leading major cryptocurrencies up roughly 16% on the week."
    publisher: "coindesk.com"
    published_at: "2026-07-02T05:22:54.000Z"
    source_url: "https://www.coindesk.com/markets/2026/07/02/ether-solana-dogecoin-in-the-green-after-warsh-comments-push-bitcoin-above-usd60-000"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/markets/2026/07/02/ether-solana-dogecoin-in-the-green-after-warsh-comments-push-bitcoin-above-usd60-000"
        retrieved_at: "2026-07-02T10:34:14+00:00"
  - type: "pm_response"
    notes: "Kalshi's SOL ladder shows the market anchoring year-end expectations well below the $200 strikes despite the Warsh-driven crypto rally."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: Ether, solana, dogecoin in the green after Warsh comments push bitcoin"
    url: "https://www.coindesk.com/markets/2026/07/02/ether-solana-dogecoin-in-the-green-after-warsh-comments-push-bitcoin-above-usd60-000"
    published_at: "2026-07-02T05:22:54.000Z"
    retrieved_at: "2026-07-02T10:34:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
