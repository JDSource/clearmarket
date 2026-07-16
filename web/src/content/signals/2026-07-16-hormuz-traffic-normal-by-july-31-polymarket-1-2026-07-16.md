---
signal_id: "CMSIG2026071602"
signal_slug: "hormuz-traffic-normal-by-july-31-polymarket-1-2026-07-16"
headline: "Hormuz traffic normal by July 31: Polymarket 1%"
semantic_title: "Hormuz normalization by July 31 nears zero pricing"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-16T04:42:00.000Z"
event_id: "CM-EVT-4J73Y3RD96"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-july-31"
event_question: "Will Strait of Hormuz traffic return to normal by July 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb8e6d129a06d0ccb21d7b32eb529ea455eddba3cf29bfa097112202cbdf5bf21"
  question_raw: "Strait of Hormuz traffic returns to normal by July 31?"
  current_price: 0.012
  volume_24h_usd: 211521.35014099974
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-31T00:00:00Z"
bullets:
  - "Polymarket prices only 1% on Strait of Hormuz traffic returning to normal by July 31, essentially fully rejecting near-term resolution."
  - "Active US strikes on northern Iran and Iranian retaliation against US bases in Bahrain, Kuwait, and Jordan are consistent with this near-zero pricing."
  - "The December 31 Polymarket contract on the same question sits at 57%, revealing sharp term-structure doubt concentrated in the next six weeks."
  - "The 56-percentage-point gap between the July and December contracts indicates markets price significant but not certain longer-run de-escalation."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US launched multiple strikes on Iran targeting missile sites, air defenses and command centers while Iran retaliated against US bases in the region, intensifying the naval blockade."
    publisher: "geo.tv"
    published_at: "2026-07-16T04:42:00.000Z"
    source_url: "https://www.geo.tv/latest/673279-us-launches-multiple-strikes-on-iran-tehran-targets-american-bases-in-region"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "geo.tv"
        source_url: "https://www.geo.tv/latest/673279-us-launches-multiple-strikes-on-iran-tehran-targets-american-bases-in-region"
        retrieved_at: "2026-07-16T10:04:17+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via UMA oracle; the July 31 contract at 1% vs December 31 at 57% is the cleanest term-structure read available on Hormuz reopening probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "geo.tv: US launches multiple strikes on Iran, Tehran targets American bases in"
    url: "https://www.geo.tv/latest/673279-us-launches-multiple-strikes-on-iran-tehran-targets-american-bases-in-region"
    published_at: "2026-07-16T04:42:00.000Z"
    retrieved_at: "2026-07-16T10:04:17+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
