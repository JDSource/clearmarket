---
signal_id: "CMSIG20261004VS05"
signal_slug: "will-luiz-in-cio-lula-da-silva-win-the-f-vol-54157"
headline: "Lula first-round alt contract: 53% on $54K"
semantic_title: "Lula first-round odds sit at 53% in separate contract"
telemetry: "53% · $54K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T07:48:35+00:00"
event_id: "CM-EVT-2NF81BZ4K5"
event_slug: "brazil-presidential-election-first-round-margin-of-victory"
event_question: "Will the margin of victory in Brazil's presidential election first round be less than 5 percentage points?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5d5b8feb963ddcc0f4688f7ac0c0d375f99945b7a07155d60cd1a306c6b3054b"
  question_raw: "Will Luiz Inácio Lula da Silva win the first round of the 2026 Brazilian presidential election by less than 5%?"
  current_price: 0.53
  volume_24h_usd: 54157.588472
  volume_cumulative_usd: 199285.66697000002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "A parallel Polymarket contract prices Lula's first-round win at 53%, sharply diverging from the 9% contract (Spike 1)."
  - "27% of all-time volume transacted in 24h, indicating active two-sided trading on this alternative framing."
  - "The pricing gap between contracts suggests different resolution criteria or a market inefficiency drawing arbitrage flow."
  - "Resolves on Brazil's 2026 first-round election result."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 54157.588472
sources:
  - label: "ClearMarket market record: Will the margin of victory in Brazil's presidential ele"
    url: "https://clearmarket.fyi/events/brazil-presidential-election-first-round-margin-of-victory"
    retrieved_at: "2026-10-04T07:48:35+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 44-point gap between two Lula first-round contracts on the same venue is a red flag for desks, differing resolution language is likely the driver, and this spread represents an arbitrage worth investigating.
