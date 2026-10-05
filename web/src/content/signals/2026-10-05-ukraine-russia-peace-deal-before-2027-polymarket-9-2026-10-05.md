---
signal_id: "CMSIG2026100508"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-9-2026-10-05"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 9%"
semantic_title: "Ukraine-Russia peace deal before 2027 stays a long shot"
telemetry: "Polymarket 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-05T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.09
  volume_24h_usd: 734.882223
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Ukraine-Russia peace deal before 2027 at just 9%, a long shot despite active US and India peace diplomacy."
  - "Escalating drone strikes on Kyiv infrastructure while peace talks are pursued puts the market's skeptical 9% in direct tension with diplomatic news headlines."
  - "A companion Polymarket contract (CM-EVT-207L4994P4) prices a US-Russia military clash at 4%, suggesting markets see neither peace nor direct escalation as likely near-term."
  - "Resolution via Polymarket's uma_oracle; a formal signed peace deal is required, setting a much higher bar than ceasefire talks or diplomatic meetings."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia escalated drone strikes targeting Kyiv bridges as the US made a fresh push for peace talks and India signaled deeper involvement in ceasefire efforts."
    publisher: "Joanna Kakissis"
    published_at: "2026-10-05T00:00:00.000Z"
    source_url: "https://www.npr.org/2026/10/05/nx-s1-5989637/russias-attacks-on-ukraine-escalate-as-its-drones-target-bridges-in-kyiv"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Joanna Kakissis"
        source_url: "https://www.npr.org/2026/10/05/nx-s1-5989637/russias-attacks-on-ukraine-escalate-as-its-drones-target-bridges-in-kyiv"
        retrieved_at: "2026-10-05T16:44:30+00:00"
  - type: "pm_response"
    notes: "Polymarket at 9% is the only priced candidate for this event; the 4% US-Russia clash contract provides a useful cross-market frame."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Joanna Kakissis: Russia's attacks on Ukraine escalate as its drones target bridges in K"
    url: "https://www.npr.org/2026/10/05/nx-s1-5989637/russias-attacks-on-ukraine-escalate-as-its-drones-target-bridges-in-kyiv"
    published_at: "2026-10-05T00:00:00.000Z"
    retrieved_at: "2026-10-05T16:44:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
