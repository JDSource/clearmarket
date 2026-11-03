---
signal_id: "CMSIG2026110205"
signal_slug: "republicans-hold-governorship-edge-kalshi-88-2026-11-02"
headline: "Republicans hold governorship edge: Kalshi 88%"
semantic_title: "Republicans staying favored to hold more governorships"
telemetry: "Kalshi 88%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-02T18:00:00.000Z"
event_id: "CM-EVT-4DFCBXLZN6"
event_slug: "kxgovwins-27jan01"
event_question: "Will Republicans hold more governorships than Democrats after the midterms?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVWINS-27JAN01-R-50"
  question_raw: "Will the difference between the number of Republican governors and the number of Democratic governors be between -50 and -1 governors after the 2026 midterms?"
  current_price: 0.88
  volume_24h_usd: 32623.78
  arbitration_model: "kalshi_staff"
  resolution_source: "the Statistical Review of World Energy"
  resolves_at: "2027-04-01T15:00:00Z"
bullets:
  - "Kalshi prices Republicans holding more governorships than Democrats after the midterms at 88%, a heavily favored outcome."
  - "Despite voters citing economic pain and trusting Democrats more on costs, the market still assigns Republicans a durable structural advantage in gubernatorial races."
  - "The 88% governorship probability contrasts with the 75% Republican odds of holding any congressional chamber, suggesting markets see executive-level races as more insulated."
  - "Resolution via the Statistical Review of World Energy as named source, an unusual resolver for a domestic political question; bettors should note this non-standard settlement authority."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Voter polls show the economy as the top midterm issue, with Democrats more trusted to address costs but Republicans holding structural advantages in gubernatorial races."
    publisher: "Ruth Igielnik"
    published_at: "2026-11-02T18:00:00.000Z"
    source_url: "https://www.nytimes.com/2026/11/02/us/politics/midterm-election-polls-trump-economy-immigration.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ruth Igielnik"
        source_url: "https://www.nytimes.com/2026/11/02/us/politics/midterm-election-polls-trump-economy-immigration.html"
        retrieved_at: "2026-11-03T07:48:22+00:00"
  - type: "pm_response"
    notes: "Kalshi contract has been consistently priced above 85% throughout the campaign cycle; the news-market gap on economic sentiment has not closed the Republican governor advantage."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ruth Igielnik: What Are Voters’ Top Concerns? Midterm Election Polls Point to the Eco"
    url: "https://www.nytimes.com/2026/11/02/us/politics/midterm-election-polls-trump-economy-immigration.html"
    published_at: "2026-11-02T18:00:00.000Z"
    retrieved_at: "2026-11-03T07:48:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
