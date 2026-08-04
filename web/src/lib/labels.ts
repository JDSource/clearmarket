// Jargon mapping layer — translate DB code constants into professional terminal terms.
// One source of truth so every component renders the same human label.

// ---------------------------------------------------------------------------
// source_status — THE stamped source judgment (source-layer refactor 2026-07-03)
// ---------------------------------------------------------------------------
// Stamped at enrichment as a pure function of the LLM commitment classification; every web
// surface reads it through this ONE helper (no component re-derives from raw field presence).
// The fallback covers pre-refactor bundles only and checks commitment BEFORE presence, so a
// hedge with a non-empty verbatim source field can never read platform_named.
// Keep in sync with api/src/index.ts marketOut().
export function sourceStatusOf(m: {
  source_status?: string | null;
  source_commitment?: string | null;
  resolution_source?: string | null;
} | null | undefined): 'platform_named' | 'no_committed_source' | 'no_source_stated' | 'unknown' {
  const stamped = (m as any)?.source_status;
  if (stamped) return stamped;
  const c = m?.source_commitment ?? null;
  if (c === 'uncommitted') return 'no_committed_source';
  if (c === 'none') return 'no_source_stated';
  if (c === 'named') return 'platform_named';
  const hasNamed = m?.resolution_source != null && String(m.resolution_source).trim() !== '';
  return hasNamed ? 'platform_named' : 'unknown';
}

export function arbiterLabel(v: string | null | undefined): string {
  switch (v) {
    case 'uma_oracle': return 'Optimistic Oracle (UMA)';
    case 'kalshi_staff': return 'Kalshi Staff';            // staff + CFTC backstop; NOT a "board"
    case 'polymarket_staff': return 'Polymarket Staff';
    case 'platform_auto': return 'Automated Settlement';
    case 'determinations_committee': return 'Determinations Committee';
    default: return v ?? '—';
  }
}

export function proposerLabel(v: string | null | undefined): string {
  switch (v) {
    case 'platform_staff': return 'Exchange Staff';
    case 'managed_whitelist': return 'Whitelisted Proposers';
    case 'permissionless': return 'Permissionless';
    case 'gov_agency': return 'Government Agency';
    default: return v ?? '—';
  }
}

export function sourceTypeLabel(v: string | null | undefined): string {
  switch (v) {
    case 'gov_stat_agency': return 'Govt Statistical Agency';
    case 'central_bank': return 'Central Bank';
    case 'regulated_data_vendor': return 'Regulated Data Vendor';
    case 'media_consensus': return 'Media Consensus';
    case 'court_filing': return 'Court Filing';
    case 'issuer_announcement': return 'Issuer Announcement';
    case 'scheduled_event': return 'Scheduled Event';
    case 'subjective': return 'Subjective';
    default: return v ?? '—';
  }
}

// Venue homepages are NOT real source citations — a market that "cites" kalshi.com or
// polymarket.com has not named where the outcome is read. Mirrors classify.py.
const PLACEHOLDER_HOSTS = ['kalshi.com', 'polymarket.com', 'kalshi.co'];
export function isPlaceholderCitation(url: string | null | undefined): boolean {
  if (!url) return true;
  const u = url.trim().replace(/\/+$/, '');
  const host = u.replace(/^https?:\/\/(www\.)?/, '').split('/')[0].toLowerCase();
  const path = u.slice(u.indexOf(host) + host.length);
  if (PLACEHOLDER_HOSTS.includes(host)) return true;
  return !path || path === '/';      // bare host, no real deep link
}
export function isPlaceholderSourceName(name: string | null | undefined): boolean {
  return !!name && name.trim().split(/\s+/).length <= 1;   // single token like "NYC"
}

// The source of record to DISPLAY: prefer a properly-named platform source; if that's a
// placeholder ("NYC"), fall back to the editorial underlying_reference (the real authority,
// e.g. "NYC Rent Guidelines Board"), flagged as editorial.
export function displaySource(
  name: string | null | undefined,
  url: string | null | undefined,
  underlyingRef: string | null | undefined,
): { text: string; editorial: boolean } {
  if (name && !isPlaceholderSourceName(name)) return { text: name, editorial: false };
  if (underlyingRef) return { text: underlyingRef, editorial: true };
  if (name) return { text: name, editorial: false };       // single-token, but it's all we have
  if (url && !isPlaceholderCitation(url)) return { text: url.replace(/^https?:\/\/(www\.)?/, '').split('/')[0], editorial: false };
  return { text: 'No named source', editorial: false };
}

