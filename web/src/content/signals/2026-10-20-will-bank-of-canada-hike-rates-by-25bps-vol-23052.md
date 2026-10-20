---
signal_id: "CMSIG20261020VS03"
signal_slug: "will-bank-of-canada-hike-rates-by-25bps-vol-23052"
headline: "BoC +25bps Oct 2026: 67% on $23K fresh volume"
semantic_title: "Bank of Canada October hike stays favored through a volume surge"
telemetry: "67% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-20T13:16:06+00:00"
event_id: "CM-EVT-RCX0GXDHW8"
event_slug: "kxcbdecisioncanada-26oct"
event_question: "Will the Bank of Canada make a decision in October 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCBDECISIONCANADA-26OCT-H25"
  question_raw: "Will Bank of Canada Hike rates by 25bps at their October 2026 meeting?"
  current_price: 0.67
  volume_24h_usd: 23052.36
  volume_cumulative_usd: 82956.16
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-28T13:29:00Z"
bullets:
  - "Kalshi prices a 67% probability of a Bank of Canada 25bps hike at the October 2026 meeting, a clear lean toward action."
  - "24h volume of $23K is 28% of all-time handle, a meaningful but measured increase consistent with pre-meeting positioning."
  - "Fresh volume likely follows a Canadian CPI print, employment data, or hawkish BoC communication sharpening the near-term rate path."
  - "Resolves at the October 2026 BoC policy decision; 67% implies markets see a hike as the base case but not a certainty."
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
      kalshi_vol_24h_usd: 23052.36
sources:
  - label: "ClearMarket market record: Will the Bank of Canada make a decision in October 2026"
    url: "https://clearmarket.fyi/events/kxcbdecisioncanada-26oct"
    retrieved_at: "2026-10-20T13:16:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Two-thirds odds on a live central bank hike with fresh positioning flow is a direct macro signal, rates desks should treat this as real-time confirmation that the market is leaning toward BoC action in October.
