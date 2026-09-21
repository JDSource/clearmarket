---
signal_id: "CMSIG2026092106"
signal_slug: "xi-visits-us-before-2027-polymarket-100-2026-09-21"
headline: "Xi visits US before 2027: Polymarket 100%"
semantic_title: "Xi Jinping US visit before 2027 fully priced in at 100 percent"
telemetry: "Polymarket 100%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-09-21T00:00:00.000Z"
event_id: "CM-EVT-LKD4XHGN64"
event_slug: "will-xi-jinping-visit-us-before-2027"
event_question: "Will Xi Jinping visit the US before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd7e906eaec2c7f66697447785aa1d4fdaa82f536ca533a2bc0d3535b04e832ec"
  question_raw: "Will Xi Jinping visit US before 2027?"
  current_price: 0.998
  volume_24h_usd: 22250.569647000004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices the Xi Jinping US visit before 2027 at 100%, reflecting that the visit has already occurred or is already confirmed beyond dispute."
  - "Multiple news outlets confirm Xi rolled into the Trump summit on September 21, making this contract effectively resolved in fact even if not yet formally settled."
  - "The companion Kalshi contract on Republicans holding more governorships sits at 64%, unrelated but worth noting that the diplomatic summit has not visibly shifted domestic political pricing."
  - "Resolution via UMA oracle will confirm the visit against public record; at 100%, no residual uncertainty remains in the market."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Xi Jinping arrived for a Trump summit as China's trade engine showed strong momentum, with both leaders seeking a tariff framework ahead of year-end."
    publisher: "The Associated Press"
    published_at: "2026-09-21T00:00:00.000Z"
    source_url: "https://wtop.com/national/2026/09/trump-decries-democrats-as-communists-even-as-he-looks-to-impress-chinas-communist-leader/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Associated Press"
        source_url: "https://wtop.com/national/2026/09/trump-decries-democrats-as-communists-even-as-he-looks-to-impress-chinas-communist-leader/"
        retrieved_at: "2026-09-21T07:47:18+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 100% is a lagging confirmation of the confirmed Xi-Trump summit; the market fully priced the visit before or concurrent with the news breaking."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Associated Press: Trump decries Democrats as ‘communists,’ even as he looks to impress C"
    url: "https://wtop.com/national/2026/09/trump-decries-democrats-as-communists-even-as-he-looks-to-impress-chinas-communist-leader/"
    published_at: "2026-09-21T00:00:00.000Z"
    retrieved_at: "2026-09-21T07:47:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
