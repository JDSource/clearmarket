---
signal_id: "CMSIG2026111306"
signal_slug: "un-security-council-iran-deal-resolution-by-dec-polymarket-5-2026-11-13"
headline: "UN Security Council Iran deal resolution by Dec: Polymarket 5%"
semantic_title: "UN Security Council Iran deal endorsement stays a long shot at 5 percent"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-13T00:00:00.000Z"
event_id: "CM-EVT-1B57MJ14Q5"
event_slug: "will-the-unsc-adopt-a-resolution-endorsing-the-final-us-iran-deal-by-date"
event_question: "Will the UN Security Council pass a resolution endorsing a final U.S.-Iran deal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0c7245047183848e41555dc9a5ccc14c970a0711a3591bebc8310119cbae64c0"
  question_raw: "UNSC Resolution Endorsing Final U.S.-Iran Deal by December 31?"
  current_price: 0.05
  volume_24h_usd: 1579.08
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on the UN Security Council passing a resolution endorsing a final US-Iran deal by December sits at 5%, a long shot."
  - "Ongoing Iranian strikes on US assets in Bahrain and broader regional fighting are consistent with the low 5% pricing; no diplomatic breakthrough is priced as likely."
  - "Trading volume on this contract surged 467.8x day over day, flagging dramatically heightened attention likely tied to the Trump-Xi-Putin APEC summit, which is reportedly set to include Iran war discussions."
  - "Resolves via UMA oracle; requires both a US-Iran deal and a formal UN Security Council resolution by December 31."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Al Jazeera reports Iran targeted a US asset in Bahrain while Qatar and Turkey signed a mutual defense pact, with fighting continuing in Yemen as the US-Israel war on Iran grinds on."
    publisher: "Enes Abuomer, Mahmoud Sayed, Edna Mohamed, Chris Hamill-Stewart, Barbara Angopa"
    published_at: "2026-11-13T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/liveblog/2026/11/13/iran-war-live-riyadh-china-discuss-houthis-as-group-claims-aramco-attacks"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Enes Abuomer, Mahmoud Sayed, Edna Mohamed, Chris Hamill-Stewart, Barbara Angopa"
        source_url: "https://www.aljazeera.com/news/liveblog/2026/11/13/iran-war-live-riyadh-china-discuss-houthis-as-group-claims-aramco-attacks"
        retrieved_at: "2026-11-14T07:47:51+00:00"
  - type: "pm_response"
    notes: "Polymarket at 5% with an extraordinary volume spike is the clearest signal of renewed market focus on Iran diplomacy; current price remains a long shot despite the attention."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Enes Abuomer, Mahmoud Sayed, Edna Mohamed, Chris Hamill-Stewart, Barbara Angopa: Iran war updates: Qatar, Turkiye ink defence deal; fighting rages in Y"
    url: "https://www.aljazeera.com/news/liveblog/2026/11/13/iran-war-live-riyadh-china-discuss-houthis-as-group-claims-aramco-attacks"
    published_at: "2026-11-13T00:00:00.000Z"
    retrieved_at: "2026-11-14T07:47:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
