---
signal_id: "CMSIG20261028VS06"
signal_slug: "will-goldman-sachs-serve-as-lead-left-un-vol-14175"
headline: "Goldman leads Anthropic IPO: 95% on $14.2K surge"
semantic_title: "Goldman Sachs near-locks Anthropic IPO lead role at 95% on Kalshi"
telemetry: "95% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T07:50:03+00:00"
event_id: "CM-EVT-G8Q9093H77"
event_slug: "kxanthropicleadleft-28jan01b"
event_question: "Which bank will lead Anthropic's initial public offering?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXANTHROPICLEADLEFT-28JAN01B-GSX"
  question_raw: "Will Goldman Sachs serve as lead-left underwriter on Anthropic's IPO?"
  current_price: 0.95
  volume_24h_usd: 14175.57
  volume_cumulative_usd: 35517.82
  arbitration_model: "kalshi_staff"
  resolves_at: "2028-01-01T15:00:00Z"
bullets:
  - "95% pricing reflects a near-certain market conviction that Goldman Sachs runs the Anthropic IPO book."
  - "Kalshi logged $14.2K in 24h, 40% of all-time volume, sharpening an already high-confidence contract."
  - "Fresh volume at 95% suggests new information or leak-adjacent positioning rather than speculative opening."
  - "Resolves on public confirmation of lead-left underwriter in Anthropic's IPO filing."
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
      kalshi_vol_24h_usd: 14175.57
sources:
  - label: "ClearMarket market record: Which bank will lead Anthropic's initial public offerin"
    url: "https://clearmarket.fyi/events/kxanthropicleadleft-28jan01b"
    retrieved_at: "2026-10-28T07:50:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 40% all-time volume surge pushing against a 95% ceiling signals that the market believes the Goldman mandate is effectively confirmed, ECM desks and competing banks should treat this as near-public information.
