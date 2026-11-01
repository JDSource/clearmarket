---
signal_id: "CMSIG2026110103"
signal_slug: "gop-holds-one-chamber-of-congress-kalshi-70-2026-11-01"
headline: "GOP holds one chamber of Congress: Kalshi 70%"
semantic_title: "Republicans holding at least one chamber stays favored"
telemetry: "Kalshi 70%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-01T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.7
  volume_24h_usd: 219604.72
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market puts 70% odds on Republicans controlling at least one chamber of Congress after the 2026 midterms."
  - "The NBC poll showing a 7-point Democratic lead in the generic ballot is a bearish signal for Republicans, yet Kalshi's 70% reflects a market that is not fully accepting the poll's implied Democratic sweep."
  - "Winning at least one chamber is a lower bar than winning both; the 70% likely reflects Senate map advantages for Republicans even as the House leans Democratic."
  - "The Polymarket Senate contract (CM-EVT-M9WJY06T90) prices at 73% for a Republican Senate win, consistent with the Kalshi reading and suggesting the Senate is carrying most of the GOP's one-chamber probability."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "An NBC News poll shows Democrats with a 7-point lead in the battle for Congress and Trump's disapproval at a record 60%, two days before the midterm elections."
    publisher: "Ben Kamisar, Bridget Bowman"
    published_at: "2026-11-01T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/politics/2026-election/poll-voters-demand-change-check-trump-fueling-steep-democratic-midterm-rcna606183"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ben Kamisar, Bridget Bowman"
        source_url: "https://www.nbcnews.com/politics/2026-election/poll-voters-demand-change-check-trump-fueling-steep-democratic-midterm-rcna606183"
        retrieved_at: "2026-11-01T14:42:33+00:00"
  - type: "pm_response"
    notes: "The Kalshi contract resolves via Bureau of Labor Statistics, likely a metadata error; resolution in practice will track official congressional certification."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ben Kamisar, Bridget Bowman: Poll: Voters demand change and a check on Trump, fueling a steep Democ"
    url: "https://www.nbcnews.com/politics/2026-election/poll-voters-demand-change-check-trump-fueling-steep-democratic-midterm-rcna606183"
    published_at: "2026-11-01T00:00:00.000Z"
    retrieved_at: "2026-11-01T14:42:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
