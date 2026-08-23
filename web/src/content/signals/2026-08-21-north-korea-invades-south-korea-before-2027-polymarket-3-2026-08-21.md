---
signal_id: "CMSIG2026082108"
signal_slug: "north-korea-invades-south-korea-before-2027-polymarket-3-2026-08-21"
headline: "North Korea invades South Korea before 2027: Polymarket 3%"
semantic_title: "North Korea invasion of South Korea stays near zero odds"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-21T00:00:00.000Z"
event_id: "CM-EVT-GGMF8V7JH2"
event_slug: "will-north-korea-invade-south-korea-before-2027"
event_question: "Will North Korea invade South Korea before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84dc47b1dd9cd99a9217b92a95690729334b647650bb6bf676bb31c3db0d7f79"
  question_raw: "Will North Korea invade South Korea before 2027?"
  current_price: 0.031
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on North Korea invading South Korea before 2027 sits at 3%."
  - "Cutting the drill short after North Korea's missile barrage is a de-escalatory signal, consistent with the market assigning near-zero invasion probability."
  - "The Kim Jong Un leadership contract on Kalshi sits at 4% for departure by year-end, suggesting continuity at the top further limits tail-risk scenarios."
  - "Resolution via UMA oracle; an invasion requires a recognized armed incursion across the border, setting a high evidentiary bar for Yes settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US and South Korea wrapped up the Ulchi Freedom Shield drill six days early, one day after North Korea launched a missile barrage."
    publisher: "apnews.com"
    published_at: "2026-08-21T00:00:00.000Z"
    source_url: "https://apnews.com/article/north-south-korea-us-drills-trump-kim-e0350e23feac60adfa60f2cbf5eff27f"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/north-south-korea-us-drills-trump-kim-e0350e23feac60adfa60f2cbf5eff27f"
        retrieved_at: "2026-08-23T08:24:02+00:00"
  - type: "pm_response"
    notes: "Polymarket holds North Korea invasion odds at 3% despite the missile barrage, treating the early drill end as a net stabilizing signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: US and South Korea wrap up Ulchi Freedom Shield drills 6 days early |"
    url: "https://apnews.com/article/north-south-korea-us-drills-trump-kim-e0350e23feac60adfa60f2cbf5eff27f"
    published_at: "2026-08-21T00:00:00.000Z"
    retrieved_at: "2026-08-23T08:24:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
