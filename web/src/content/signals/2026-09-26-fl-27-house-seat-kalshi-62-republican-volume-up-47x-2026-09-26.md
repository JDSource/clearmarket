---
signal_id: "CMSIG2026092606"
signal_slug: "fl-27-house-seat-kalshi-62-republican-volume-up-47x-2026-09-26"
headline: "FL-27 House seat: Kalshi 62% Republican, volume up 47x"
semantic_title: "FL-27 House race near 50%, drawing surge in fresh attention"
telemetry: "Kalshi 62%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-26T00:00:00.000Z"
event_id: "CM-EVT-RTW7ZKGKR3"
event_slug: "kxhouserace-fl27-26"
event_question: "Will the Republican or Democratic candidate win the FL-27 House seat in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL27-26-R"
  question_raw: "Will Republican win the House race for FL-27?"
  current_price: 0.62
  volume_24h_usd: 91.03
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices the Republican candidate winning FL-27 at 62%, with trading volume up 4,616% day over day, 47 times the prior session."
  - "Trump's record-low pre-midterm approval is drawing market attention to competitive seats like FL-27, where Republican odds sit only modestly above a coin flip."
  - "The volume surge signals the FL-27 contract is attracting significant fresh positioning, likely as traders reassess GOP exposure given the polling backdrop."
  - "A companion Polymarket contract (CM-EVT-7RNJ53L5L5) puts 94% on the Democrat winning Massachusetts 2nd, illustrating how partisan polarization is shaping district-level pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump's approval rating has dropped to 37%, the lowest for any president heading into midterms since 1990, raising questions about Republican vulnerability in competitive House districts."
    publisher: "newsweek.com"
    published_at: "2026-09-26T00:00:00.000Z"
    source_url: "https://www.newsweek.com/trump-approval-lowest-president-midterms-wsj-poll-12493499"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "newsweek.com"
        source_url: "https://www.newsweek.com/trump-approval-lowest-president-midterms-wsj-poll-12493499"
        retrieved_at: "2026-09-28T07:47:41+00:00"
  - type: "pm_response"
    notes: "Kalshi resolves via Library of Congress official election certification; results may lag election night by days or weeks if a race is contested."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "newsweek.com: Trump Approval Lowest for Any President Pre-Midterms Since 1990: WSJ P"
    url: "https://www.newsweek.com/trump-approval-lowest-president-midterms-wsj-poll-12493499"
    published_at: "2026-09-26T00:00:00.000Z"
    retrieved_at: "2026-09-28T07:47:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
