---
signal_id: "CMSIG2026062803"
signal_slug: "us-invades-iran-before-2027-polymarket-14-2026-06-28"
headline: "US invades Iran before 2027: Polymarket 14%"
semantic_title: "US invasion of Iran before 2027 wavers at low conviction"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-28T06:14:45.000Z"
event_id: "CM-EVT-WD982793G1"
event_slug: "will-the-us-invade-iran-before-2027"
event_question: "Will the United States invade Iran before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5db999fad322cea2914535aae5517060c3f80ad6d8c0231cde2124a434d16846"
  question_raw: "Will the U.S. invade Iran before 2027?"
  current_price: 0.14
  volume_24h_usd: 38634.804211999995
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a US invasion of Iran before 2027 at 14%, resolving via uma_oracle."
  - "Active exchanges including Iranian drone strikes on Bahrain and Kuwait and US counter-strikes are consistent with elevated but minority invasion odds."
  - "The Iranian regime survival contract at 100% on Polymarket implies markets see escalation as limited, not regime-ending."
  - "Polymarket's 'UK, France, or Germany strike Iran by June 30' sits at 0%, confirming markets price this as a bilateral US-Iran conflict with no NATO expansion."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran attacked US bases in Bahrain and Kuwait while the US conducted strikes near the Strait of Hormuz, escalating the 121-day conflict."
    publisher: "Elizabeth Melimopoulos"
    published_at: "2026-06-28T06:14:45.000Z"
    source_url: "https://www.aljazeera.com/news/2026/6/28/iran-war-day-121-iran-attacks-bahrain-kuwait-as-us-strikes-near-hormuz"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Elizabeth Melimopoulos"
        source_url: "https://www.aljazeera.com/news/2026/6/28/iran-war-day-121-iran-attacks-bahrain-kuwait-as-us-strikes-near-hormuz"
        retrieved_at: "2026-06-29T01:46:24+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; 14% reflects active hostilities priced as short of full ground-invasion threshold."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Elizabeth Melimopoulos: Iran war day 121: Iran attacks Bahrain, Kuwait as US strikes near Horm"
    url: "https://www.aljazeera.com/news/2026/6/28/iran-war-day-121-iran-attacks-bahrain-kuwait-as-us-strikes-near-hormuz"
    published_at: "2026-06-28T06:14:45.000Z"
    retrieved_at: "2026-06-29T01:46:24+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
