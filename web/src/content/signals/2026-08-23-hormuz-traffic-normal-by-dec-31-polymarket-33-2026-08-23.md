---
signal_id: "CMSIG2026082306"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-33-2026-08-23"
headline: "Hormuz traffic normal by Dec 31: Polymarket 33%"
semantic_title: "Strait of Hormuz reopening by year-end stays a long shot"
telemetry: "Polymarket 33%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-23T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.33
  volume_24h_usd: 146477.760731
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices Strait of Hormuz traffic returning to normal by December 31 at 33%, keeping full reopening a distinct minority outcome."
  - "U.S. sanctions escalation and Iran's defiant posture are consistent with this below-50% reading; China's diplomatic backing for talks is the main upside risk the market is partially pricing."
  - "At 33%, the market is not ruling out a resolution, Pakistan's mediation role and Egypt's parallel diplomacy keep the tail alive."
  - "Resolves via UMA oracle; 'normal' traffic is likely defined against a pre-conflict baseline, creating potential dispute risk at settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "China backed diplomatic talks with Iran as the U.S. prepared sweeping new sanctions under 'Operation Economic Outcast,' keeping Strait of Hormuz disruption at the center of global trade risk."
    publisher: "Randy Thanthong-Knight"
    published_at: "2026-08-23T00:00:00.000Z"
    source_url: "https://www.bloomberg.com/news/articles/2026-08-23/china-actively-committed-to-iran-talks-with-tensions-rising"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Randy Thanthong-Knight"
        source_url: "https://www.bloomberg.com/news/articles/2026-08-23/china-actively-committed-to-iran-talks-with-tensions-rising"
        retrieved_at: "2026-08-25T08:36:45+00:00"
  - type: "pm_response"
    notes: "Polymarket hosts this year-end contract at 33%; no near-term companion contract has a live price, leaving the full timeline risk concentrated in this single year-end read."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Randy Thanthong-Knight: China Backs Diplomatic Talks With Iran as US Prepares New Sanctions -"
    url: "https://www.bloomberg.com/news/articles/2026-08-23/china-actively-committed-to-iran-talks-with-tensions-rising"
    published_at: "2026-08-23T00:00:00.000Z"
    retrieved_at: "2026-08-25T08:36:45+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
