---
signal_id: "CMSIG2026060604"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-28-2026-06-06"
headline: "US-Iran nuclear deal by June 30: Polymarket 28%"
semantic_title: "US-Iran nuclear deal by June 30 holds at long-shot pricing"
telemetry: "Polymarket 28%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-06T01:04:27.000Z"
event_id: "CM-EVT-LG47Z78CF2"
event_slug: "us-iran-nuclear-deal-by-june-30"
event_question: "Will the US and Iran reach a nuclear deal by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa70fc3695a65833b91b45df6db6015096f3e1471b70352ca411b4209010e7633"
  question_raw: "US-Iran nuclear deal by June 30?"
  current_price: 0.28
  volume_24h_usd: 207316.77510300005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices a 28% chance of a US-Iran nuclear deal by June 30, a meaningful but minority probability despite active diplomacy."
  - "Reports of Witkoff and Kushner meeting nuclear experts and pursuing a framework are consistent with elevated odds, but the market is not treating a deal as likely within weeks."
  - "The December 31 contract on Iran ending uranium enrichment sits at 52%, suggesting the market sees the second half of 2026 as the more plausible window."
  - "Active drone intercepts near the Strait of Hormuz (Story 20) and the June 30 Hormuz-deal contract at just 6% (CM-EVT-974T1626Q2) suggest the market sees military tensions as inconsistent with imminent diplomacy."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump envoys Steve Witkoff and Jared Kushner reportedly met nuclear experts and are eyeing a memorandum of understanding with Iran to end the conflict and launch detailed nuclear talks."
    publisher: "aa.com.tr"
    published_at: "2026-06-06T01:04:27.000Z"
    source_url: "https://www.aa.com.tr/en/americas/trump-envoys-hold-meeting-with-nuclear-experts-for-deal-with-iran-report/3958134"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aa.com.tr"
        source_url: "https://www.aa.com.tr/en/americas/trump-envoys-hold-meeting-with-nuclear-experts-for-deal-with-iran-report/3958134"
        retrieved_at: "2026-06-06T10:00:26+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; a formal signed nuclear agreement, not a memorandum of understanding, would likely be required for resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aa.com.tr: Trump envoys hold meeting with nuclear experts for deal with Iran: Rep"
    url: "https://www.aa.com.tr/en/americas/trump-envoys-hold-meeting-with-nuclear-experts-for-deal-with-iran-report/3958134"
    published_at: "2026-06-06T01:04:27.000Z"
    retrieved_at: "2026-06-06T10:00:26+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
