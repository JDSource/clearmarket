---
signal_id: "CMSIG2026090307"
signal_slug: "gop-sc-7-house-seat-2026-polymarket-96-2026-09-03"
headline: "GOP SC-7 House seat 2026: Polymarket 96%"
semantic_title: "GOP South Carolina 7th District seat stays heavily favored"
telemetry: "Polymarket 96%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-03T00:00:00.000Z"
event_id: "CM-EVT-LHTPJL4HZ2"
event_slug: "sc-07-house-election-winner"
event_question: "Will the Republican Party win the South Carolina 7th Congressional District House seat in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa6dcf4a15de9b25d12fe24019a64b996f6e0c1eacd39d656f4d915429a46be56"
  question_raw: "Will the Republican Party win the SC-07 House seat?"
  current_price: 0.96
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "The Polymarket contract on the Republican Party winning the South Carolina 7th Congressional District House seat sits at 96%, near certain."
  - "Trump's active midterm campaigning pledge is consistent with the strong Republican position in South Carolina, one of the party's safest seats."
  - "The companion contract on the Democratic candidate winning South Carolina House District 6 (CM-EVT-HYH65MMVY3) sits at just 5%, reinforcing the GOP's dominance in this state."
  - "Resolution is tied to the official 2026 general election result for the South Carolina 7th Congressional District, via Polymarket's UMA oracle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump vowed to campaign in 35 midterm races as Elon Musk's PAC targets key House and Senate seats ahead of the 2026 midterms."
    publisher: "newsweek.com"
    published_at: "2026-09-03T00:00:00.000Z"
    source_url: "https://www.newsweek.com/trump-vows-to-campaign-in-35-races-as-musk-pac-targets-key-seats-12398081"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "newsweek.com"
        source_url: "https://www.newsweek.com/trump-vows-to-campaign-in-35-races-as-musk-pac-targets-key-seats-12398081"
        retrieved_at: "2026-09-03T12:30:58+00:00"
  - type: "pm_response"
    notes: "Polymarket at 96% reflects near-unanimous consensus; SC-7 is among the least contested seats across all currently priced midterm contracts in this batch."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "newsweek.com: Trump Vows to Campaign in 35 Midterm Races as Musk PAC Targets Key Sea"
    url: "https://www.newsweek.com/trump-vows-to-campaign-in-35-races-as-musk-pac-targets-key-seats-12398081"
    published_at: "2026-09-03T00:00:00.000Z"
    retrieved_at: "2026-09-03T12:30:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
