---
signal_id: "CMSIG2026110305"
signal_slug: "trump-putin-zelensky-together-before-2027-polymarket-3-2026-11-03"
headline: "Trump, Putin, Zelensky together before 2027: Polymarket 3%"
semantic_title: "Trump-Putin-Zelensky summit stays a very long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-03T00:00:00.000Z"
event_id: "CM-EVT-QP1YL1BSS0"
event_slug: "trump-putin-and-zelensky-seen-together-before-2027"
event_question: "Will Trump, Putin, and Zelensky be seen together before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa04dcb7b7f5a313d09e7728ca39835be4096da877ca5fbae5e3a36af239433c3"
  question_raw: "Trump, Putin, and Zelensky seen together before 2027?"
  current_price: 0.03
  volume_24h_usd: 389.57
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Trump-Putin-Zelensky in-person summit before 2027 at just 3%."
  - "Mediated indirect talks via Abu Dhabi are consistent with the very low probability: proximity talks are not the same as a three-way leaders meeting."
  - "Russia's public skepticism on security guarantees, as stated by Foreign Minister Sergey Lavrov, reinforces the market's dim view of a summit materializing."
  - "The Ukraine-Russia peace deal Polymarket contract sits at 10% before 2027, suggesting the market prices in some deal path but almost entirely without a direct leaders summit."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US is set to mediate Ukraine-Russia talks in Abu Dhabi next week, with de-escalation and security on the agenda."
    publisher: "Guardian staff"
    published_at: "2026-11-03T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/nov/03/ukraine-war-briefing-us-to-mediate-talks-with-kyiv-and-moscow-in-abu-dhabi-next-week-says-witkoff"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Guardian staff"
        source_url: "https://www.theguardian.com/world/2026/nov/03/ukraine-war-briefing-us-to-mediate-talks-with-kyiv-and-moscow-in-abu-dhabi-next-week-says-witkoff"
        retrieved_at: "2026-11-03T15:45:44+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; requires documented in-person appearance of all three leaders together."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Guardian staff: Ukraine war briefing: US to mediate talks with Kyiv and Moscow in Abu"
    url: "https://www.theguardian.com/world/2026/nov/03/ukraine-war-briefing-us-to-mediate-talks-with-kyiv-and-moscow-in-abu-dhabi-next-week-says-witkoff"
    published_at: "2026-11-03T00:00:00.000Z"
    retrieved_at: "2026-11-03T15:45:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
