# Flora Pacifica — Atelier redesign

An editorial, responsive wedding-floral website with a real D1 inquiry backend and protected staff lead queue. Client portal deferred by owner instruction. Existing Sites project retained; public florapacifica.co has not been replaced.

Start with docs/HANDOFF.html. Source is in app/, assets in public/images/, schema in db/, immutable migrations in drizzle/.

## Setup
Use Node 22.13+ and npm. Run `npm ci`, copy `.env.example` to `.env`, then `npm run build`. Apply each migration once, in filename order:
`node --import ./scripts/sites-env.mjs ./node_modules/wrangler/bin/wrangler.js d1 execute DB --local --config dist/server/wrangler.json --persist-to .wrangler/state --file drizzle/FILE.sql`
Run `npm run dev` and open the URL printed by the server. The local preview simulates staff sign-in; this is not a production identity test. `npm start` serves the built Worker locally.

Run `node node_modules/typescript/bin/tsc --noEmit` and `python tests/verify_local.py` while dev is running. Python test uses the standard library. Preview screenshots and browser/a11y results are included separately. Browser tests use Playwright and axe-core; consult test evidence for scope.

## Hosting
Cloudflare Worker-compatible Sites runtime plus D1 are required. GitHub Pages and static-only hosts cannot run inquiry persistence, staff authorization, outbox, or analytics. Do not deploy the static assets alone as the full website. A different server host requires porting the D1 and trusted identity integration.

## Review defaults
INQUIRY_MODE=review; INDEXING_ENABLED=false. Test details only. No live notifications, CRM delivery, or marketing. Do not enable indexing or live mode until the launch checklist is signed off. No client login is offered.
