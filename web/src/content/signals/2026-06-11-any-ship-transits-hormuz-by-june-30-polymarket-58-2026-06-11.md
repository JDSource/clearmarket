---
signal_id: "CMSIG2026061105"
signal_slug: "any-ship-transits-hormuz-by-june-30-polymarket-58-2026-06-11"
headline: "Any ship transits Hormuz by June 30: Polymarket 58%"
semantic_title: "Any Hormuz ship transit by June 30 consensus wavers at majority"
telemetry: "Polymarket 58%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-11T04:46:07.000Z"
event_id: "CM-EVT-VB1YHPRLZ3"
event_slug: "will-ships-transit-the-strait-of-hormuz-on-any-day-by-june-30"
event_question: "Will any ships transit the Strait of Hormuz by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2358809f9f612f8fb4f224b342ba2841ca644a6e3c46adb4c3bcee910cc31632"
  question_raw: "Will 20 ships transit the Strait of Hormuz on any day by June 30, 2026?"
  current_price: 0.58
  volume_24h_usd: 4003.476819
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T16:00:00Z"
bullets:
  - "Polymarket prices 58% on at least one ship transiting the Strait of Hormuz by June 30, 2026."
  - "Tehran's closure claim and ongoing US-Iran exchanges of fire push against this majority, but the market still leans toward at least token transit occurring, consistent with Trump's reported claim that the US secretly escorted over 200 commercial ships through Hormuz."
  - "The 58% versus 13% on full unrestricted shipping agreement by June 30 shows the market distinguishes between a technical transit and a formal deal."
  - "Resolves via portwatch.imf.org shipping traffic data; a single US-escorted vessel would likely satisfy the contract's 'any ships' threshold, making the resolution definition critical."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran claimed closure of the Strait of Hormuz after the US launched a second night of strikes, with reports of active exchange of fire and Bahraini infrastructure damage."
    publisher: "David Vujanovic"
    published_at: "2026-06-11T04:46:07.000Z"
    source_url: "https://www.thenationalnews.com/news/mena/2026/06/11/what-we-know-us-strikes-iran-again-as-tehran-claims-strait-of-hormuz-closure/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "David Vujanovic"
        source_url: "https://www.thenationalnews.com/news/mena/2026/06/11/what-we-know-us-strikes-iran-again-as-tehran-claims-strait-of-hormuz-closure/"
        retrieved_at: "2026-06-11T12:08:11+00:00"
  - type: "pm_response"
    notes: "Polymarket's 58% on any Hormuz transit by June 30 sits well above the 13% on a formal Iranian agreement, with the gap reflecting the market's belief that practical transit may occur without a diplomatic resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "David Vujanovic: What we know: US strikes Iran again as Tehran claims Strait of Hormuz"
    url: "https://www.thenationalnews.com/news/mena/2026/06/11/what-we-know-us-strikes-iran-again-as-tehran-claims-strait-of-hormuz-closure/"
    published_at: "2026-06-11T04:46:07.000Z"
    retrieved_at: "2026-06-11T12:08:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
