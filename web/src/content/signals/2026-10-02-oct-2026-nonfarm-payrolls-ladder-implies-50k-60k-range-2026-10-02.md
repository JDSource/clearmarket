---
signal_id: "CMSIG2026100202"
signal_slug: "oct-2026-nonfarm-payrolls-ladder-implies-50k-60k-range-2026-10-02"
headline: "Oct 2026 nonfarm payrolls: ladder implies 50K-60K range"
semantic_title: "October payrolls implied range holds at 50K-60K"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-02T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payroll change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T60000"
  question_raw: "Will above 60000 jobs be added in October 2026?"
  current_price: 0.46
  volume_24h_usd: 15.2
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "The payroll ladder prices the October 2026 nonfarm change in the 50,000-60,000 range: 67% above 30K, 60% above 40K, dropping to 46% above 60K."
  - "September's 29,000 print missed estimates sharply; the ladder suggests markets expect a modest October rebound but not a return to strong growth."
  - "The sharp right-tail drop, only 22% above 100K and 19% above 125K, indicates very low market confidence in a strong October recovery."
  - "The September positive-growth contract (CM-EVT-MZQH465PC3) saw trading volume surge roughly 9,950 times day-over-day, signaling intense fresh attention on the jobs theme heading into October."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The September jobs report showed only 29,000 payrolls added, well below estimates, sending stocks and bonds higher and cooling Fed rate-hike expectations."
    publisher: "lse.co.uk"
    published_at: "2026-10-02T00:00:00.000Z"
    source_url: "https://www.lse.co.uk/news/instant-view-soft-september-jobs-report-sends-markets-higher-u26fsa0o1v5oiw3.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "lse.co.uk"
        source_url: "https://www.lse.co.uk/news/instant-view-soft-september-jobs-report-sends-markets-higher-u26fsa0o1v5oiw3.html"
        retrieved_at: "2026-10-02T14:25:25+00:00"
  - type: "pm_response"
    notes: "The ladder distribution is drawn from prediction market strike probabilities; no single-venue binary price is available for October payrolls."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "lse.co.uk: INSTANT VIEW-Soft September jobs report sends markets higher | Financi"
    url: "https://www.lse.co.uk/news/instant-view-soft-september-jobs-report-sends-markets-higher-u26fsa0o1v5oiw3.html"
    published_at: "2026-10-02T00:00:00.000Z"
    retrieved_at: "2026-10-02T14:25:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
