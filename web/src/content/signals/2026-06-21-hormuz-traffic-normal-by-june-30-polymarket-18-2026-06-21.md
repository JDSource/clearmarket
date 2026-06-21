---
signal_id: "CMSIG2026062102"
signal_slug: "hormuz-traffic-normal-by-june-30-polymarket-18-2026-06-21"
headline: "Hormuz traffic normal by June 30: Polymarket 18%"
semantic_title: "Hormuz June reopening consensus wavers near slim odds"
telemetry: "Polymarket 18%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-21T00:22:00.000Z"
event_id: "CM-EVT-YPW93GCTK6"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-end-of-june"
event_question: "Will traffic through the Strait of Hormuz return to normal by the end of June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x348cd9adf4f6855f58bd9c6dbf9ff251c4142ef77233a5dc95c65b4b61cd2187"
  question_raw: "Strait of Hormuz traffic returns to normal by end of June?"
  current_price: 0.18
  volume_24h_usd: 2192769.440225002
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "The Polymarket contract prices only 18% odds that Strait of Hormuz traffic returns to normal by end of June, resolving via portwatch.imf.org shipping data."
  - "Iran's active Hormuz closure threats heading into the talks are consistent with the low near-term probability, markets do not expect a shipping breakthrough this month."
  - "The December 31 companion Polymarket contract prices at 78%, showing the market sees eventual normalization as likely but not in the current negotiating window."
  - "The June 30 contract for Iran agreeing to unrestricted Hormuz shipping prices at 31%, higher than the traffic normalization contract, suggesting markets see an agreement as possible but implementation as slower."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran threatened renewed Hormuz closure as US and Iranian delegations convened in Switzerland for high-stakes nuclear and shipping talks."
    publisher: "straitstimes.com"
    published_at: "2026-06-21T00:22:00.000Z"
    source_url: "https://www.straitstimes.com/world/middle-east/us-disputes-iranian-claims-about-closing-strait-of-hormuz-as-negotiators-head-to-switzerland"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "straitstimes.com"
        source_url: "https://www.straitstimes.com/world/middle-east/us-disputes-iranian-claims-about-closing-strait-of-hormuz-as-negotiators-head-to-switzerland"
        retrieved_at: "2026-06-21T11:13:58+00:00"
  - type: "pm_response"
    notes: "Polymarket's 18% June versus 78% December spread on Hormuz normalization frames the talks as a medium-term catalyst, not an immediate resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "straitstimes.com: Vance arrives in Switzerland for Iran peace talks with Hormuz in spotl"
    url: "https://www.straitstimes.com/world/middle-east/us-disputes-iranian-claims-about-closing-strait-of-hormuz-as-negotiators-head-to-switzerland"
    published_at: "2026-06-21T00:22:00.000Z"
    retrieved_at: "2026-06-21T11:13:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
