---
signal_id: "CMSIG2026061205"
signal_slug: "iran-ends-enrichment-by-june-30-polymarket-21-2026-06-12"
headline: "Iran ends enrichment by June 30: Polymarket 21%"
semantic_title: "Iran uranium enrichment halt by June 30 breaks away at 21 percent"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-12T10:54:39.000Z"
event_id: "CM-EVT-73D6P1DKY8"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-june-30"
event_question: "Will Iran agree to end uranium enrichment by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9d3f02264a94bafc676afd7add8b11442e6ec72dabaa69cefef835f0672275c7"
  question_raw: " Iran agrees to end enrichment of uranium by June 30?"
  current_price: 0.21
  volume_24h_usd: 32831.130789
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket puts only 21% on Iran agreeing to end uranium enrichment by June 30, despite Iran releasing deal-framework details."
  - "The 60-day nuclear talks structure disclosed by Iran implies enrichment decisions are deferred beyond June 30, directly consistent with the low 21% probability."
  - "The broader US-Iran nuclear deal by June 30 contract sits at 28%, the gap between 28% and 21% isolates the specific enrichment-halt condition as the harder ask."
  - "Resolves via UMA oracle; Iran must formally agree to cease all uranium enrichment, not merely enter talks, to settle YES by June 30."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran publicly released details of a proposed deal with Trump including a full ceasefire, 60-day nuclear talks, and a sanctions waiver, but enrichment halt terms remain contested."
    publisher: "firstpost.com"
    published_at: "2026-06-12T10:54:39.000Z"
    source_url: "https://www.firstpost.com/world/us-iran-deal-14-point-mou-full-details-west-asia-war-trump-peace-talks-14021810.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "firstpost.com"
        source_url: "https://www.firstpost.com/world/us-iran-deal-14-point-mou-full-details-west-asia-war-trump-peace-talks-14021810.html"
        retrieved_at: "2026-06-12T11:42:07+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 21% is consistent with the deal's own reported structure, which explicitly defers enrichment decisions into a 60-day negotiation window."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "firstpost.com: Iran releases details of deal with Trump: Full ceasefire, 60-day nucle"
    url: "https://www.firstpost.com/world/us-iran-deal-14-point-mou-full-details-west-asia-war-trump-peace-talks-14021810.html"
    published_at: "2026-06-12T10:54:39.000Z"
    retrieved_at: "2026-06-12T11:42:07+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
