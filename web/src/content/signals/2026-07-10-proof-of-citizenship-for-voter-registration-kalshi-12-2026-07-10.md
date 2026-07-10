---
signal_id: "CMSIG2026071005"
signal_slug: "proof-of-citizenship-for-voter-registration-kalshi-12-2026-07-10"
headline: "Proof of citizenship for voter registration: Kalshi 12%"
semantic_title: "Proof-of-citizenship voter registration requirement priced as unlikely"
telemetry: "Kalshi 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-10T02:12:41.000Z"
event_id: "CM-EVT-G8CYMWNWC6"
event_slug: "kxelectionbill"
event_question: "Will proof of citizenship be required for federal voter registration?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXELECTIONBILL-27JAN01"
  question_raw: "Will legislation that requires proof of U.S. citizenship as a condition of registering to vote in federal elections become law before Jan 1, 2027?"
  current_price: 0.12
  volume_24h_usd: 44.35
  arbitration_model: "kalshi_staff"
  resolution_source: "White House"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market prices only 12% on proof of citizenship becoming required for federal voter registration, resolving via the White House."
  - "Despite aggressive administration rhetoric and EAC firings, the market prices an 88% chance this specific policy requirement does not take effect."
  - "The low probability suggests markets expect legal or legislative barriers to block implementation, even as executive pressure intensifies."
  - "Resolution depends on a White House action formalizing the requirement; court challenges from states would likely be the primary settlement-delaying mechanism."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump fired all EAC commissioners and administration officials have threatened to arrest state election officials who allow noncitizens to vote, part of a broader push to reshape federal voting rules."
    publisher: "straitstimes.com"
    published_at: "2026-07-10T02:12:41.000Z"
    source_url: "https://www.straitstimes.com/world/united-states/trump-fires-election-assistance-commission-members-ahead-of-midterms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "straitstimes.com"
        source_url: "https://www.straitstimes.com/world/united-states/trump-fires-election-assistance-commission-members-ahead-of-midterms"
        retrieved_at: "2026-07-10T10:49:37+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via the White House; at 12%, the market is clearly fading the administration's voter-roll enforcement rhetoric as a near-term policy outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "straitstimes.com: Trump fires Election Assistance Commission members ahead of midterms |"
    url: "https://www.straitstimes.com/world/united-states/trump-fires-election-assistance-commission-members-ahead-of-midterms"
    published_at: "2026-07-10T02:12:41.000Z"
    retrieved_at: "2026-07-10T10:49:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
