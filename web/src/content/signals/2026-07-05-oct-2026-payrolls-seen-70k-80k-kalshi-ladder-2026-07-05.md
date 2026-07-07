---
signal_id: "CMSIG2026070503"
signal_slug: "oct-2026-payrolls-seen-70k-80k-kalshi-ladder-2026-07-05"
headline: "Oct 2026 payrolls seen 70K-80K: Kalshi ladder"
semantic_title: "October payroll pricing holds above labor contraction despite June miss"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-07-05T20:25:30.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.45
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder implies October 2026 payroll additions in the 70,000-80,000 range: 50% above 70K, 45% above 80K, 24% above 100K."
  - "June's 57,000 print is well below the ladder's modal October range, suggesting markets expect a mean-reversion rebound rather than sustained weakness."
  - "The 79% probability above zero and above negative 25K shows near-consensus that October avoids outright contraction, even after the June shock."
  - "Resolution via the Bureau of Labor Statistics October Employment Situation report; the 100K threshold at 24% is the key upside surprise marker to watch."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "June 2026 nonfarm payrolls came in at just 57,000, one of the weakest monthly prints in recent memory, with the unemployment rate holding at 4.2% as the labor force shrank."
    publisher: "finance.biggo.com"
    published_at: "2026-07-05T20:25:30.000Z"
    source_url: "https://finance.biggo.com/news/e2b2479d-ad74-47db-bf75-11a5ce24b089"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "finance.biggo.com"
        source_url: "https://finance.biggo.com/news/e2b2479d-ad74-47db-bf75-11a5ce24b089"
        retrieved_at: "2026-07-07T10:52:00+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder covers October 2026 nonfarm payrolls; the gap between June's 57K print and the October 70K-80K modal range is the market's mean-reversion bet."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "finance.biggo.com: U.S. June Nonfarm Payrolls Plunge to 57,000, Rapidly Cooling Fed Rate"
    url: "https://finance.biggo.com/news/e2b2479d-ad74-47db-bf75-11a5ce24b089"
    published_at: "2026-07-05T20:25:30.000Z"
    retrieved_at: "2026-07-07T10:52:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
