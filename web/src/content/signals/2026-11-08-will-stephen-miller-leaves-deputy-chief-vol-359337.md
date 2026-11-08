---
signal_id: "CMSIG20261108VS00"
signal_slug: "will-stephen-miller-leaves-deputy-chief-vol-359337"
headline: "Miller Deputy CoS exit: 97% NO on $359K surge"
semantic_title: "Traders back Miller staying as Deputy Chief through 2026"
telemetry: "97% · $359K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-08T07:48:33+00:00"
event_id: "CM-EVT-Z5Z4K6WBZ9"
event_slug: "kxtrumpadminleave-26dec31"
event_question: "Will someone leave their role in the Trump administration in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPADMINLEAVE-26DEC31-SMIL"
  question_raw: "Will Stephen Miller leaves Deputy Chief of Staff in before 2027?"
  current_price: 0.966
  volume_24h_usd: 359337.19
  volume_cumulative_usd: 938064.16
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-07T15:00:00Z"
bullets:
  - "97% NO implies market sees near-zero chance Miller departs the role before Jan 1, 2027."
  - "Kalshi logged $359K in 24h, 38% of the contract's entire all-time volume in a single session."
  - "Fresh activity likely triggered by circulation of West Wing personnel rumors; market is pricing them out hard."
  - "Contract resolves YES if Miller leaves the position before 2027, NO otherwise."
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
      kalshi_vol_24h_usd: 359337.19
sources:
  - label: "ClearMarket market record: Will someone leave their role in the Trump administrati"
    url: "https://clearmarket.fyi/events/kxtrumpadminleave-26dec31"
    retrieved_at: "2026-11-08T07:48:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The lopsided 97% NO with heavy single-day volume signals desks are actively fading a personnel-change rumor rather than pricing in genuine departure risk, worth monitoring for a catalyst that shifts that conviction.
