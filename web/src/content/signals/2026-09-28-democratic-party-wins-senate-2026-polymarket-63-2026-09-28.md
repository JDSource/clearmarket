---
signal_id: "CMSIG2026092806"
signal_slug: "democratic-party-wins-senate-2026-polymarket-63-2026-09-28"
headline: "Democratic Party wins Senate 2026: Polymarket 63%"
semantic_title: "Democrats favored to take Senate control in 2026 midterms"
telemetry: "Polymarket 63%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-28T00:00:00.000Z"
event_id: "CM-EVT-M9WJY06T90"
event_slug: "which-party-will-win-the-senate-in-2026"
event_question: "Which party will win control of the U.S. Senate in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x307a1ed89d60b61002dd5bbf00e1408c5ed2ab3fcdb056191ca7ef9bc34d38f3"
  question_raw: "Will the Democratic Party control the Senate after the 2026 Midterm elections?"
  current_price: 0.63
  volume_24h_usd: 10507.615635
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "The Polymarket contract on the Democratic Party winning control of the US Senate in the 2026 election prices at 63%."
  - "Trump's taxpayer-funded campaign-style advertising is drawing scrutiny weeks before the midterms, consistent with a market that prices Democrats as modest Senate favorites."
  - "The Kalshi contract on Republicans holding at least one chamber sits at 62%, implying markets see the House as the more likely Republican retention vehicle."
  - "Resolves via Polymarket's UMA oracle based on official Senate election outcomes following the November 2026 midterms."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "USA Today reports President Donald Trump launched another taxpayer-funded television ad warning of a 'final battle' ahead of the 2026 midterm elections."
    publisher: "usatoday.com"
    published_at: "2026-09-28T00:00:00.000Z"
    source_url: "https://www.usatoday.com/story/news/politics/2026/09/28/trump-ad-taxpayer-funds-midterm-election/91984613007/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "usatoday.com"
        source_url: "https://www.usatoday.com/story/news/politics/2026/09/28/trump-ad-taxpayer-funds-midterm-election/91984613007/"
        retrieved_at: "2026-09-29T14:34:30+00:00"
  - type: "pm_response"
    notes: "Polymarket contract on Democratic Senate control in 2026; 63% pricing puts Democrats as clear but not dominant favorites entering the final weeks."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "usatoday.com: Trump ad funded by taxpayers warns of 'final battle' before midterms"
    url: "https://www.usatoday.com/story/news/politics/2026/09/28/trump-ad-taxpayer-funds-midterm-election/91984613007/"
    published_at: "2026-09-28T00:00:00.000Z"
    retrieved_at: "2026-09-29T14:34:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
