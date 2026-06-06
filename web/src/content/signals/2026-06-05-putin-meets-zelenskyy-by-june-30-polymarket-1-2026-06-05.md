---
signal_id: "CMSIG2026060503"
signal_slug: "putin-meets-zelenskyy-by-june-30-polymarket-1-2026-06-05"
headline: "Putin meets Zelenskyy by June 30: Polymarket 1%"
semantic_title: "Putin-Zelenskyy summit by June 30 wavers near zero pricing"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-05T18:04:27.000Z"
event_id: "CM-EVT-2DR1P4YZ13"
event_slug: "will-putin-meet-with-zelenskyy-by-june-30-2026"
event_question: "Will Putin meet with Zelenskyy by June 30, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc5ab3fb332af0bebf7ed6df1b1d5e1cc32a91e960c57d7602a5224830cf0084b"
  question_raw: "Will Putin meet with Zelenskyy by June 30, 2026?"
  current_price: 0.011
  volume_24h_usd: 535.846363
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices only 1% on Putin meeting Zelenskyy by June 30, effectively treating the event as ruled out."
  - "Putin's open-letter rejection of Zelenskyy's direct-talks proposal is fully consistent with this near-zero probability."
  - "The longer-horizon Polymarket contract on a Ukraine-Russia ceasefire by December 31, 2026 sits at 49%, showing the market sees a longer timeline as possible even as near-term diplomacy is dismissed."
  - "Polymarket contract resolves via UMA oracle; a confirmed bilateral summit meeting would be required, not a phone call or third-party mediation."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russian President Vladimir Putin publicly rejected Ukrainian President Volodymyr Zelenskyy's written proposal for direct face-to-face peace negotiations."
    publisher: "AFP ,  AP  and  Reuters"
    published_at: "2026-06-05T18:04:27.000Z"
    source_url: "https://www.aljazeera.com/news/2026/6/5/russias-putin-says-no-point-meeting-ukraines-zelenskyy-for-now"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AFP ,  AP  and  Reuters"
        source_url: "https://www.aljazeera.com/news/2026/6/5/russias-putin-says-no-point-meeting-ukraines-zelenskyy-for-now"
        retrieved_at: "2026-06-06T10:00:26+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 1% price leaves no meaningful probability on any summit this month."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AFP ,  AP  and  Reuters: Russia’s Putin says ‘no point’ meeting Ukraine’s Zelenskyy for now | R"
    url: "https://www.aljazeera.com/news/2026/6/5/russias-putin-says-no-point-meeting-ukraines-zelenskyy-for-now"
    published_at: "2026-06-05T18:04:27.000Z"
    retrieved_at: "2026-06-06T10:00:26+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
