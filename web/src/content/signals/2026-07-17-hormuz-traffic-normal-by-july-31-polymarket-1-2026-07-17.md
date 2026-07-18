---
signal_id: "CMSIG2026071705"
signal_slug: "hormuz-traffic-normal-by-july-31-polymarket-1-2026-07-17"
headline: "Hormuz traffic normal by July 31: Polymarket 1%"
semantic_title: "Hormuz July normalization collapses near zero at 1 percent"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-17T00:00:00.000Z"
event_id: "CM-EVT-4J73Y3RD96"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-july-31"
event_question: "Will Strait of Hormuz traffic return to normal by July 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb8e6d129a06d0ccb21d7b32eb529ea455eddba3cf29bfa097112202cbdf5bf21"
  question_raw: "Strait of Hormuz traffic returns to normal by July 31?"
  current_price: 0.012
  volume_24h_usd: 305911.33875499974
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by July 31 at just 1%, near-certain rejection of a near-term resolution."
  - "Seven consecutive nights of US strikes on Iranian infrastructure and Iran's retaliatory attacks on US Gulf bases are fully consistent with this pricing."
  - "The December 31 contract on the same question sits at 51% on Polymarket, implying the market sees a possible but uncertain longer-run normalization."
  - "Resolves via Polymarket's UMA oracle confirming whether Hormuz shipping traffic returns to pre-conflict normal levels by July 31."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US struck bridges and other infrastructure in Iran while Tehran targeted US Gulf bases, with Iran calling the Strait of Hormuz a red line as the conflict intensified."
    publisher: "By                  
   
       
      NPR Staff"
    published_at: "2026-07-17T00:00:00.000Z"
    source_url: "https://www.npr.org/2026/07/17/g-s1-134158/us-iran-war-updates"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "By                  
   
       
      NPR Staff"
        source_url: "https://www.npr.org/2026/07/17/g-s1-134158/us-iran-war-updates"
        retrieved_at: "2026-07-18T09:20:01+00:00"
  - type: "pm_response"
    notes: "Polymarket's 1% July versus 51% December spread captures the market's view that near-term normalization is essentially ruled out but year-end resolution remains a coin flip."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "By                  
   
       
      NPR Staff: U.S. strikes bridges in Iran; Tehran targets U.S. bases in the Gulf  :"
    url: "https://www.npr.org/2026/07/17/g-s1-134158/us-iran-war-updates"
    published_at: "2026-07-17T00:00:00.000Z"
    retrieved_at: "2026-07-18T09:20:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
