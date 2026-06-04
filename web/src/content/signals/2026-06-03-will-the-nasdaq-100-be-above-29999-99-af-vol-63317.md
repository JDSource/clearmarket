---
signal_id: "CMSIG20260603VS07"
signal_slug: "will-the-nasdaq-100-be-above-29999-99-af-vol-63317"
headline: "Nasdaq-100 above 30K before Dec 31: 99% on $63K"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-03T01:46:55+00:00"
event_id: "CM-EVT-HYFSJ2CNW7"
event_slug: "kxnasdaq100maxy-26dec31h1600"
event_question: "Will the Nasdaq-100 reach a new all-time high by the end of 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXNASDAQ100MAXY-26DEC31H1600-T29999.99"
  question_raw: "Will the Nasdaq-100 be above 29999.99 after issuance and before Dec 31, 2026 at 4pm EST?"
  current_price: 0.989
  volume_24h_usd: 63317.96
  volume_cumulative_usd: 102356.32
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-31T21:00:00Z"
bullets:
  - "Kalshi consensus at 99%, market treats NDX breaching 30K by year-end as near-certain."
  - "$63K in 24h is 62% of all-time volume; contract likely newly issued and filling initial liquidity."
  - "NDX currently near or above threshold; contract may reflect recent index level confirmation."
  - "Resolves December 31, 2026; tail risk priced at 1%."
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
      kalshi_vol_24h_usd: 63317.96
sources:
  - label: "ClearMarket market record: Will the Nasdaq-100 reach a new all-time high by the en"
    url: "https://clearmarket.fyi/events/kxnasdaq100maxy-26dec31h1600"
    retrieved_at: "2026-06-03T01:46:55+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

New-issuance contract with majority of lifetime volume in day one at 99% suggests institutional participants are using Kalshi to express high-conviction NDX constructive views, equity desks can monitor for drift if macro conditions deteriorate.
