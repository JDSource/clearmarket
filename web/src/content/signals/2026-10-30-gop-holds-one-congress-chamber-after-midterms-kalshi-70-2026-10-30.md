---
signal_id: "CMSIG2026103004"
signal_slug: "gop-holds-one-congress-chamber-after-midterms-kalshi-70-2026-10-30"
headline: "GOP holds one Congress chamber after midterms: Kalshi 70%"
semantic_title: "Republicans retaining at least one chamber stays near 75%"
telemetry: "Kalshi 70%"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-10-30T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.7
  volume_24h_usd: 2110519.5
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi contract on Republicans controlling at least one chamber of Congress after the midterms sits at 70%."
  - "Election-day is days away; the 70% reading reflects a market that favors GOP retention of at least one chamber but does not treat it as a near-certainty."
  - "The companion Kalshi contract on the Democratic Party winning the U.S. House (CM-EVT-FV8MR86S63) sits at 94%, implying the market sees Democrats flipping the House as very likely while Republicans hold the Senate."
  - "Resolves via the Bureau of Labor Statistics per the contract terms, an unusual resolution source for an electoral question; traders should note this potential ambiguity."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The final weekend of the 2026 U.S. midterm campaign features Trump tele-rallies, a Democratic intraparty rift in Michigan, and major tech earnings all hitting markets simultaneously."
    publisher: "Thomson Reuters"
    published_at: "2026-10-30T00:00:00.000Z"
    source_url: "https://wtvbam.com/2026/10/30/take-five-midterms-meet-earnings/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://wtvbam.com/2026/10/30/take-five-midterms-meet-earnings/"
        retrieved_at: "2026-10-31T14:15:55+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 70%; the 94% Democratic House win contract on Kalshi implies the 70% GOP-holds-one-chamber reading is driven almost entirely by Senate retention odds."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: Take Five: Midterms meet earnings"
    url: "https://wtvbam.com/2026/10/30/take-five-midterms-meet-earnings/"
    published_at: "2026-10-30T00:00:00.000Z"
    retrieved_at: "2026-10-31T14:15:55+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
