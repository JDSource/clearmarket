---
signal_id: "CMSIG20260921VS00"
signal_slug: "will-the-republicans-win-the-ohio-senate-vol-65107"
headline: "Ohio Senate GOP win: 41% on $65K surge"
semantic_title: "Ohio Senate odds stay under 50% through heavy trading"
telemetry: "41% · $65K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-21T14:47:42+00:00"
event_id: "CM-EVT-53NPW6YWF1"
event_slug: "ohio-senate-election-winner"
event_question: "Will the winner of the Ohio Senate election be decided by DATE?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x771873c365f87bffd990644e4b688aebc1be7f18396d2eab64b996ff66e88669"
  question_raw: "Will the Republicans win the Ohio Senate race in 2026?"
  current_price: 0.41
  volume_24h_usd: 65107.88389
  volume_cumulative_usd: 242215.79234699995
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republicans as underdogs at 41%, implying Democrats hold a meaningful edge in Ohio."
  - "24h volume of $65K is 27% of all-time, making today one of the contract's most active sessions."
  - "Late-cycle Senate positioning likely driving fresh attention as 2026 midterm race sharpens."
  - "Resolves on the outcome of the Ohio 2026 U.S. Senate general election."
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
      poly_vol_24h_usd: 65107.88389
sources:
  - label: "ClearMarket market record: Will the winner of the Ohio Senate election be decided "
    url: "https://clearmarket.fyi/events/ohio-senate-election-winner"
    retrieved_at: "2026-09-21T14:47:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A significant one-day volume burst with odds still below 50% signals desks are actively re-pricing GOP prospects in Ohio rather than confirming a favorite.
