---
signal_id: "CMSIG2026052904"
signal_slug: "strait-of-hormuz-traffic-normal-by-dec-31-polymarket-86-2026-05-29"
headline: "Strait of Hormuz traffic normal by Dec 31: Polymarket 86%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-05-29T08:33:07.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will traffic through the Strait of Hormuz return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.86
  volume_24h_usd: 15118.72909
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31, 2026 sits at 86%, pricing a strong majority probability of resolution well before year-end."
  - "Treasury Secretary Scott Bessent's threat of sanctions and military action against Oman over a potential Iranian tolling system in the Strait is a significant escalation in the Hormuz standoff, yet the 86% Polymarket reading suggests markets still assign high odds to normalization -- implying the threat is read as coercive leverage rather than a harbinger of prolonged disruption."
  - "A shorter-horizon companion Polymarket contract (CM-EVT-4J73Y3RD96) on Hormuz traffic returning to normal by July 31 sits at 63%, meaning the market prices a 23-percentage-point premium for the full-year window over the two-month window -- consistent with a view that talks are ongoing but a quick resolution is uncertain."
  - "A separate near-term Polymarket contract (CM-EVT-5Q8B6RCX69) on Iran agreeing to unrestricted Hormuz shipping by May 31 sits at only 12%, confirming the market sees imminent resolution as unlikely even as longer-term normalization odds remain elevated."
  - "The Polymarket contract resolves via uma_oracle; resolution will require evidence of traffic returning to pre-conflict levels through the Strait, meaning a formal ceasefire alone may not be sufficient if tanker traffic remains disrupted by insurance or logistical constraints."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Trump administration threatened sanctions and military action against Oman after Treasury Secretary Scott Bessent warned the US would aggressively penalize Oman if it helped Iran establish a tolling system in the Strait of Hormuz."
    publisher: "Sam Meredith"
    published_at: "2026-05-29T08:33:07.000Z"
    source_url: "https://www.cnbc.com/2026/05/29/oman-trump-sanctions-iran-war-bessent.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Sam Meredith"
        source_url: "https://www.cnbc.com/2026/05/29/oman-trump-sanctions-iran-war-bessent.html"
        retrieved_at: "2026-05-29T21:01:04+00:00"
  - type: "pm_response"
    notes: "Polymarket's three Hormuz contracts (May 31 at 12%, July 31 at 63%, Dec 31 at 86%) form a term structure showing the market expects normalization in the second half of 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Sam Meredith: Iran war: U.S. threatens sanctions and military action against Oman"
    url: "https://www.cnbc.com/2026/05/29/oman-trump-sanctions-iran-war-bessent.html"
    published_at: "2026-05-29T08:33:07.000Z"
    retrieved_at: "2026-05-29T21:01:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
