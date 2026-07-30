---
signal_id: "CMSIG2026072905"
signal_slug: "republican-wins-iowa-senate-seat-polymarket-44-2026-07-29"
headline: "Republican wins Iowa Senate seat: Polymarket 44%"
semantic_title: "Iowa Senate seat odds sit near 50-50 after Obama endorsement"
telemetry: "Polymarket 44%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-29T00:00:00.000Z"
event_id: "CM-EVT-2X8487L8P4"
event_slug: "iowa-senate-election-winner"
event_question: "Will a Republican win the Iowa Senate seat in the next election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd50c016598c499fceea10a1a714e48d9b4953487fe215daeaf916068fae722f1"
  question_raw: "Will the Democrats win the Iowa Senate race in 2026?"
  current_price: 0.44
  volume_24h_usd: 1608.874544
  arbitration_model: "uma_oracle"
bullets:
  - "The Polymarket prediction market prices a 44% chance a Republican wins the Iowa Senate seat, implying a slight lean toward Democrat Josh Turek."
  - "Obama's endorsement of Turek is consistent with the near-even Polymarket odds, confirming the race is viewed as genuinely competitive."
  - "By contrast, the Polymarket contract on Alabama's Senate seat going Republican stands at 95%, illustrating how Iowa is an outlier among contested seats."
  - "Resolution is via UMA oracle using official election results; the contract settles after the general election."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Former President Barack Obama endorsed Iowa Democrat Josh Turek in a video for his bid to flip a Republican-held US Senate seat."
    publisher: "apnews.com"
    published_at: "2026-07-29T00:00:00.000Z"
    source_url: "https://apnews.com/article/obama-josh-turek-iowa-senate-571bcd5377eca160eac686f57875f663"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/obama-josh-turek-iowa-senate-571bcd5377eca160eac686f57875f663"
        retrieved_at: "2026-07-30T10:20:48+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via UMA oracle; the 44% Republican price reflects a coin-flip contest that Obama's involvement has not yet moved decisively."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Obama endorses Iowa Democrat Josh Turek for US Senate | AP News"
    url: "https://apnews.com/article/obama-josh-turek-iowa-senate-571bcd5377eca160eac686f57875f663"
    published_at: "2026-07-29T00:00:00.000Z"
    retrieved_at: "2026-07-30T10:20:48+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
