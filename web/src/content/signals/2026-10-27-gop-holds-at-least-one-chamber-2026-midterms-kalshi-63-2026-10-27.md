---
signal_id: "CMSIG2026102704"
signal_slug: "gop-holds-at-least-one-chamber-2026-midterms-kalshi-63-2026-10-27"
headline: "GOP holds at least one chamber, 2026 midterms: Kalshi 63%"
semantic_title: "Republican Chamber control after midterms holds near 63 percent"
telemetry: "Kalshi 63%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-27T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.63
  volume_24h_usd: 597536.09
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices 63% on Republicans controlling at least one chamber of Congress after the 2026 midterms."
  - "ABC News reports high early-voting turnout with competitive Senate and House races, consistent with a market that sees GOP control as more likely than not but far from certain."
  - "A companion Kalshi contract (CM-EVT-4DFCBXLZN6) prices 73% on Republicans holding more governorships than Democrats, suggesting markets see GOP strength more clearly at the state than federal level."
  - "Resolves via Bureau of Labor Statistics designation as named resolution source; settlement follows official certified election results."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "With one week until the November 3 midterms, early voting has surged and key House and Senate races remain competitive."
    publisher: "ABC NEWS"
    published_at: "2026-10-27T00:00:00.000Z"
    source_url: "https://www.goodmorningamerica.com/news/live-updates/midterm-elections-2026-1-week-high-stakes-elections-137578278"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC NEWS"
        source_url: "https://www.goodmorningamerica.com/news/live-updates/midterm-elections-2026-1-week-high-stakes-elections-137578278"
        retrieved_at: "2026-10-28T07:49:08+00:00"
  - type: "pm_response"
    notes: "Kalshi at 63% reflects a competitive but Republican-leaning outlook one week out; the governor contract at 73% on the same venue shows a wider GOP advantage at the state level."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC NEWS: Midterm elections live updates: 1 week until high-stakes elections - G"
    url: "https://www.goodmorningamerica.com/news/live-updates/midterm-elections-2026-1-week-high-stakes-elections-137578278"
    published_at: "2026-10-27T00:00:00.000Z"
    retrieved_at: "2026-10-28T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