// The HONEST platform source-of-record status, scaling across the universe.
// Distinguishes a real named source from a placeholder ("NYC") from a genuinely-absent
// source (subjective / consensus resolution). The editorial underlying_reference is NEVER
// returned here — that is "our read," shown separately and clearly subordinate, so we never
// present our own interpretation as the venue's named source.
//   named       → platform named a real authority in words (e.g. "U.S. Department of the Treasury")
//   cited       → no name in words, but a real deep-link citation (show the host, e.g. home.treasury.gov)
//   placeholder → platform gestured at a source but named only a placeholder token ("NYC")
//   subjective  → no source named at all; resolves by judgment / consensus
// Only 'named' is a clean source-of-record; for every other tone the caller should surface the
// "our read" editorial authority alongside.
export type PlatformSourceTone = 'named' | 'cited' | 'placeholder' | 'subjective';
export function platformSource(
  name: string | null | undefined,
  url: string | null | undefined,
): { text: string; tone: PlatformSourceTone; cited: string | null } {
  const realName = name && !isPlaceholderSourceName(name);
  const realUrl = url && !isPlaceholderCitation(url);
  if (realName) return { text: name as string, tone: 'named', cited: null };
  if (realUrl) return { text: (url as string).replace(/^https?:\/\/(www\.)?/, '').split('/')[0], tone: 'cited', cited: null };
  if (name) return { text: 'unnamed', tone: 'placeholder', cited: name as string };  // placeholder token, e.g. "NYC"
  return { text: 'subjective', tone: 'subjective', cited: null };
}

// host of a citation URL, or a clear "undefined" when there is genuinely no source
export function sourceLabel(name: string | null | undefined, url: string | null | undefined): string {
  if (name && !isPlaceholderSourceName(name)) return name;
  if (url && !isPlaceholderCitation(url)) return url.replace(/^https?:\/\/(www\.)?/, '').split('/')[0];
  if (name) return name;
  return 'No named source';
}

// RCG chip hover tooltips (institutional, plain English). Match the original event page.
export const RCG_TOOLTIP: Record<'A' | 'B' | 'C', string> = {
  A: 'Resolution Clarity Grade A — institutional-grade resolution. Committed source, mechanical settlement, no judgment. Click to see source.',
  B: 'Resolution Clarity Grade B — solid but not airtight: a hedged source, judgment step, or timing risk costs points. Click to see why.',
  C: 'Resolution Clarity Grade C — elevated resolution risk: uncommitted source, or contested / discretionary resolution. Click to see why.',
};

// Per-market resolution rationale — the grade + one neutral plain-English sentence on WHY.
// Shared by the single-venue verdict card and each row of the cross-venue compare table,
// so one market reads the same everywhere. States the fact; draws no conclusion for the reader.
export type Rationale = { grade: 'A' | 'B' | 'C'; word: string; flag: string | null; text: string };

export function rationaleFor(m: {
  resolution_clarity_grade?: string | null;
  rcg_caps?: string[] | null;
  arbitration_model?: string | null;
  resolution_source?: string | null;
  source_citation?: string | null;
}): Rationale {
  const grade = ((m.resolution_clarity_grade ?? 'C') as string).toUpperCase() as 'A' | 'B' | 'C';
  const caps = m.rcg_caps ?? [];
  const arbiter = m.arbitration_model ?? null;
  const name = m.resolution_source ?? null;
  const url = m.source_citation ?? null;
  const src = name ?? (url ? url.replace(/^https?:\/\/(www\.)?/, '').split('/')[0] : null);

  if (grade === 'A') {
    return {
      grade, word: 'Clean settlement', flag: null,
      text: src ? `Resolves against a named source (${src}) with mechanical settlement.` : `Resolves on a mechanical rule.`,
    };
  }
  if (grade === 'B') {
    // name the BINDING cause when a cap fired — never blame the arbiter for a source cap
    if (caps.includes('commitment_uncommitted_illustrative')) {
      return { grade, word: 'Hedged source', flag: 'source not committed',
        text: `Source only gestured at ("for example …") — a candidate, not a commitment.` };
    }
    return {
      grade, word: 'Some judgment', flag: 'judgment in settlement',
      text: src ? `Named source (${src}), but settlement involves some judgment.` : `Resolution involves some judgment.`,
    };
  }
  // C — surface the single BINDING fact, neutrally. Commitment caps first: they are the
  // most common binding constraint, and naming a different factor here was the wrong-cause
  // tooltip bug (cl-hit oil, 2026-06-28).
  if (caps.includes('commitment_none')) {
    return { grade, word: 'Elevated risk', flag: 'no source stated',
      text: `The venue names no resolution source at all.` };
  }
  // secondhand BEFORE the generic commitment branch: its copy must not claim "committed to
  // no controlling source" — the venue DID commit; the defect is authority quality (ruled 2026-07-04)
  if (caps.includes('commitment_committed_secondhand')) {
    return { grade, word: 'Elevated risk', flag: 'secondhand source',
      text: src
        ? `Settles per ${src} — a secondhand data source, not the underlying authority; no rule for when they disagree.`
        : `Settles per a secondhand data source, not the underlying authority; no rule for when they disagree.` };
  }
  if (caps.some((c) => c.startsWith('commitment_'))) {
    return { grade, word: 'Elevated risk', flag: 'no committed source',
      text: `The venue committed to no controlling source — placeholder or menu language decides at resolution.` };
  }
  // exchange-notice conflict BEFORE the generic branches: the venue DID commit a source —
  // the defect is two venue documents disagreeing (v3.7; same wrong-cause class as cl-hit oil)
  if (caps.includes('exchange_notice_source_conflict')) {
    return { grade, word: 'Elevated risk', flag: 'venue notice conflict',
      text: src
        ? `The venue committed to ${src}, but its own page notice names a different settlement source.`
        : `The venue's own page notice names a settlement source different from its committed source.` };
  }
  if (caps.includes('adversarial_ground_truth')) {
    return { grade, word: 'Elevated risk', flag: 'contested outcome',
      text: `The outcome depends on a fact an interested party controls or can dispute.` };
  }
  if (caps.includes('multi_source_no_conflict_rule')) {
    return { grade, word: 'Elevated risk', flag: 'no tie-breaker rule',
      text: `Names more than one source with no tie-breaker rule; if they disagree, settlement is ambiguous.` };
  }
  if (arbiter === 'uma_oracle') {
    return { grade, word: 'Elevated risk', flag: 'oracle-settled',
      text: `No named source; settled by a token-holder vote rather than an automatic data feed.` };
  }
  return { grade, word: 'Elevated risk', flag: 'unclear resolution',
    text: `No clearly named source, or resolution relies on judgment.` };
}

