---
signal_id: "CMSIG2026092506"
signal_slug: "nasdaq-100-implied-range-31400-31600-kalshi-ladder-2026-09-25"
headline: "Nasdaq-100 implied range 31400-31600: Kalshi ladder"
semantic_title: "Nasdaq-100 market-implied level holds in the 31400 to 31600 range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-25T15:46:11.621Z"
event_id: "CM-EVT-HYFSJ2CNW7"
event_slug: "kxnasdaq100maxy-26dec31h1600"
event_question: "Nasdaq-100 index level"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXNASDAQ100MAXY-26DEC31H1600-T31599.99"
  question_raw: "Will the Nasdaq-100 be above 31599.99 at the end of Dec 31, 2026 at 4pm EST?"
  current_price: 0.44
  volume_24h_usd: 114.4
  arbitration_model: "kalshi_staff"
  resolution_source: "For example, Google Finance"
  resolves_at: "2027-01-08T00:00:00Z"
bullets:
  - "The Kalshi ladder prices the Nasdaq-100 market-implied range at approximately 31400 to 31600, with 68% above 31400 but only 44% above 31600."
  - "Trading volume on this ladder surged roughly 59000 times day-over-day, a sharp signal of fresh positioning amid the jobs and rate-hike uncertainty."
  - "The current Nasdaq spot level cited in the story excerpt is 27099, well below the ladder's implied range, the ladder likely references a different contract horizon or index definition; traders should verify the exact contract terms."
  - "The tail is notable: only 19% probability above 32000, suggesting the market caps the near-term upside even as volume floods in."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Wall Street week-ahead coverage flags US jobs data and possible Fed rate hike as the key tests for equities and bonds, with the Nasdaq already at 27099."
    publisher: "By Dow Jones Newswires staff"
    published_at: "2026-09-25T15:46:11.621Z"
    source_url: "https://www.wsj.com/economy/week-ahead-for-fx-bonds-u-s-jobs-data-in-focus-as-another-fed-rate-hike-looks-possible-8593c44f"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "By Dow Jones Newswires staff"
        source_url: "https://www.wsj.com/economy/week-ahead-for-fx-bonds-u-s-jobs-data-in-focus-as-another-fed-rate-hike-looks-possible-8593c44f"
        retrieved_at: "2026-09-26T07:47:13+00:00"
  - type: "pm_response"
    notes: "Ladder contract volume confirmed at 59405x day-over-day; resolution source unspecified, contract terms should be checked before trading."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "By Dow Jones Newswires staff: Week Ahead for FX, Bonds: U.S. Jobs Data in Focus as Another Fed Rate"
    url: "https://www.wsj.com/economy/week-ahead-for-fx-bonds-u-s-jobs-data-in-focus-as-another-fed-rate-hike-looks-possible-8593c44f"
    published_at: "2026-09-25T15:46:11.621Z"
    retrieved_at: "2026-09-26T07:47:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
