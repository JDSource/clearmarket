---
signal_id: "CMSIG20260903VS01"
signal_slug: "will-any-ai-model-have-a-score-of-at-lea-vol-30460"
headline: "AI 1520 score by Jan 1: 92% on $30K volume"
semantic_title: "AI Arena 1520 score by year-end stays a heavy favorite"
telemetry: "92% · $30K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-03T12:31:50+00:00"
event_id: "CM-EVT-0MCTG7XWR4"
event_slug: "kxaispike-27"
event_question: "Will there be significant AI capability growth this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAISPIKE-27B-1520"
  question_raw: "Will any AI model have a score of at least 1520 before Jan 1, 2027"
  current_price: 0.92
  volume_24h_usd: 30460.9
  volume_cumulative_usd: 45624.81
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices the milestone at 92%, market strongly expects at least one model to clear 1520 before 2027."
  - "24h volume of $30K equals 67% of all-time flow, an extraordinary single-session concentration."
  - "Fresh model releases or benchmark announcements in late 2026 appear to be drawing capital to this contract."
  - "Resolves if any AI model posts a 1520 Overall Arena Score before January 1, 2027."
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
      kalshi_vol_24h_usd: 30460.9
sources:
  - label: "ClearMarket market record: Will there be significant AI capability growth this yea"
    url: "https://clearmarket.fyi/events/kxaispike-27"
    retrieved_at: "2026-09-03T12:31:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Two-thirds of lifetime volume landing in one session at 92% suggests a specific model release or benchmark update is imminent, prompting desks to take firm positions before resolution.
