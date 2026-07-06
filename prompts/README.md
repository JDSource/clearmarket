# ClearMarket Signal — editorial methodology

CM Signal wire items carry values produced by an LLM judge, labelled with the
`cm:tier: editorial` provenance tier. This directory documents the **methodology**
behind that editorial layer: what each wire-type detection path evaluates, the
inputs it considers, and the decision rubric it applies.

The exact prompt text and the model configuration behind the judge are
**proprietary** and are not published. What we publish is the reasoning method —
enough for a consumer to understand and trust what the `editorial` tier means,
without exposing the implementation that produces it.

## What the editorial tier means

The `cm:tier: editorial` label marks a value as the output of CM's judge rather
than a direct venue field (`cm:tier: direct`) or an arithmetic derivation
(`cm:tier: derived`). Editorial values are governed by a documented rubric and are
versioned: a material change to a detection method ships as a new version, and a
wire item's provenance records the methodology version that produced it.

## Detection paths

| Wire type | What the judge evaluates |
|---|---|
| `cross_venue_divergence` | Whether a price gap between venues on the same linked question reflects a real divergence vs. a stale or thin quote |
| `benchmark_drift` | Whether a market's implied path has drifted from an external benchmark of record |
| `news_cycle` | Whether fresh market movement is attributable to an identifiable news catalyst |
| `volume_spike` | Whether a surge of trading volume reflects genuine fresh attention vs. structural churn |

Per-wire methodology detail and the field-level provenance model live in the
published methodology reference at `/methodology`.

## License

Same CC-BY-4.0 as the rest of ClearMarket data products.
