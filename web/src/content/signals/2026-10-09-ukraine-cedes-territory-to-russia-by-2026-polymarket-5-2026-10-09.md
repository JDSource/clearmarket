---
signal_id: "CMSIG2026100907"
signal_slug: "ukraine-cedes-territory-to-russia-by-2026-polymarket-5-2026-10-09"
headline: "Ukraine cedes territory to Russia by 2026: Polymarket 5%"
semantic_title: "Ukraine ceding territory to Russia by year-end stays a long shot"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-09T07:14:17.000Z"
event_id: "CM-EVT-XP7FFT2MC9"
event_slug: "will-ukraine-agree-to-cede-territory-to-russia-before-2027"
event_question: "Will Ukraine agree to cede territory to Russia by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x21bf9a7dae81b6bd51acae73185686ab8997b81b1401e4be10e114d472599c26"
  question_raw: "Will Ukraine agree to cede territory to Russia before 2027?"
  current_price: 0.05
  volume_24h_usd: 1553.4099999999999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 5% on Ukraine agreeing to cede territory to Russia by end of 2026."
  - "The Miami talks signal active diplomacy, but the near-zero probability reflects markets seeing a formal territorial concession by year-end as highly unlikely despite the negotiations."
  - "The Polymarket contract on Trump, Putin, and Zelensky meeting together before 2027 sits at just 5%, suggesting markets see even the preconditions for a settlement as remote."
  - "Resolves via UMA oracle; a formal, publicly announced Ukrainian agreement to cede specific territory would be required to settle YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US, Ukrainian, and European officials gathered in Miami to discuss new proposals for breaking the war stalemate amid ongoing Russian strikes killing dozens."
    publisher: "Alex Raufoglu"
    published_at: "2026-10-09T07:14:17.000Z"
    source_url: "https://www.rferl.org/a/us-ukraine-talks-miami-russian-air-strikes/33873365.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Alex Raufoglu"
        source_url: "https://www.rferl.org/a/us-ukraine-talks-miami-russian-air-strikes/33873365.html"
        retrieved_at: "2026-10-09T07:48:13+00:00"
  - type: "pm_response"
    notes: "Polymarket at 5% shows diplomacy in Miami has not shifted market pricing on territorial concession; long-shot pricing holds despite high-level talks."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Alex Raufoglu: US, Ukraine Set For Talks In Miami Amid Onslaught Of Russian Air Strik"
    url: "https://www.rferl.org/a/us-ukraine-talks-miami-russian-air-strikes/33873365.html"
    published_at: "2026-10-09T07:14:17.000Z"
    retrieved_at: "2026-10-09T07:48:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
