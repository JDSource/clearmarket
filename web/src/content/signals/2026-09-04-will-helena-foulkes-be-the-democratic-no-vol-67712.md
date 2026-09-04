---
signal_id: "CMSIG20260904VS00"
signal_slug: "will-helena-foulkes-be-the-democratic-no-vol-67712"
headline: "Foulkes RI Gov nomination: 99% on $67K surge"
semantic_title: "Foulkes RI Democratic nomination priced as a certainty"
telemetry: "99% · $68K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-04T12:29:08+00:00"
event_id: "CM-EVT-ZVCJ160PY0"
event_slug: "kxgovrinomd-26"
event_question: "Will Rhode Island have a Democratic Governor nominee by September 8, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVRINOMD-26-HFOU"
  question_raw: "Will Helena Foulkes be the Democratic nominee for Governor in Rhode Island?"
  current_price: 0.986
  volume_24h_usd: 67712.88
  volume_cumulative_usd: 96499.17
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T14:00:00Z"
bullets:
  - "Kalshi prices Foulkes at 99%, market treats the Democratic nomination as resolved."
  - "$67K traded in 24h, equal to 70% of all-time volume, signaling a decisive late rush."
  - "Surge likely follows a filing deadline, poll, or rival withdrawal collapsing any residual doubt."
  - "Contract resolves on the outcome of the Rhode Island Democratic gubernatorial primary."
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
      kalshi_vol_24h_usd: 67712.88
sources:
  - label: "ClearMarket market record: Will Rhode Island have a Democratic Governor nominee by"
    url: "https://clearmarket.fyi/events/kxgovrinomd-26"
    retrieved_at: "2026-09-04T12:29:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-total consensus at 99% with 70% of all-time volume printing in one session tells a desk the nomination question is effectively closed, any remaining spread is noise, not signal.
