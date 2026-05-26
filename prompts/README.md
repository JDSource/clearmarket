# ClearMarket Signal — LLM judge prompt templates

Versioned text files holding the exact prompt content fed to the LLM judge for each
wire-type detection path. Every wire item published by CM Signal carries a
`prompt_template` field (e.g., `cross_venue_v1`) that resolves to one of the files
in this directory.

## Why these are public

The `cm:tier: editorial` provenance label on values produced by the LLM judge is
only meaningful if downstream consumers can audit what the judge was asked to
decide. Publishing the prompts here makes the editorial layer reproducible:

- Institutional data buyers (Datalinx, Bloomberg-shape distributors) can audit
  exactly what reasoning rubric the judge applied
- AI agents grounding answers from CM Signal can verify the editorial method
  matches their trust threshold
- External researchers can re-run a wire item through a different model with the
  same prompt and compare outputs

## Versioning

Prompts are immutable once published under a version. Material changes ship a new
version (`cross_venue_v2`), never modify `cross_venue_v1`. The `prompt_template`
field on a wire item is a stable reference; old wires keep pointing at the
version that produced them.

## Files

| File | Wire type | Status |
|---|---|---|
| `cross_venue_v1.txt` | `cross_venue_divergence` detection | stub (real prompt populated when LLM generator ships, build item #12 in `now.md`) |
| `benchmark_drift_v1.txt` | `benchmark_drift` detection | stub |
| `news_cycle_v1.txt` | `news_cycle` detection | stub |
| `volume_spike_v1.txt` | `volume_spike` detection | stub |

## Raw access

GitHub raw URLs follow the pattern:

```
https://raw.githubusercontent.com/JDSource/clearmarket/main/prompts/<name>.txt
```

Wire items link the `prompt_template` field to the corresponding raw URL so any
consumer can fetch the prompt programmatically.

## License

Same CC-BY-4.0 as the rest of ClearMarket data products.
