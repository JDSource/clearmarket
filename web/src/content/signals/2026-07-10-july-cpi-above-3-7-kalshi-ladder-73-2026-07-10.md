---
signal_id: "CMSIG2026071004"
signal_slug: "july-cpi-above-3-7-kalshi-ladder-73-2026-07-10"
headline: "July CPI above 3.7%: Kalshi ladder 73%"
semantic_title: "CPI above 3.7 percent nears full pricing on inflation repricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-10T13:00:55.000Z"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "CPI inflation rate, year ending July 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.25
  volume_24h_usd: 1363.13
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-10-13T14:00:00Z"
bullets:
  - "Kalshi ladder implies CPI for the year ending July 2026 at 3.70-3.80%, with 73% above 3.70% but only 25% above 3.80%; volume rose 81x day over day."
  - "The inflation pricing sits in direct tension with Standard Chartered's bullish Bitcoin call, which assumes improving risk sentiment and a softer macro backdrop."
  - "A CPI print firming above 3.7% would reinforce the FOMC freeze narrative and undercut the rate-cut assumptions embedded in many year-end crypto bull cases."
  - "Resolves via Bureau of Labor Statistics CPI release; the volume surge suggests traders are actively repositioning around the upcoming print, not waiting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Standard Chartered maintained its year-end Bitcoin target at $100,000, citing improving macro sentiment, even as prediction markets price CPI inflation firming well above 3.5%."
    publisher: "en.bloomingbit.io"
    published_at: "2026-07-10T13:00:55.000Z"
    source_url: "https://en.bloomingbit.io/feed/news/116009"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "en.bloomingbit.io"
        source_url: "https://en.bloomingbit.io/feed/news/116009"
        retrieved_at: "2026-07-11T09:24:13+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder with 81x volume surge is the dominant inflation contract this cycle; the distribution's sharp cutoff above 3.80% sets the key resolution boundary."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "en.bloomingbit.io: Standard Chartered Maintains $100,000 Bitcoin Target for Year-End"
    url: "https://en.bloomingbit.io/feed/news/116009"
    published_at: "2026-07-10T13:00:55.000Z"
    retrieved_at: "2026-07-11T09:24:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
