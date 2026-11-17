---
signal_id: "CMSIG2026111605"
signal_slug: "lutnick-out-as-commerce-secretary-by-dec-31-polymarket-18-2026-11-16"
headline: "Lutnick out as Commerce Secretary by Dec 31: Polymarket 18%"
semantic_title: "Lutnick out as Commerce Secretary by year-end stays a long shot"
telemetry: "Polymarket 18%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-16T11:11:16.000Z"
event_id: "CM-EVT-H31QLM4JT3"
event_slug: "howard-lutnick-out-as-secretary-of-commerce-by-december-31"
event_question: "Will Howard Lutnick be out as Secretary of Commerce by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7978663d03b5c053dcea87b39e06fad5bcdd036b0c7febfa4309502c02f70c2c"
  question_raw: "Howard Lutnick out as Secretary of Commerce by December 31?"
  current_price: 0.18
  volume_24h_usd: 46723.922945
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract puts 18% odds on Howard Lutnick exiting as Commerce Secretary by December 31, 2026, resolving via UMA oracle."
  - "Trump's public defense of Lutnick is consistent with an 82% market read that Lutnick stays in place through year-end."
  - "The Nvidia chip export restriction controversy provides a concrete near-term trigger that could shift this probability if political pressure escalates."
  - "Resolution via UMA oracle by December 31; a companion Kalshi contract on Lutnick removal via unspecified source shows no price, leaving Polymarket as the sole live read."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Commerce Secretary Howard Lutnick was defended by President Trump after reports that Lutnick was allegedly slow-walking Nvidia chip export restrictions."
    publisher: "Cecilia Nowell"
    published_at: "2026-11-16T11:11:16.000Z"
    source_url: "https://www.theguardian.com/us-news/live/2026/nov/16/donald-trump-asia-visit-democrats-republicans-elizabeth-warren-faa-air-disruption-latest-news-updates"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Cecilia Nowell"
        source_url: "https://www.theguardian.com/us-news/live/2026/nov/16/donald-trump-asia-visit-democrats-republicans-elizabeth-warren-faa-air-disruption-latest-news-updates"
        retrieved_at: "2026-11-17T07:48:04+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on December 31, 2026; Trump's defense of Lutnick is the dominant near-term news driver keeping removal odds below 20%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Cecilia Nowell: DOJ warns Elizabeth Warren over Trump investigations, US politics liv"
    url: "https://www.theguardian.com/us-news/live/2026/nov/16/donald-trump-asia-visit-democrats-republicans-elizabeth-warren-faa-air-disruption-latest-news-updates"
    published_at: "2026-11-16T11:11:16.000Z"
    retrieved_at: "2026-11-17T07:48:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
