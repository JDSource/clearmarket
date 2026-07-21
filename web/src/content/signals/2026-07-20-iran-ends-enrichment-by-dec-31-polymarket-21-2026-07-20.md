---
signal_id: "CMSIG2026072005"
signal_slug: "iran-ends-enrichment-by-dec-31-polymarket-21-2026-07-20"
headline: "Iran ends enrichment by Dec 31: Polymarket 21%"
semantic_title: "Iran uranium enrichment halt by year-end holds below 25%"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-20T00:00:00.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end enrichment of uranium by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.21
  volume_24h_usd: 13368.293736000001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 21% probability that Iran agrees to end uranium enrichment by December 31, 2026."
  - "Nine straight nights of US airstrikes and Khamenei rejecting ceasefire terms are consistent with the low 21% probability; talks have collapsed."
  - "The Polymarket contract on Iranian regime survival (CM-EVT-QNQ4VPVP80) sits at 10% for regime fall before 2027, suggesting the market prices continued conflict rather than resolution."
  - "Resolves via Polymarket UMA oracle; the enrichment halt must be formally agreed and verifiable to settle YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US carried out its ninth consecutive night of airstrikes on Iran, with Khamenei calling ceasefire talks worthless as Hormuz tensions escalate."
    publisher: "Al Jazeera Staff"
    published_at: "2026-07-20T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/7/20/us-bombs-iran-for-ninth-consecutive-night-as-hormuz-tensions-escalate"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/7/20/us-bombs-iran-for-ninth-consecutive-night-as-hormuz-tensions-escalate"
        retrieved_at: "2026-07-21T10:22:25+00:00"
  - type: "pm_response"
    notes: "Polymarket at 21% on enrichment halt; the companion regime-fall contract at 10% creates a coherent picture: market sees Iran persisting under pressure, with talks but no deal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: US bombs Iran for ninth consecutive night as Hormuz tensions escalate"
    url: "https://www.aljazeera.com/news/2026/7/20/us-bombs-iran-for-ninth-consecutive-night-as-hormuz-tensions-escalate"
    published_at: "2026-07-20T00:00:00.000Z"
    retrieved_at: "2026-07-21T10:22:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
