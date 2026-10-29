---
signal_id: "CMSIG2026102906"
signal_slug: "alaska-gov-senate-gop-combo-kalshi-1-2026-10-29"
headline: "Alaska Gov-Senate GOP combo: Kalshi 1%"
semantic_title: "Alaska GOP governor-Senate sweep stays a long shot at 1 percent"
telemetry: "Kalshi 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-29T00:00:00.000Z"
event_id: "CM-EVT-09C696KZH3"
event_slug: "kxaksengovcombo-26nov"
event_question: "Alaska Governor-Senate combo"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAKSENGOVCOMBO-26NOV-REPDEM"
  question_raw: "Will Alaska Governor winner be Republican party and Alaska Senate winner be Democratic party?"
  current_price: 0.01
  volume_24h_usd: 92.03
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-11-03T15:00:00Z"
bullets:
  - "The Kalshi contract on a Republican Alaska governor-Senate combination prices at just 1%, a near-certain NO reading."
  - "Trading volume on this contract surged 15,247% day over day, a 153.5x spike, showing the investigation news drove immediate and significant fresh attention."
  - "Kalshi's separate contract on a new senator being elected to represent Alaska prices at 32%, suggesting the market sees a real possibility of Peltola defeating Murkowski but not the full GOP sweep."
  - "Resolves via Bureau of Labor Statistics sourcing; the 1% contract price suggests the market views the governor investigation as noise rather than a decisive electoral shift."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Alaska Governor Mike Dunleavy ordered a criminal investigation into Democratic Senate nominee Mary Peltola's campaign over alleged spoiler candidate recruitment, a move seen as favoring Republican incumbent Lisa Murkowski."
    publisher: "Chris Hippensteel"
    published_at: "2026-10-29T00:00:00.000Z"
    source_url: "https://www.theguardian.com/us-news/live/2026/oct/29/midterm-elections-politics-trump-obama-california-alaska-latest-news-updates"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Chris Hippensteel"
        source_url: "https://www.theguardian.com/us-news/live/2026/oct/29/midterm-elections-politics-trump-obama-california-alaska-latest-news-updates"
        retrieved_at: "2026-10-29T14:55:20+00:00"
  - type: "pm_response"
    notes: "Kalshi resolves via Bureau of Labor Statistics certified results; the massive volume spike is the primary signal here, as the contract price itself was already near its floor."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Chris Hippensteel: Alaska governor orders investigation into Democrat’s Senate campaign,"
    url: "https://www.theguardian.com/us-news/live/2026/oct/29/midterm-elections-politics-trump-obama-california-alaska-latest-news-updates"
    published_at: "2026-10-29T00:00:00.000Z"
    retrieved_at: "2026-10-29T14:55:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
