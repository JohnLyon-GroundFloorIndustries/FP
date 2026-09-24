# Launch acceptance and rollback

## Current delivery boundary
Private review application with real test storage; no change to florapacifica.co DNS or Showit. Higher-value full-service repositioning approved in conversation; exact new minimum not provided. Client portal deferred by the owner. Do not infer a $50,000 minimum or an annual capacity claim from the brief.

## Owner decisions
- Approve exact minimum and whether to display it. Proposed after confirmation: “Full-service wedding commissions typically begin at $50,000.” Until then, individually scoped copy and a free-text investment field avoid invented thresholds.
- Approve case-study captions, image reuse and credits. Confirm Rock Creek season/planner, case-study installation challenges, production details and outcomes. These were not invented.
- Confirm annual capacity before adding “a considered number of commissions each season.” Current site does not publish an unsupported scarcity claim.
- Confirm business email, business identity/location, privacy contact, approved response practice and travel boundaries. No public street address is invented.
- Approve any retirement or referral path for the existing small-event services. New positioning omits the old low-price offers as directed.

## Production configuration
1. Owner and counsel approve copy, image rights, privacy notice, retention, processor disclosures and consent wording.
2. Verify staff identity and allowlist in actual production. Test allowed staff, signed-in nonstaff, anonymous requests, logout and identity recovery. The source must run behind the Sites identity dispatcher.
3. Configure BUSINESS_EMAIL, EMAIL_FROM, RESEND_API_KEY and PUBLIC_SITE_ORIGIN in hosting secrets/settings. Verify sending domain SPF/DKIM and appropriate DMARC with the provider. Send only authorized test messages to controlled recipients; check delivered, bounced, retry, duplicate and failure paths.
4. If CRM is later selected, approve data mapping, configure webhook credentials and verify receipt/retry/idempotency before enabling. Built-in lead queue works independently.
5. Test live inquiry with explicit authorized test data: database receipt, staff visibility, notification, acknowledgement, no analytics PII. Confirm queue is monitored and backup restore has been tested.
6. Update `app/content.ts` origin and layout metadata base/Organization URL to the confirmed final domain. Configure canonical domain and HTTPS at host. Confirm caching/compression/security headers on the actual deployment.
7. Preserve old host export and DNS records. Implement middleware redirect map plus any URLs discovered in complete Showit/WordPress export. Current sitemap children returned 403, so full hidden/legacy URL coverage is unresolved.
8. Run a production crawl, keyboard and screen-reader audit, 200% zoom, real phone testing, and PageSpeed/CWV checks. Validate XML sitemap, canonicals, schema and social cards. Baseline Search Console data before changes; no traffic uplift is forecast.
9. Only after approval, set INQUIRY_MODE=live and INDEXING_ENABLED=true, redeploy, then explicitly authorize public access/domain cutover. Private review indexing stays off.
10. Verify domain in Google Search Console via DNS, submit sitemap, inspect root/work/commissions/inquiry URLs. Verify Bing Webmaster Tools (DNS or approved import), submit sitemap and check crawl reports. Review 404s and redirect loops after launch and again after one week.

## Deployment package
Sites package contains built Cloudflare Worker, client assets, hosting metadata and migrations. Source ZIP is for developers. Preserve project_id appgprj_6aa75107ad148191848b5b62eb29b698. Push exact source before saving its version and deploy only that saved version. Existing migrations are immutable; 0002 adds inquiry details/consent columns without deleting old data.

## Rollback
For application regression redeploy the previous saved Sites version. Keep additive database columns; do not reverse migrations or delete stored inquiries. If a migration fails, inspect which files applied before doing anything further. Turn intake to review if delivery is misconfigured and reconcile every queued message. For public domain rollback restore recorded DNS/host settings and the prior Showit export, keeping a protected copy of new inquiries and documented follow-up responsibility. Database recovery uses a verified provider restore/export; application rollback is not data rollback.

## Performance acceptance
Use responsive WebP (640/1440), explicit image geometry, lazy loading and prioritized hero. System serif/sans fonts avoid font requests and layout shifts. Target mobile LCP ≤2.5s, INP ≤200ms and CLS ≤0.1 at the 75th percentile after sufficient real traffic; these are goals, not measured production results. Initial compressed JS budget 200KB, first viewport image budget 500KB, no third-party scripts. Review actual built transfer and field data before launch.

Archive preservation: four additional venue/photographer credits are retained on /work with a link to the existing portfolio. Before replacing the old domain, import licensed full image sets and remove/replace that external archive link, which otherwise would loop through the /portfolio redirect.
