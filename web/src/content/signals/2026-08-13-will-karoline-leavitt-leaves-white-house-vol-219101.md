---
signal_id: "CMSIG20260813VS00"
signal_slug: "will-karoline-leavitt-leaves-white-house-vol-219101"
headline: "Leavitt WH exit: 99% on $219K volume surge"
semantic_title: "Leavitt exit before 2027 priced as near-certain"
telemetry: "99% · $219K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-13T09:08:38+00:00"
event_id: "CM-EVT-Z5Z4K6WBZ9"
event_slug: "kxtrumpadminleave-26dec31"
event_question: "Will someone leave their role in the Trump administration in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPADMINLEAVE-26DEC31-KLEA"
  question_raw: "Will Karoline Leavitt leaves White House Press Secretary in before 2027?"
  current_price: 0.992
  volume_24h_usd: 219101.15
  volume_cumulative_usd: 587237.21
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-07T15:00:00Z"
bullets:
  - "Kalshi prices a Leavitt departure before 2027 at 99%, the market treats it as resolved."
  - "37% of all-time volume, $219K, landed in 24 hours, an extraordinary late-stage concentration."
  - "Surge at near-ceiling odds suggests a known or imminent trigger is driving final-leg conviction."
  - "Resolves YES if she leaves the Press Secretary role before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 219101.15
sources:
  - label: "ClearMarket market record: Will someone leave their role in the Trump administrati"
    url: "https://clearmarket.fyi/events/kxtrumpadminleave-26dec31"
    retrieved_at: "2026-08-13T09:08:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 99% price absorbing 37% of lifetime volume in one session signals the desk that a confirming event may be publicly known or imminent, near-zero residual risk being priced out.
