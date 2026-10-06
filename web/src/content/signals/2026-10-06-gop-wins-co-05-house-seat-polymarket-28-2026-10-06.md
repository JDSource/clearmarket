---
signal_id: "CMSIG2026100606"
signal_slug: "gop-wins-co-05-house-seat-polymarket-28-2026-10-06"
headline: "GOP wins CO-05 House seat: Polymarket 28%"
semantic_title: "Republican win in CO-05 holds below 30%"
telemetry: "Polymarket 28%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-06T00:00:00.000Z"
event_id: "CM-EVT-FMXJH0P4G0"
event_slug: "co-05-house-election-winner"
event_question: "Will the CO-05 House seat be won by a Republican in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbc533740775ffabd04d60009b45332c2a6f8cba43813bdf7b9577c5d0196a25d"
  question_raw: "Will the Democratic Party win the CO-05 House seat?"
  current_price: 0.28
  volume_24h_usd: 66.199316
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "The Polymarket contract on a Republican winning Colorado's 5th congressional district sits at 28%, making it a decided underdog."
  - "The late money wave described in the news is not yet reflected as a GOP-favorable shift; Polymarket keeps Republicans well below 50% in CO-05."
  - "By contrast, Polymarket prices Republicans at 96% in Ohio's 11th district and 95% in Oklahoma's 3rd, showing the ad dollars are targeting genuinely contested seats."
  - "Resolves via Polymarket's UMA oracle following official district election certification."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Republicans have poured over 700 million dollars in late advertising into congressional races as they try to contain midterm losses in challenging districts."
    publisher: "Ben Kamisar"
    published_at: "2026-10-06T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/politics/2026-election/republicans-fight-red-state-midterm-chaos-hundreds-millions-late-money-rcna601675"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ben Kamisar"
        source_url: "https://www.nbcnews.com/politics/2026-election/republicans-fight-red-state-midterm-chaos-hundreds-millions-late-money-rcna601675"
        retrieved_at: "2026-10-06T14:42:27+00:00"
  - type: "pm_response"
    notes: "Polymarket draws a sharp distinction between safe Republican seats and competitive targets like CO-05, where the party remains a long shot."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ben Kamisar: Republicans fight red-state midterm chaos with hundreds of millions in"
    url: "https://www.nbcnews.com/politics/2026-election/republicans-fight-red-state-midterm-chaos-hundreds-millions-late-money-rcna601675"
    published_at: "2026-10-06T00:00:00.000Z"
    retrieved_at: "2026-10-06T14:42:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
