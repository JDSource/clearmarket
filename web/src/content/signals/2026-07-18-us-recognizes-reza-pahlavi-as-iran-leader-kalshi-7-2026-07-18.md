---
signal_id: "CMSIG2026071806"
signal_slug: "us-recognizes-reza-pahlavi-as-iran-leader-kalshi-7-2026-07-18"
headline: "US recognizes Reza Pahlavi as Iran leader: Kalshi 7%"
semantic_title: "Reza Pahlavi recognition pricing holds deep discount amid strikes"
telemetry: "Kalshi 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-18T00:00:00.000Z"
event_id: "CM-EVT-SY50TZ6672"
event_slug: "kxrecogpersoniran-26"
event_question: "Will the United States recognize Reza Pahlavi as the leader of Iran by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRECOGPERSONIRAN-26"
  question_raw: "Will the United States recognize Reza Pahlavi as the leader of Iran in 2026?"
  current_price: 0.067
  volume_24h_usd: 14.44
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 7% on the US formally recognizing Reza Pahlavi as Iran's leader in 2026, despite active US military engagement with Iranian forces."
  - "Escalating airstrikes and troop deaths have not moved market pricing toward regime-change scenarios; the market treats recognition as a low-probability political step."
  - "A companion Kalshi contract (CM-EVT-34SYT4T2T1) prices just 7% on the US reopening its embassy in Iran, confirming markets see normalization as equally remote."
  - "Resolution is via ABC News reporting on formal US government recognition; military strikes alone would not trigger resolution without a diplomatic declaration."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US forces launched new airstrikes on Iran to punish IRGC units after two US troops were killed in a Jordan base attack, with the conflict now described as lurching toward all-out war."
    publisher: "abc.net.au"
    published_at: "2026-07-18T00:00:00.000Z"
    source_url: "https://www.abc.net.au/news/2026-07-19/us-says-two-military-personnel-killed-in-jordan/106932528"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "abc.net.au"
        source_url: "https://www.abc.net.au/news/2026-07-19/us-says-two-military-personnel-killed-in-jordan/106932528"
        retrieved_at: "2026-07-19T09:48:56+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolved via ABC; at 7%, pricing is consistent with deep skepticism about regime-change political outcomes despite military escalation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "abc.net.au: US military launches new air strikes to 'swiftly punish' Iran for deat"
    url: "https://www.abc.net.au/news/2026-07-19/us-says-two-military-personnel-killed-in-jordan/106932528"
    published_at: "2026-07-18T00:00:00.000Z"
    retrieved_at: "2026-07-19T09:48:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
