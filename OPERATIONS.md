# Operating the studio workflow

| Stage | System and responsible person | Required action / evidence |
|---|---|---|
| Inquiry receipt | Website / staff owner | D1 stores details, consent version and time, request ID before receipt. Check queue each working day. |
| Qualification | Staff queue / owner | Review date, setting, scope, investment and creative fit. No automated rejection. |
| Assignment | Staff queue / owner | Set responsible person, next action and due date. |
| Human response | Approved email / assigned person | Send considered response; then mark human reply to measure elapsed time. No response SLA published. |
| Consultation | Team calendar / assigned person | Agree agenda, attendees and creative priorities; mark stage. |
| Proposal | Approved proposal tool / owner | Define inclusions, exclusions, taxes, travel, labor, installation, strike, rentals and substitution process. |
| Booking | Contract and payment provider / owner | Verify signed agreement and required payment before setting Booked. Checkbox gate is an attestation, not payment verification. |
| Design development | Team / lead designer | Maintain versioned design notes; client portal deferred. |
| Final details | Planner and designer | Confirm access, permits, load-in, weather plan, responsibilities and strike. |
| Completion | Team / owner | Close production tasks, reconcile rentals and mark Completed. |
| Photography permission | Team / owner | Obtain event, couple, photographer, planner and venue publishing permissions as applicable. Record permitted channels and credits. |
| Honest review | Team / owner | Request a candid review only with approved outreach; never filter by expected rating or offer incentives. |
| Referral | Team / owner | Thank referring partners personally with approved language; record source. |
| Retention/deletion | Owner / privacy reviewer | Apply approved schedule; record deletion action and backup aging. |

## Staff access and security
Production authentication is managed by Sites dispatch. SITE_ADMIN_EMAILS is a server-side staff allowlist; authentication alone grants no lead access. Require MFA on staff identity accounts where available. Recovery occurs through the identity provider. On offboarding remove the person from allowlist and Site sharing, redeploy, revoke sessions as supported and confirm API denial. Never expose this Worker directly on a host that lets visitors forge the trusted identity headers. A host migration needs a verified replacement identity boundary.

Exports are restricted to staff, no-store, audited and protected against spreadsheet formula injection. Export includes at most 2,000 latest records; queue displays at most 200. Review those limits before scale-up. Store exports in an approved restricted folder; delete promptly. No production record browser deletion is implemented: approved live deletion requires an administrator runbook and audit record. Test records can be deleted in the queue.

## Delivery and retry
The transactionally stored outbox supports staff-triggered processing, five attempts, exponential delay, a processing lease and provider idempotency keys. Email requires RESEND_API_KEY, EMAIL_FROM and BUSINESS_EMAIL. CRM is optional and not needed for the built-in lead queue. No unattended delivery worker is scheduled. Until scheduling is explicitly approved and tested, staff must process and inspect the queue. Provider idempotency has a finite window: reconcile uncertain deliveries before any manual retry after 24 hours. Approve notification and acknowledgement wording before live mode. Do not process live messages merely to test the review site.

## Retention recommendation — requires approval
Delete review/test inquiries after acceptance. Consider 12 months for unbooked inquiries, 13 months for anonymous event counts, and a counsel-approved contractual/tax schedule for booked events. Keep only necessary records. Consent is versioned with inquiry time. Do not apply recommendations to production data until approved. Backups may retain deleted data until their own expiry; document this in the final privacy notice.

## Backup / recovery
Before launch and material migrations, obtain a protected database export or provider restore bookmark. Confirm Sites support/access for D1 restore rather than assuming account access to Cloudflare. Test restore into an isolated database and compare record counts, consent records and outbox statuses. Never replay a restored outbox until reconciling messages already sent. Record recovery owner, last backup, achieved restore time and losses. No recovery-time promise is made by this package.

## Vendor inventory
Sites/OpenAI: private hosting access and managed identity. Cloudflare: Worker and D1 persistence through Sites. Resend: optional, unconfigured transactional processor. CRM: none selected; optional disabled webhook. Social platforms: external links only. No external web fonts, embedded social trackers, payment collection or client portal. Verify hosting logs and subprocessors with vendors before approving the public privacy notice.
