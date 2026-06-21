---
signal_id: "CMSIG2026062103"
signal_slug: "us-iran-nuclear-deal-before-2027-polymarket-71-2026-06-21"
headline: "US-Iran nuclear deal before 2027: Polymarket 71%"
semantic_title: "Pre-2027 US-Iran deal consensus anchors above 70 percent"
telemetry: "Polymarket 71%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-21T05:18:43.000Z"
event_id: "CM-EVT-VP51KKLQH2"
event_slug: "us-iran-nuclear-deal-before-2027"
event_question: "Will the US and Iran reach a nuclear deal before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x182390641d3b1b47cc64274b9da290efd04221c586651ba190880713da6347d9"
  question_raw: "US-Iran nuclear deal before 2027?"
  current_price: 0.71
  volume_24h_usd: 73413.15463799999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices a 71% probability that the US and Iran reach a nuclear deal before 2027, resolving via UMA oracle."
  - "The launch of formal VP-level talks in Switzerland is consistent with above-even pricing, though the market assigns meaningful doubt to any completed deal."
  - "The June 30 short-dated contract at 51% versus 71% by end-2026 captures the market's view that timeline, not deal viability, is the primary uncertainty."
  - "A 19% Polymarket contract on the US invading Iran before 2027 sits alongside the deal contract, framing the outcome distribution as deal-or-escalation, not a stable status quo."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Vance and senior Iranian officials arrived in Switzerland to formally launch negotiations over Tehran's nuclear program and extend a fragile interim ceasefire."
    publisher: "AAMER MADHANI, SEUNG MIN KIM and JAMEY KEATEN Associated Press"
    published_at: "2026-06-21T05:18:43.000Z"
    source_url: "https://www.witn.com/2026/06/21/us-vice-president-jd-vance-arrives-switzerland-launch-talks-with-iran-its-nuclear-program/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AAMER MADHANI, SEUNG MIN KIM and JAMEY KEATEN Associated Press"
        source_url: "https://www.witn.com/2026/06/21/us-vice-president-jd-vance-arrives-switzerland-launch-talks-with-iran-its-nuclear-program/"
        retrieved_at: "2026-06-21T11:13:58+00:00"
  - type: "pm_response"
    notes: "Polymarket's 71% on a pre-2027 deal is the market's base case as talks formally open; the 20-point gap to the June 30 contract reflects deadline uncertainty, not deal skepticism."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AAMER MADHANI, SEUNG MIN KIM and JAMEY KEATEN Associated Press: Vance and Iranian officials arrive in Switzerland to launch talks on T"
    url: "https://www.witn.com/2026/06/21/us-vice-president-jd-vance-arrives-switzerland-launch-talks-with-iran-its-nuclear-program/"
    published_at: "2026-06-21T05:18:43.000Z"
    retrieved_at: "2026-06-21T11:13:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
