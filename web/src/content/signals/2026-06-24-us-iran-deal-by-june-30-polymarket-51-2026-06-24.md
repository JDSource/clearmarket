---
signal_id: "CMSIG2026062401"
signal_slug: "us-iran-deal-by-june-30-polymarket-51-2026-06-24"
headline: "US-Iran deal by June 30: Polymarket 51%"
semantic_title: "US-Iran nuclear deal by June 30 wavers on inspection dispute"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T14:18:24.000Z"
event_id: "CM-EVT-LG47Z78CF2"
event_slug: "us-iran-nuclear-deal-by-june-30"
event_question: "Will the US and Iran reach a nuclear deal by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa70fc3695a65833b91b45df6db6015096f3e1471b70352ca411b4209010e7633"
  question_raw: "US-Iran nuclear deal by June 30?"
  current_price: 0.51
  volume_24h_usd: 1088905.717404001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices a US-Iran nuclear deal by June 30 at 51%, essentially a coin-flip on the near-term deadline."
  - "IAEA head Rafael Grossi says inspections are coming; Iran's diplomat says only after a final deal, the contradiction directly threatens the June 30 timeline."
  - "The July 31 Polymarket contract sits at 59% and the pre-2027 contract at 71%, showing the market sees a deal as likely eventually but doubts the June 30 close."
  - "Resolves via Polymarket uma_oracle assessing whether a formal nuclear deal is reached by June 30; inspection disputes are a classic pre-deadline stall risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "IAEA chief says nuclear site inspections will happen under the interim ceasefire deal, but Tehran insists inspections require a final deal first, creating a key sticking point."
    publisher: "military.com"
    published_at: "2026-06-24T14:18:24.000Z"
    source_url: "https://www.military.com/un-nuclear-boss-says-inspectors-will-visit-iran-sites-tehran-says-only-after-a-final-deal"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "military.com"
        source_url: "https://www.military.com/un-nuclear-boss-says-inspectors-will-visit-iran-sites-tehran-says-only-after-a-final-deal"
        retrieved_at: "2026-06-25T10:38:54+00:00"
  - type: "pm_response"
    notes: "Polymarket prices near-term deal risk as a pure toss-up, consistent with active but unresolved negotiations."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "military.com: UN Nuclear Boss Says Inspectors Will Visit Iran Sites. Tehran Says Onl"
    url: "https://www.military.com/un-nuclear-boss-says-inspectors-will-visit-iran-sites-tehran-says-only-after-a-final-deal"
    published_at: "2026-06-24T14:18:24.000Z"
    retrieved_at: "2026-06-25T10:38:54+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
