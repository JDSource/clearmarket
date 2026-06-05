---
signal_id: "CMSIG2026060404"
signal_slug: "congress-iran-war-powers-resolution-by-june-30-polymarket-4-2026-06-04"
headline: "Congress Iran war powers resolution by June 30: Polymarket 4%"
semantic_title: "Congress passing Iran war powers resolution by June 30 remains priced out"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-04T03:50:26.000Z"
event_id: "CM-EVT-KF5S4BY541"
event_slug: "congress-passes-iran-war-powers-resolution-by-june-30"
event_question: "Will Congress pass an Iran war powers resolution by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xcb3c2e94aefd13bb09a72fdf74d44fa7b2ebe437b863e0621831c020bfd4ed4d"
  question_raw: "Congress passes Iran war powers resolution by June 30?"
  current_price: 0.039
  volume_24h_usd: 1234.659639
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices only a 4% chance Congress passes an Iran war powers resolution by June 30."
  - "The House vote is a genuine rebuke of the president, but the market implies the Senate is seen as a near-certain kill switch for the resolution."
  - "The House passage is a procedural milestone, yet Polymarket is effectively pricing a Senate block as near-certain within the month."
  - "Resolves via Polymarket's UMA oracle; the resolution must clear both chambers and survive any veto or procedural block before June 30."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The House passed a war powers resolution to halt U.S. military action against Iran, with four Republicans joining Democrats in a 215-208 vote."
    publisher: "thedailybeast.com"
    published_at: "2026-06-04T03:50:26.000Z"
    source_url: "https://www.thedailybeast.com/donald-trump-hit-with-huge-blow-as-republicans-vote-against-his-war-in-iran/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "thedailybeast.com"
        source_url: "https://www.thedailybeast.com/donald-trump-hit-with-huge-blow-as-republicans-vote-against-his-war-in-iran/"
        retrieved_at: "2026-06-05T12:03:19+00:00"
  - type: "pm_response"
    notes: "Polymarket at 4% sharply discounts the House vote's downstream impact, implying the Senate is viewed as a near-certain obstacle within the June 30 window."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "thedailybeast.com: Donald Trump Hit With Huge Blow as Republicans Vote Against His War in"
    url: "https://www.thedailybeast.com/donald-trump-hit-with-huge-blow-as-republicans-vote-against-his-war-in-iran/"
    published_at: "2026-06-04T03:50:26.000Z"
    retrieved_at: "2026-06-05T12:03:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
