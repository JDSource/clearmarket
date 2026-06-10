---
signal_id: "CMSIG2026061001"
signal_slug: "us-iran-nuclear-deal-by-jul-31-polymarket-45-2026-06-10"
headline: "US-Iran nuclear deal by Jul 31: Polymarket 45%"
semantic_title: "US-Iran nuclear deal by July 31 wavers at coin-flip pricing"
telemetry: "Polymarket 45%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-10T00:00:00.000Z"
event_id: "CM-EVT-Y2L01CWLW3"
event_slug: "us-iran-nuclear-deal-by-july-31"
event_question: "Will the US and Iran reach a nuclear deal by July 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbdb44ce1624dbf80fe70a96e7cb027b854aa44c52cf87a6bd0bc9ea2c332c3dc"
  question_raw: "US-Iran nuclear deal by July 31?"
  current_price: 0.45
  volume_24h_usd: 6351.02358
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-31T00:00:00Z"
bullets:
  - "Polymarket prices a US-Iran nuclear deal by July 31 at 45%, essentially a coin-flip despite active exchange of strikes."
  - "Active US-Iran military exchange is consistent with deal uncertainty, yet the market has not collapsed below 50%, suggesting traders still see a negotiated path."
  - "The near-term Polymarket contract on an Iran-Oman Strait of Hormuz agreement by June 15 sits at only 6%, signaling near-zero confidence in imminent de-escalation."
  - "Resolves via UMA oracle; any ceasefire announcement or formal deal document before July 31 would trigger resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US and Iran exchanged strikes overnight, jolting their two-month-old truce and endangering ongoing peace negotiations."
    publisher: "Patrick Sykes and Omar Tamo      Wed, June 10, 2026 at 12:25 p.m. GMT+2   4 min read"
    published_at: "2026-06-10T00:00:00.000Z"
    source_url: "https://ca.finance.yahoo.com/news/us-iran-attack-other-over-072210630.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Patrick Sykes and Omar Tamo      Wed, June 10, 2026 at 12:25 p.m. GMT+2   4 min read"
        source_url: "https://ca.finance.yahoo.com/news/us-iran-attack-other-over-072210630.html"
        retrieved_at: "2026-06-10T11:36:47+00:00"
  - type: "pm_response"
    notes: "Polymarket prices the July 31 nuclear deal at 45%, holding well above zero despite active US-Iran strikes, while the June 15 Hormuz side-contract at 6% shows traders see little near-term off-ramp."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Patrick Sykes and Omar Tamo      Wed, June 10, 2026 at 12:25 p.m. GMT+2   4 min read: US, Iran Exchange Strikes, Putting Lasting Peace Deal at Risk"
    url: "https://ca.finance.yahoo.com/news/us-iran-attack-other-over-072210630.html"
    published_at: "2026-06-10T00:00:00.000Z"
    retrieved_at: "2026-06-10T11:36:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
