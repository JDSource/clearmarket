---
signal_id: "CMSIG2026092102"
signal_slug: "iran-ends-enrichment-by-dec-31-polymarket-12-2026-09-21"
headline: "Iran ends enrichment by Dec 31: Polymarket 12%"
semantic_title: "Iran uranium enrichment deal stays a long shot at 12 percent"
telemetry: "Polymarket 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-21T00:00:00.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end enrichment of uranium by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.12
  volume_24h_usd: 1305.77
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices just 12% on Iran agreeing to end uranium enrichment by December 31, 2026, keeping this a heavy long shot despite intense diplomatic pressure."
  - "Trading volume on this contract surged 3,167% day over day, signaling a large spike in fresh attention as Trump-Iran rhetoric escalated sharply over the weekend."
  - "A companion Polymarket contract on the Iranian regime falling before 2027 sits at only 6%, suggesting markets do not expect military action to produce regime change."
  - "Resolution requires a verified Iranian agreement to halt enrichment; the gap between heated rhetoric and the 12% price reflects deep market skepticism that threats translate to a deal."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump threatened to destroy Iran's economy or eliminate its leadership ahead of UN General Assembly talks, as Tehran vowed painful retaliation."
    publisher: "independent.co.uk"
    published_at: "2026-09-21T00:00:00.000Z"
    source_url: "https://www.independent.co.uk/news/world/middle-east/iran-us-war-live-trump-strikes-update-oil-houthis-riyadh-b3053306.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "independent.co.uk"
        source_url: "https://www.independent.co.uk/news/world/middle-east/iran-us-war-live-trump-strikes-update-oil-houthis-riyadh-b3053306.html"
        retrieved_at: "2026-09-21T07:47:18+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the volume surge confirms new capital entering on the Iran escalation news, though the headline probability remains low."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "independent.co.uk: Iran-US war live: Trump threatens to ‘blow the entire nation up’ after"
    url: "https://www.independent.co.uk/news/world/middle-east/iran-us-war-live-trump-strikes-update-oil-houthis-riyadh-b3053306.html"
    published_at: "2026-09-21T00:00:00.000Z"
    retrieved_at: "2026-09-21T07:47:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
