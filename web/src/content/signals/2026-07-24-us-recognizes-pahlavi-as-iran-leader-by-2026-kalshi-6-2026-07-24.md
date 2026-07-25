---
signal_id: "CMSIG2026072405"
signal_slug: "us-recognizes-pahlavi-as-iran-leader-by-2026-kalshi-6-2026-07-24"
headline: "US recognizes Pahlavi as Iran leader by 2026: Kalshi 6%"
semantic_title: "US recognizing Reza Pahlavi as Iran leader stays a long shot"
telemetry: "Kalshi 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-24T00:00:00.000Z"
event_id: "CM-EVT-SY50TZ6672"
event_slug: "kxrecogpersoniran-26"
event_question: "Will the United States recognize Reza Pahlavi as the leader of Iran by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRECOGPERSONIRAN-26"
  question_raw: "Will the United States recognize Reza Pahlavi as the leader of Iran in 2026?"
  current_price: 0.065
  volume_24h_usd: 249.64
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 6% on the U.S. recognizing Reza Pahlavi as Iran's leader by end of 2026."
  - "Despite escalating U.S. strikes and Trump threatening a massive attack, markets see regime-change recognition as a remote outcome this year."
  - "A companion Polymarket contract puts the Iranian regime's fall before 2027 at 9%, and Kalshi prices a U.S. embassy reopening in Iran at just 7%, consistent with a low-probability regime-change scenario."
  - "Resolution adjudicated by ABC News reporting on an official U.S. government recognition act."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The U.S. launched new strikes on Iran and President Donald Trump threatened a massive attack as the conflict widened, raising questions about U.S. end-state goals."
    publisher: "nbcnews.com"
    published_at: "2026-07-24T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/world/iran/us-iran-strikes-trump-massive-attack-war-hormuz-red-sea-oil-rcna589016"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nbcnews.com"
        source_url: "https://www.nbcnews.com/world/iran/us-iran-strikes-trump-massive-attack-war-hormuz-red-sea-oil-rcna589016"
        retrieved_at: "2026-07-25T09:42:27+00:00"
  - type: "pm_response"
    notes: "Kalshi at 6% treats U.S. recognition of a replacement Iranian government as a deep long shot even as military strikes escalate."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nbcnews.com: U.S. launches new Iran strikes, Trump threatens ‘massive attack’ as wa"
    url: "https://www.nbcnews.com/world/iran/us-iran-strikes-trump-massive-attack-war-hormuz-red-sea-oil-rcna589016"
    published_at: "2026-07-24T00:00:00.000Z"
    retrieved_at: "2026-07-25T09:42:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
