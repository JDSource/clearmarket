---
signal_id: "CMSIG2026090407"
signal_slug: "zelensky-out-by-end-of-2026-polymarket-8-2026-09-04"
headline: "Zelensky out by end of 2026: Polymarket 8%"
semantic_title: "Odds on Zelensky leaving office before 2027 remain a long shot"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-04T00:00:00.000Z"
event_id: "CM-EVT-355Q75KD17"
event_slug: "zelenskyy-out-as-ukraine-president-before-2027"
event_question: "Will Zelenskyy be out as Ukraine president by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x51f624dbbf14f9edb575fef1be6f7a303751de70783fa144fce27b957452c803"
  question_raw: "Zelenskyy out as Ukraine president by end of 2026?"
  current_price: 0.08
  volume_24h_usd: 14705.47
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 8% odds that Zelensky will be out as Ukraine president by end of 2026, resolving via UMA oracle, and trading volume surged 6,419% day over day."
  - "The volume spike, 65 times the prior day's level, signals this contract is drawing intense fresh attention amid the Russian strike escalation and US peace envoy visit."
  - "The current 8% price means the market still treats Zelensky's removal as a long shot, but the volume surge flags that traders are actively reassessing the scenario."
  - "Companion Polymarket contract on US recognizing Russian sovereignty over Ukraine (CM-EVT-T1H8NR4G99) sits at just 4%, suggesting the market sees neither a Zelensky exit nor a US capitulation as likely near-term."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia struck Ukraine's intelligence headquarters in what officials called a major escalation, as US envoys prepared to visit Moscow and Kyiv."
    publisher: "Amy Hawkins"
    published_at: "2026-09-04T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/sep/04/russia-strikes-ukraine-intelligence-hq-kyiv-major-escalation"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Amy Hawkins"
        source_url: "https://www.theguardian.com/world/2026/sep/04/russia-strikes-ukraine-intelligence-hq-kyiv-major-escalation"
        retrieved_at: "2026-09-05T11:34:19+00:00"
  - type: "pm_response"
    notes: "Volume up 6,419% day over day on Polymarket is the standout signal, price stays low at 8% but the surge in trading activity indicates the market is actively stress-testing this scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Amy Hawkins: Russia strikes Ukraine intelligence HQ in ‘major escalation’ | Ukraine"
    url: "https://www.theguardian.com/world/2026/sep/04/russia-strikes-ukraine-intelligence-hq-kyiv-major-escalation"
    published_at: "2026-09-04T00:00:00.000Z"
    retrieved_at: "2026-09-05T11:34:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
