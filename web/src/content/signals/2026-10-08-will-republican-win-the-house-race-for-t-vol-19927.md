---
signal_id: "CMSIG20261008VS02"
signal_slug: "will-republican-win-the-house-race-for-t-vol-19927"
headline: "TX-35 GOP win: 40% on $20K volume"
semantic_title: "TX-35 House race draws heavy trading at a live 40% Republican price"
telemetry: "40% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-08T15:10:56+00:00"
event_id: "CM-EVT-30RGTM2V02"
event_slug: "kxhousetx35-26"
event_question: "Will there be a winner determined in the TX-35 House race by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSETX35-26-R"
  question_raw: "Will Republican win the House race for TX-35?"
  current_price: 0.4
  volume_24h_usd: 19927.92
  volume_cumulative_usd: 33274.58
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Republican priced at 40%, genuinely competitive, market sees this as a contested battleground."
  - "24h volume of $20K is 60% of all-time, indicating strong new-money conviction entering the contract."
  - "TX-35 is a majority-minority district; fresh volume may trail candidate filing news or internal poll leaks."
  - "Resolves on November 2026 general election for TX-35."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 19927.92
sources:
  - label: "ClearMarket market record: Will there be a winner determined in the TX-35 House ra"
    url: "https://clearmarket.fyi/events/kxhousetx35-26"
    retrieved_at: "2026-10-08T15:10:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 40% Republican odds and 60% of all-time volume in one session, TX-35 is being actively repriced as a genuine toss-up worth hedging by any desk tracking House majority math.
