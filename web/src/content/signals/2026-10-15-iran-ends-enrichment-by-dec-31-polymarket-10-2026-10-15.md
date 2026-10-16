---
signal_id: "CMSIG2026101507"
signal_slug: "iran-ends-enrichment-by-dec-31-polymarket-10-2026-10-15"
headline: "Iran ends enrichment by Dec 31: Polymarket 10%"
semantic_title: "Iran ending uranium enrichment by year-end stays at long odds"
telemetry: "Polymarket 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-15T23:44:19.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end enrichment of uranium by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.1
  volume_24h_usd: 2129.1
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 10% on Iran agreeing to end uranium enrichment by December 31, 2026."
  - "The combination of Trump nuclear strike commentary and ongoing diplomacy is consistent with a market that sees a negotiated enrichment halt as unlikely but non-trivial."
  - "A companion Polymarket contract on Congress approving an Iran deal by 2026 (CM-EVT-PB2TWNBNL3) sits at 7%, and a UN Security Council endorsement contract (CM-EVT-1B57MJ14Q5) is at 10%, the suite is aligned in pricing low odds on any full diplomatic resolution."
  - "The CM-EVT-38HGT3RJ52 contract on the U.S. obtaining Iranian enriched uranium saw a 7,209x volume surge day over day, the largest in this entire batch, flagging that Trump's nuclear strike remarks are drawing intense market attention to the enrichment question."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "News coverage includes Trump commentary on a potential Iran nuclear strike alongside ongoing nuclear diplomacy, raising the stakes on enrichment talks."
    publisher: "Express Global Desk"
    published_at: "2026-10-15T23:44:19.000Z"
    source_url: "https://indianexpress.com/article/world/us-iran-war-live-updates-trump-tehran-threat-to-shipping-strait-of-hormuz-saudi-conflict-india-oil-prices-10923782/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Express Global Desk"
        source_url: "https://indianexpress.com/article/world/us-iran-war-live-updates-trump-tehran-threat-to-shipping-strait-of-hormuz-saudi-conflict-india-oil-prices-10923782/"
        retrieved_at: "2026-10-16T12:59:00+00:00"
  - type: "pm_response"
    notes: "Polymarket contract via UMA oracle; the 7,209x volume spike on a related U.S.-Iran uranium-transfer contract is the most significant activity signal across all stories today."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Express Global Desk: World News Today Live Updates: Trump on Iran nuclear strike, Russia’s"
    url: "https://indianexpress.com/article/world/us-iran-war-live-updates-trump-tehran-threat-to-shipping-strait-of-hormuz-saudi-conflict-india-oil-prices-10923782/"
    published_at: "2026-10-15T23:44:19.000Z"
    retrieved_at: "2026-10-16T12:59:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
