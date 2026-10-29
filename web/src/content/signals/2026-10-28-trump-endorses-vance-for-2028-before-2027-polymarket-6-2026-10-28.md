---
signal_id: "CMSIG2026102808"
signal_slug: "trump-endorses-vance-for-2028-before-2027-polymarket-6-2026-10-28"
headline: "Trump endorses Vance for 2028 before 2027: Polymarket 6%"
semantic_title: "Trump endorsing Vance for president before 2027 stays a long shot"
telemetry: "Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T23:00:00.000Z"
event_id: "CM-EVT-VYGG3P41R5"
event_slug: "will-trump-endorse-jd-vance-for-president-before-2027"
event_question: "Will Trump endorse JD Vance for president before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9c414cb64000dc7645b2bba8d7586746f3ddb1cfd1b564769188b81cd63ad667"
  question_raw: "Will Trump endorse JD Vance for president before 2027?"
  current_price: 0.056
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Trump endorsing Vance for president before 2027 prices at just 6%, a long-shot read."
  - "Vance's dual public hawk and private diplomatic posture on Iran suggests an alignment with Trump's agenda rather than an independent political standing that might prompt early endorsement."
  - "A separate Polymarket contract asks whether Vance will announce he will not run for president in 2028 this year, priced at 7%, reinforcing the market's view that the 2028 race remains wide open and unresolved."
  - "Resolves via UMA oracle; the 6% price likely reflects the market treating a 2026 endorsement as a logistically unlikely political maneuver given no imminent primary calendar."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Vice President JD Vance secretly reached out to Iran's security chief with a letter seeking to restart peace talks, even as he publicly backed the US-Iran war, at President Trump's direction."
    publisher: "Benoit Faucon, Alexander Ward, Natalie Andrews"
    published_at: "2026-10-28T23:00:00.000Z"
    source_url: "https://www.wsj.com/world/middle-east/vance-reaches-out-to-iranian-hard-liner-in-bid-to-restart-peace-talks-2c8a2ab8"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Benoit Faucon, Alexander Ward, Natalie Andrews"
        source_url: "https://www.wsj.com/world/middle-east/vance-reaches-out-to-iranian-hard-liner-in-bid-to-restart-peace-talks-2c8a2ab8"
        retrieved_at: "2026-10-29T14:55:20+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via UMA oracle on public statements; Vance's diplomatic role keeps him prominent but the market does not treat that as a 2028 endorsement catalyst."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Benoit Faucon, Alexander Ward, Natalie Andrews: Exclusive | Vance Reaches Out to Iranian Hard-Liner in Bid to Restart"
    url: "https://www.wsj.com/world/middle-east/vance-reaches-out-to-iranian-hard-liner-in-bid-to-restart-peace-talks-2c8a2ab8"
    published_at: "2026-10-28T23:00:00.000Z"
    retrieved_at: "2026-10-29T14:55:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
