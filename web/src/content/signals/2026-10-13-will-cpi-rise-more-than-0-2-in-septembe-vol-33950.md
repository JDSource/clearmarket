---
signal_id: "CMSIG20261013VS01"
signal_slug: "will-cpi-rise-more-than-0-2-in-septembe-vol-33950"
headline: "Sept CPI >0.2%: 99% on $34K pre-release surge"
semantic_title: "Traders pile into September CPI above 0.2% ahead of print"
telemetry: "99% · $34K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T07:49:07+00:00"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "Will CPI in September be above expectations?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.2"
  question_raw: "Will CPI rise more than 0.2% in September 2026?"
  current_price: 0.99
  volume_24h_usd: 33950.24
  volume_cumulative_usd: 62654.27
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "Kalshi contract sits at 99%, effectively treating a hotter-than-threshold September CPI as a done deal."
  - "24h volume of $34K is 54% of all-time, compressing lifetime activity into the pre-release window."
  - "September CPI release is imminent; last-minute positioning reflects consensus leaning well above the 0.2% bar."
  - "Resolves on the official BLS September 2026 CPI monthly change reading."
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
      kalshi_vol_24h_usd: 33950.24
sources:
  - label: "ClearMarket market record: Will CPI in September be above expectations?"
    url: "https://clearmarket.fyi/events/kxcpi-26sep"
    retrieved_at: "2026-10-13T07:49:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-unanimous pricing with a volume surge this close to the data drop tells a desk that the market has fully priced a beat of the threshold, any sub-0.2% print would be a significant shock.
