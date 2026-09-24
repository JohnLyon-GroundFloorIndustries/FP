declare namespace Cloudflare {
  interface Env {
    DB?: D1Database;
    INDEXING_ENABLED?: string;
    BUCKET?: R2Bucket;
    SITE_ADMIN_EMAILS?: string;
    INQUIRY_MODE?: string;
    BUSINESS_EMAIL?: string;
    EMAIL_FROM?: string;
    RESEND_API_KEY?: string;
    CRM_WEBHOOK_URL?: string;
    CRM_WEBHOOK_SECRET?: string;
    PUBLIC_SITE_ORIGIN?: string;
    CLIENT_PORTAL_URL?: string;
  }
}
