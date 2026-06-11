---
signal_id: "CMSIG2026061104"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-76-2026-06-11"
headline: "Hormuz traffic normal by Dec 31: Polymarket 76%"
semantic_title: "Hormuz traffic normalization by year-end holds majority pricing"
telemetry: "Polymarket 76%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-11T09:14:02.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will traffic through the Strait of Hormuz return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.76
  volume_24h_usd: 24270.863375000004
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 76% on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Tehran's closure claim and second-day US strikes represent active conflict, yet the market holds a clear majority on resolution by year-end, implying capital-weighted expectation of eventual diplomatic or military de-escalation within six months."
  - "A companion Polymarket contract prices only 13% on Iran agreeing to unrestricted Hormuz shipping by June 30, revealing a large near-term versus long-term spread: the market bets on resolution but not quickly."
  - "Resolves via IMF PortWatch shipping traffic data at portwatch.imf.org; the definition of 'normal' traffic is the key settlement edge case given potential partial reopening scenarios."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US and Iran exchanged fire for a second consecutive day as Tehran claimed closure of the Strait of Hormuz, threatening a fragile ceasefire and global energy shipping routes."
    publisher: "Macarena Vidal Liy"
    published_at: "2026-06-11T09:14:02.000Z"
    source_url: "https://english.elpais.com/international/2026-06-11/exchange-of-fire-between-us-and-iran-marks-beginning-of-a-dangerous-new-phase-in-the-war.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Macarena Vidal Liy"
        source_url: "https://english.elpais.com/international/2026-06-11/exchange-of-fire-between-us-and-iran-marks-beginning-of-a-dangerous-new-phase-in-the-war.html"
        retrieved_at: "2026-06-11T12:08:11+00:00"
  - type: "pm_response"
    notes: "Polymarket's 76% on year-end Hormuz normalization contrasts sharply with 13% on a June 30 deal, reflecting strong conviction in eventual resolution but deep skepticism about near-term diplomacy."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Macarena Vidal Liy: Exchange of fire between US and Iran marks beginning of a dangerous ne"
    url: "https://english.elpais.com/international/2026-06-11/exchange-of-fire-between-us-and-iran-marks-beginning-of-a-dangerous-new-phase-in-the-war.html"
    published_at: "2026-06-11T09:14:02.000Z"
    retrieved_at: "2026-06-11T12:08:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
