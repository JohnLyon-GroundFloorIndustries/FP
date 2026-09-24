ALTER TABLE `inquiries` ADD `details` text DEFAULT '{}' NOT NULL;--> statement-breakpoint
ALTER TABLE `inquiries` ADD `consent_version` text DEFAULT 'legacy' NOT NULL;--> statement-breakpoint
ALTER TABLE `inquiries` ADD `consented_at` text;