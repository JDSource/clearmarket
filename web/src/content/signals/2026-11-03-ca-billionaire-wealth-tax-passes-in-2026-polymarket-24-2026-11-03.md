---
signal_id: "CMSIG2026110307"
signal_slug: "ca-billionaire-wealth-tax-passes-in-2026-polymarket-24-2026-11-03"
headline: "CA billionaire wealth tax passes in 2026: Polymarket 24%"
semantic_title: "California billionaire wealth tax odds stay well below 25%"
telemetry: "Polymarket 24%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-03T05:01:51.000Z"
event_id: "CM-EVT-NGG1B28FJ8"
event_slug: "billionaire-one-time-wealth-tax-passes-in-california-election-2026"
event_question: "Will a billionaire one-time wealth tax pass in the California election in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9345d5142a67f5541264c96515496affee02580f1c572680759eac9fd2a1588a"
  question_raw: "Billionaire one-time wealth tax passes in California election 2026?"
  current_price: 0.24
  volume_24h_usd: 19874.141337999998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket puts the California billionaire one-time wealth tax passing at 24%, keeping it a clear underdog heading into the vote."
  - "Record $12 billion in national midterm spending has not translated to market confidence in the California ballot measure succeeding."
  - "The 24% probability sits well below the 50% threshold, suggesting the market is not pricing any late-cycle polling surge for the measure."
  - "Resolution via Polymarket UMA oracle; California ballot initiative results can take days to certify given mail-vote counting rules, delaying settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Election Day arrives with California voters weighing a one-time billionaire wealth tax measure amid a record-spending midterm cycle."
    publisher: "Jill Colvin, Mary Clare Jalonick, Will Weissert"
    published_at: "2026-11-03T05:01:51.000Z"
    source_url: "https://apnews.com/article/midterm-election-house-senate-democrats-republicans-trump-f126e12e05b579a327b98481c0ae2226"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jill Colvin, Mary Clare Jalonick, Will Weissert"
        source_url: "https://apnews.com/article/midterm-election-house-senate-democrats-republicans-trump-f126e12e05b579a327b98481c0ae2226"
        retrieved_at: "2026-11-03T07:48:22+00:00"
  - type: "pm_response"
    notes: "Polymarket at 24% is consistent with historical base rates for wealth tax ballot measures facing organized opposition spending in California."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jill Colvin, Mary Clare Jalonick, Will Weissert: Midterm elections coming to a close as voters pass judgment on Trump's"
    url: "https://apnews.com/article/midterm-election-house-senate-democrats-republicans-trump-f126e12e05b579a327b98481c0ae2226"
    published_at: "2026-11-03T05:01:51.000Z"
    retrieved_at: "2026-11-03T07:48:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
