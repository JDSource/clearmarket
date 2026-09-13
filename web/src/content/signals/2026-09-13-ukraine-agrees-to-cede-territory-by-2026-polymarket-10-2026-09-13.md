---
signal_id: "CMSIG2026091305"
signal_slug: "ukraine-agrees-to-cede-territory-by-2026-polymarket-10-2026-09-13"
headline: "Ukraine agrees to cede territory by 2026: Polymarket 10%"
semantic_title: "Ukraine ceding territory by year-end stays a long shot"
telemetry: "Polymarket 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-13T11:05:00.000Z"
event_id: "CM-EVT-XP7FFT2MC9"
event_slug: "will-ukraine-agree-to-cede-territory-to-russia-before-2027"
event_question: "Will Ukraine agree to cede territory to Russia by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x21bf9a7dae81b6bd51acae73185686ab8997b81b1401e4be10e114d472599c26"
  question_raw: "Will Ukraine agree to cede territory to Russia before 2027?"
  current_price: 0.1
  volume_24h_usd: 1828.1765019999998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract puts only 10% on Ukraine agreeing to cede territory to Russia by 2026, resolving via UMA oracle."
  - "Kushner's public acknowledgment that territory is the central sticking point is consistent with the market's long-shot pricing of a deal this year."
  - "The companion contract on Ukraine recognizing Russian sovereignty over its territory (CM-EVT-1L07BR8JD5) saw volume surge 114x day-over-day, signaling the question is drawing intense fresh attention despite no stated price."
  - "The Polymarket contract on the US recognizing Russian sovereignty over Ukraine before 2027 sits at just 3%, suggesting markets see diplomatic resolution as even less likely from the American side."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US special envoy Jared Kushner stated at the YES 2026 conference that territory remains the main obstacle to a Ukraine-Russia peace deal."
    publisher: "Kyiv Post"
    published_at: "2026-09-13T11:05:00.000Z"
    source_url: "https://www.kyivpost.com/post/84406"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kyiv Post"
        source_url: "https://www.kyivpost.com/post/84406"
        retrieved_at: "2026-09-13T13:04:33+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; a formal Ukrainian government announcement of territorial concession would be the key resolution trigger."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kyiv Post: Territory Remains Main Obstacle to Ukraine-Russia Deal, Kushner Says"
    url: "https://www.kyivpost.com/post/84406"
    published_at: "2026-09-13T11:05:00.000Z"
    retrieved_at: "2026-09-13T13:04:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
