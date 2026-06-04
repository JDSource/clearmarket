-- Per-call audit log for the REST API + MCP. Non-destructive; safe to run on the live DB.
-- Mirrors the call_log block in scripts/export-d1.mjs so reseeds keep it (IF NOT EXISTS = persists).
CREATE TABLE IF NOT EXISTS call_log (
  ts TEXT NOT NULL,           -- ISO timestamp of the call
  surface TEXT NOT NULL,      -- 'rest' | 'mcp'
  action TEXT NOT NULL,       -- endpoint or MCP tool name
  target TEXT,                -- the key argument: slug / market_id / JSON of filters
  requester TEXT,             -- 'key:<key>' if authenticated, else 'ip:<addr>'
  country TEXT                -- Cloudflare-resolved country of the caller
);
CREATE INDEX IF NOT EXISTS idx_call_log_ts ON call_log(ts);
