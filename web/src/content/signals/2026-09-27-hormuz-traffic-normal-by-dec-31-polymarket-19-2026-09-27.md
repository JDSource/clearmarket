---
signal_id: "CMSIG2026092704"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-19-2026-09-27"
headline: "Hormuz traffic normal by Dec 31: Polymarket 19%"
semantic_title: "Hormuz traffic back to normal by year-end stays unlikely"
telemetry: "Polymarket 19%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-27T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.19
  volume_24h_usd: 114212.02400599999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts just 19% on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Iran's refusal to back down after Trump's rejection is consistent with the market's skeptical pricing, both sides remain far apart, and the market is not treating a year-end deal as a base case."
  - "The Kalshi contract on the US reopening its embassy in Iran sits at only 4%, with volume up 1553x day-over-day, signaling a sharp spike in attention on Iran-related resolution risk."
  - "The Polymarket contract resolves via UMA oracle, likely on publicly verifiable transit data; the definition of 'normal' traffic levels is a key settlement edge case given disrupted baseline."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran stood firm Sunday on its conditions for reopening the Strait of Hormuz after Trump rejected the foreign minister's seven-day plan, leaving no deal framework in place."
    publisher: "afp.com"
    published_at: "2026-09-27T00:00:00.000Z"
    source_url: "https://www.afp.com/en/iran-stands-firm-hormuz-plan-after-us-rejection"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "afp.com"
        source_url: "https://www.afp.com/en/iran-stands-firm-hormuz-plan-after-us-rejection"
        retrieved_at: "2026-09-27T13:30:43+00:00"
  - type: "pm_response"
    notes: "Polymarket at 19% and the embassy contract at 4% on Kalshi paint a consistent picture: the market sees no near-term diplomatic breakthrough despite Iran's stated desire for a deal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "afp.com: Iran stands firm on Hormuz plan after US rejection | AFP.com"
    url: "https://www.afp.com/en/iran-stands-firm-hormuz-plan-after-us-rejection"
    published_at: "2026-09-27T00:00:00.000Z"
    retrieved_at: "2026-09-27T13:30:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
