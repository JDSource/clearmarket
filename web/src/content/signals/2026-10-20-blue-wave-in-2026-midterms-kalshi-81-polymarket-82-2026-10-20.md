---
signal_id: "CMSIG2026102005"
signal_slug: "blue-wave-in-2026-midterms-kalshi-81-polymarket-82-2026-10-20"
headline: "Blue wave in 2026 midterms: Kalshi 81%, Polymarket 82%"
semantic_title: "Blue wave in 2026 stays heavily favored two weeks out"
telemetry: "Kalshi 81%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-20T00:00:00.000Z"
event_id: "CM-EVT-QK0HJYVMX2"
event_slug: "kxbluewavecombo-27feb"
event_question: "Will there be a blue wave in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBLUEWAVECOMBO-27FEB"
  question_raw: "Will Democrats hold 218 or more seats in the House after the 2026 midterms AND hold 49 or more seats in the Senate after the 2026 midterms?"
  current_price: 0.81
  volume_24h_usd: 77913.43
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices an 81% probability of a blue wave in 2026; Polymarket independently prices 82%, a rare cross-venue consensus."
  - "Trump's aggressive midterm campaigning is not moving either market; both venues hold near identical high probabilities, showing the rally blitz is being discounted."
  - "Kalshi separately prices a blue tsunami at only 53%, suggesting markets see a strong Democratic outcome as likely but an overwhelming sweep as coin-flip territory."
  - "Kalshi resolves via Bureau of Labor Statistics (unusual resolution source noted); Polymarket resolves via UMA oracle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "With two weeks until Election Day, Trump is barnstorming the country to counter a potential midterm blue wave as NPR reports fever-pitch campaigning."
    publisher: "Stephen Fowler"
    published_at: "2026-10-20T00:00:00.000Z"
    source_url: "https://www.npr.org/2026/10/20/nx-s1-6007867/with-just-two-weeks-until-election-day-midterm-campaigning-reaches-a-fever-pitch"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Stephen Fowler"
        source_url: "https://www.npr.org/2026/10/20/nx-s1-6007867/with-just-two-weeks-until-election-day-midterm-campaigning-reaches-a-fever-pitch"
        retrieved_at: "2026-10-20T13:15:16+00:00"
  - type: "pm_response"
    notes: "Kalshi and Polymarket cross-venue alignment at 81-82% is unusually tight, making this one of the best-corroborated midterm pricing signals available."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Stephen Fowler: With just two weeks until Election Day, midterm campaigning reaches a"
    url: "https://www.npr.org/2026/10/20/nx-s1-6007867/with-just-two-weeks-until-election-day-midterm-campaigning-reaches-a-fever-pitch"
    published_at: "2026-10-20T00:00:00.000Z"
    retrieved_at: "2026-10-20T13:15:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
