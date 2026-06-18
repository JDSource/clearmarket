---
signal_id: "CMSIG2026061806"
signal_slug: "iran-ends-uranium-enrichment-by-dec-31-polymarket-46-2026-06-18"
headline: "Iran ends uranium enrichment by Dec 31: Polymarket 46%"
semantic_title: "Iran enrichment end by December pricing holds near a coin flip"
telemetry: "Polymarket 46%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-18T00:00:00.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end uranium enrichment by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.46
  volume_24h_usd: 9462.239892
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market prices 46% on Iran agreeing to end uranium enrichment by December 31, 2026."
  - "Republican criticism of the MoU and unresolved technical gaps are consistent with a market that refuses to price a done deal despite the Islamabad signing ceremony."
  - "The deal calls for diluting Iran's highly enriched uranium stockpile at minimum, stopping short of full enrichment cessation, which the 54% no-pricing reflects."
  - "The June 30 enrichment-end contract (CM-EVT-73D6P1DKY8) sits at only 24%, revealing the market assigns far higher probability to a December outcome than a June one, a clear term structure discount."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Republican backlash to Trump's Iran MoU and ongoing technical issues indicate the path to a full uranium enrichment halt remains contested and uncertain."
    publisher: "Erin Hale"
    published_at: "2026-06-18T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/6/18/trumps-iran-framework-draws-backlash-from-some-republicans"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Erin Hale"
        source_url: "https://www.aljazeera.com/news/2026/6/18/trumps-iran-framework-draws-backlash-from-some-republicans"
        retrieved_at: "2026-06-18T11:48:44+00:00"
  - type: "pm_response"
    notes: "The Polymarket contract resolves via uma_oracle; the distinction between dilution of existing stockpiles and a formal enrichment halt is likely a key resolution edge case."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Erin Hale: Trump’s MoU with Iran draws backlash from some Republicans | US-Israel"
    url: "https://www.aljazeera.com/news/2026/6/18/trumps-iran-framework-draws-backlash-from-some-republicans"
    published_at: "2026-06-18T00:00:00.000Z"
    retrieved_at: "2026-06-18T11:48:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