// ---------------------------------------------------------------------------
// Event title display — strike placeholder substitution
// ---------------------------------------------------------------------------
// ~32 grouped events carry a Polymarket template title with the strike blanked
// to "___" (e.g. "Will gold (GC) be above ___ by the end of June?"). The member
// markets DO carry the real strikes in question_raw ("settle over $8,000"…), so
// we derive the strike RANGE and substitute it in. Used by the events index,
// the event detail H1/<title>/JSON-LD, and the search index so "___" never ships.
const STRIKE_RE =
  /(?:above|over|exceeds?|reach(?:es)?|hits?|of at least|at least|score of|of)\s+(\$)?\s?([\d][\d,]*(?:\.\d+)?)\s?(?:(trillion|billion|million|tn|bn|[kmbt])(?![a-z])|(%))?/i;

const STRIKE_MULT: Record<string, number> = {
  k: 1e3, m: 1e6, million: 1e6, b: 1e9, bn: 1e9, billion: 1e9, t: 1e12, tn: 1e12, trillion: 1e12,
};

function strikeOf(q: string | null | undefined): { val: number; dollar: boolean; pct: boolean } | null {
  if (!q) return null;
  const m = q.match(STRIKE_RE);
  if (!m) return null;
  const raw = parseFloat(m[2].replace(/,/g, ''));
  if (isNaN(raw)) return null;
  const unit = (m[3] || '').toLowerCase();
  return { val: raw * (STRIKE_MULT[unit] ?? 1), dollar: !!m[1], pct: !!m[4] };
}

function trimNum(n: number): string {
  return Number(n.toFixed(2)).toString();
}

function fmtStrike(s: { val: number; dollar: boolean; pct: boolean }): string {
  const { val, dollar, pct } = s;
  if (pct) return `${trimNum(val)}%`;
  const d = dollar ? '$' : '';
  if (val >= 1e12) return `${d}${trimNum(val / 1e12)}T`;
  if (val >= 1e9) return `${d}${trimNum(val / 1e9)}B`;
  if (val >= 1e6) return `${d}${trimNum(val / 1e6)}M`;
  if (val >= 1000) return `${d}${val.toLocaleString('en-US')}`;
  return `${d}${trimNum(val)}`;
}

export function eventDisplayQuestion(
  question: string | null | undefined,
  markets: { question_raw?: string | null }[],
): string {
  const q = question ?? '';
  if (!q.includes('___')) return q;
  const strikes = markets
    .map((m) => strikeOf(m.question_raw))
    .filter((s): s is { val: number; dollar: boolean; pct: boolean } => s !== null);
  if (!strikes.length) return q.replace('___', 'a set threshold');
  const lo = strikes.reduce((a, b) => (b.val < a.val ? b : a));
  const hi = strikes.reduce((a, b) => (b.val > a.val ? b : a));
  const range = lo.val === hi.val ? fmtStrike(lo) : `${fmtStrike(lo)}–${fmtStrike(hi)}`;
  return q.replace('___', range);
}
