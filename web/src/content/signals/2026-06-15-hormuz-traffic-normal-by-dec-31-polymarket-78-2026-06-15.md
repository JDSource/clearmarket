---
signal_id: "CMSIG2026061504"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-78-2026-06-15"
headline: "Hormuz traffic normal by Dec 31: Polymarket 78%"
semantic_title: "Strait of Hormuz normal traffic by year-end solidifies above consensus"
telemetry: "Polymarket 78%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-15T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will traffic through the Strait of Hormuz return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.78
  volume_24h_usd: 289674.7514719999
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 78% probability that Strait of Hormuz traffic returns to normal by December 31."
  - "The deal framework includes Hormuz reopening, making the 78% year-end read broadly consistent with the news, though details remain murky."
  - "The near-term June contract (CM-EVT-YPW93GCTK6) prices only 18% for normal traffic by end of June, showing markets see a drawn-out implementation timeline."
  - "Resolves via portwatch.imf.org shipping data; normal traffic requires observable throughput recovery, not just a political announcement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A US-Iran interim agreement includes reopening the Strait of Hormuz, but implementation details and Israeli operations in Lebanon remain unresolved."
    publisher: "JON GAMBRELL, ELENA BECATOROS and MICHELLE L. PRICE Associated Press"
    published_at: "2026-06-15T00:00:00.000Z"
    source_url: "https://www.lite.aol.com/politics/story/0001/20260615/77406473da38c6c126818610a219dc20"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "JON GAMBRELL, ELENA BECATOROS and MICHELLE L. PRICE Associated Press"
        source_url: "https://www.lite.aol.com/politics/story/0001/20260615/77406473da38c6c126818610a219dc20"
        retrieved_at: "2026-06-16T12:50:14+00:00"
  - type: "pm_response"
    notes: "Polymarket's June versus December Hormuz contracts reveal a sharp near-term discount: the formal signing and implementation gap is the dominant risk priced in."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "JON GAMBRELL, ELENA BECATOROS and MICHELLE L. PRICE Associated Press: Initial deal to end US-Iran war moves toward formal signing despite li"
    url: "https://www.lite.aol.com/politics/story/0001/20260615/77406473da38c6c126818610a219dc20"
    published_at: "2026-06-15T00:00:00.000Z"
    retrieved_at: "2026-06-16T12:50:14+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
