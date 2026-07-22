---
signal_id: "CMSIG2026072204"
signal_slug: "iran-ends-enrichment-by-dec-31-polymarket-22-2026-07-22"
headline: "Iran ends enrichment by Dec 31: Polymarket 22%"
semantic_title: "Iran uranium enrichment halt by year-end stays a long shot"
telemetry: "Polymarket 22%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-22T00:00:00.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end enrichment of uranium by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.22
  volume_24h_usd: 244.061817
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 22% on Iran agreeing to end uranium enrichment by December 31."
  - "Trump's nuclear-site threats and disclosed war costs signal escalation, not negotiation, keeping enrichment-halt odds well below 50%."
  - "The Kalshi contract on the US reopening its embassy in Iran sits at only 7%, reinforcing how far markets are from pricing diplomatic normalization."
  - "Resolves via UMA oracle; the question turns on a formal Iranian government commitment, not a temporary halt."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump threatened to attack Iran's Pickaxe Mountain nuclear site as Secretary of Defense Pete Hegseth disclosed the staggering human and financial cost of five months of US-Iran war."
    publisher: "independent.co.uk"
    published_at: "2026-07-22T00:00:00.000Z"
    source_url: "https://www.independent.co.uk/news/world/middle-east/iran-us-war-live-trump-pickaxe-mountain-hegseth-hormuz-b3019215.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "independent.co.uk"
        source_url: "https://www.independent.co.uk/news/world/middle-east/iran-us-war-live-trump-pickaxe-mountain-hegseth-hormuz-b3019215.html"
        retrieved_at: "2026-07-22T10:22:09+00:00"
  - type: "pm_response"
    notes: "Polymarket at 22% on enrichment ending by year-end is consistent with Rubio's public assessment that Iran is not serious about talks."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "independent.co.uk: Iran-US war updates: Trump threatens to attack nuclear site as Hegseth"
    url: "https://www.independent.co.uk/news/world/middle-east/iran-us-war-live-trump-pickaxe-mountain-hegseth-hormuz-b3019215.html"
    published_at: "2026-07-22T00:00:00.000Z"
    retrieved_at: "2026-07-22T10:22:09+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
