---
signal_id: "CMSIG2026081908"
signal_slug: "north-korea-invades-south-korea-before-2027-polymarket-3-2026-08-19"
headline: "North Korea invades South Korea before 2027: Polymarket 3%"
semantic_title: "North Korea invading South Korea before 2027 stays a long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-19T00:00:00.000Z"
event_id: "CM-EVT-GGMF8V7JH2"
event_slug: "will-north-korea-invade-south-korea-before-2027"
event_question: "Will North Korea invade South Korea before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84dc47b1dd9cd99a9217b92a95690729334b647650bb6bf676bb31c3db0d7f79"
  question_raw: "Will North Korea invade South Korea before 2027?"
  current_price: 0.028
  volume_24h_usd: 48.13
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 3% on North Korea invading South Korea before 2027, a deep long-shot despite the diplomatic shift."
  - "Trump cutting drills short and praising Kim Jong Un is a significant security signal, but markets are not pricing an imminent invasion scenario."
  - "The news and market pricing diverge in magnitude, the geopolitical gesture is real, but the Polymarket contract shows no escalation pricing."
  - "Resolves via UMA oracle on a confirmed North Korean military invasion, a high evidentiary bar that keeps the contract anchored near zero."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US-South Korea joint military drills were cut short after a surprise Trump order, with Trump calling the exercises hostile toward North Korea."
    publisher: "ABC News"
    published_at: "2026-08-19T00:00:00.000Z"
    source_url: "https://abcnews.com/International/us-south-korea-military-drills-end-early-after/story?id=135763052"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/International/us-south-korea-military-drills-end-early-after/story?id=135763052"
        retrieved_at: "2026-08-20T08:32:51+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 3% resolves via UMA oracle; the low reading reflects markets treating the diplomatic overture as posturing, not a security breakdown."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: US-South Korea military drills to end early after Trump order, Seoul s"
    url: "https://abcnews.com/International/us-south-korea-military-drills-end-early-after/story?id=135763052"
    published_at: "2026-08-19T00:00:00.000Z"
    retrieved_at: "2026-08-20T08:32:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
