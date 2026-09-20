---
signal_id: "CMSIG2026092007"
signal_slug: "trump-approval-below-37-ladder-implies-74-odds-2026-09-20"
headline: "Trump approval below 37%: ladder implies 74% odds"
semantic_title: "Trump approval below 37 percent seen likely as Mideast risk builds"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-20T00:00:00.000Z"
event_id: "CM-EVT-0DMSQTKVX3"
event_slug: "kxtrumpapprovalbelow-26dec31"
event_question: "Trump approval rating floor during measurement period"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALBELOW-26DEC31-33"
  question_raw: "Will Donald Trump's approval rating on approval rating be below 33% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.1
  volume_24h_usd: 142.16
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "The ladder prices 74% odds Trump's approval stays below 37%, with volume up 71x day over day, signaling intense fresh attention on this contract."
  - "Houthi ballistic missile attack on Riyadh and US warnings of rapid escalation are the likely catalyst driving the volume surge on the approval floor contract."
  - "The distribution shows only 10% odds approval falls below 33%, suggesting the market sees a floor around the 34-36% range, not a collapse."
  - "A companion Polymarket contract on Trump ceasing to be president before 2027 holds at just 5%, indicating the approval pressure is not being read as an existential political risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US warned of rapid Mideast escalation after Houthis fired a ballistic missile at Riyadh, adding geopolitical pressure on the administration."
    publisher: "afp.com"
    published_at: "2026-09-20T00:00:00.000Z"
    source_url: "https://www.afp.com/en/us-fears-rapid-escalation-mideast-after-houthis-attack-riyadh"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "afp.com"
        source_url: "https://www.afp.com/en/us-fears-rapid-escalation-mideast-after-houthis-attack-riyadh"
        retrieved_at: "2026-09-20T07:47:17+00:00"
  - type: "pm_response"
    notes: "Volume on the ladder jumped 71x day over day, making this one of the most actively traded approval contracts in the dataset; resolution methodology and pollster sourcing should be confirmed before trading."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "afp.com: US fears rapid escalation in Mideast after Houthis attack Riyadh | AFP"
    url: "https://www.afp.com/en/us-fears-rapid-escalation-mideast-after-houthis-attack-riyadh"
    published_at: "2026-09-20T00:00:00.000Z"
    retrieved_at: "2026-09-20T07:47:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
