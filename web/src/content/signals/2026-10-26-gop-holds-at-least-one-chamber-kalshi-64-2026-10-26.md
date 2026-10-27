---
signal_id: "CMSIG2026102604"
signal_slug: "gop-holds-at-least-one-chamber-kalshi-64-2026-10-26"
headline: "GOP holds at least one chamber: Kalshi 64%"
semantic_title: "Republican control of at least one chamber stays near 50-50 on Kalshi"
telemetry: "Kalshi 64%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-26T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.64
  volume_24h_usd: 96528.52
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices Republicans retaining at least one chamber of Congress at 64%, reflecting meaningful but not dominant GOP chances."
  - "With the House Democrat contract at 90% on Kalshi, the 64% Republican retention figure implies the Senate is the most plausible path for GOP to hold one chamber."
  - "The Polymarket Senate control contract (CM-EVT-M9WJY06T90) at 66% for Democrats is directionally consistent: Democrats favored in both chambers, but Senate is closer."
  - "Resolves via Bureau of Labor Statistics per the listed source, though congressional seat certification is the functional resolution mechanic."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Midterm previews indicate Democrats could flip both the House and Senate, but Republican retention of at least one chamber remains a live scenario."
    publisher: "Amber Phillips"
    published_at: "2026-10-26T00:00:00.000Z"
    source_url: "https://www.washingtonpost.com/politics/2026/10/26/what-expect-next-weeks-midterm-elections/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Amber Phillips"
        source_url: "https://www.washingtonpost.com/politics/2026/10/26/what-expect-next-weeks-midterm-elections/"
        retrieved_at: "2026-10-27T07:48:12+00:00"
  - type: "pm_response"
    notes: "Kalshi's 64% on GOP holding at least one chamber sits in tension with the 90% Democrat House contract, pointing to the Senate as the key battleground in market pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Amber Phillips: What to expect in next week’s midterm elections - The Washington Post"
    url: "https://www.washingtonpost.com/politics/2026/10/26/what-expect-next-weeks-midterm-elections/"
    published_at: "2026-10-26T00:00:00.000Z"
    retrieved_at: "2026-10-27T07:48:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
