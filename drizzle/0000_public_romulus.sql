CREATE TABLE `audit` (
	`id` text PRIMARY KEY NOT NULL,
	`actor_id` text NOT NULL,
	`action` text NOT NULL,
	`record_id` text NOT NULL,
	`created_at` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `client_events` (
	`id` text PRIMARY KEY NOT NULL,
	`owner_user_id` text NOT NULL,
	`title` text NOT NULL,
	`event_date` text DEFAULT '' NOT NULL,
	`venue` text DEFAULT '' NOT NULL,
	`design` text DEFAULT '' NOT NULL,
	`timeline` text DEFAULT '' NOT NULL,
	`proposal_url` text DEFAULT '' NOT NULL,
	`invoice_url` text DEFAULT '' NOT NULL,
	`approval` text DEFAULT 'Awaiting review' NOT NULL,
	`updated_at` text NOT NULL
);
--> statement-breakpoint
CREATE INDEX `idx_client_events_owner` ON `client_events` (`owner_user_id`);--> statement-breakpoint
CREATE TABLE `events` (
	`id` text PRIMARY KEY NOT NULL,
	`name` text NOT NULL,
	`path` text NOT NULL,
	`service` text DEFAULT '' NOT NULL,
	`created_at` text NOT NULL
);
--> statement-breakpoint
CREATE INDEX `idx_events_name_created` ON `events` (`name`,`created_at`);--> statement-breakpoint
CREATE TABLE `inquiries` (
	`id` text PRIMARY KEY NOT NULL,
	`request_id` text NOT NULL,
	`name` text NOT NULL,
	`email` text NOT NULL,
	`event_date` text NOT NULL,
	`venue` text NOT NULL,
	`service` text NOT NULL,
	`budget` text NOT NULL,
	`guests` integer,
	`vision` text DEFAULT '' NOT NULL,
	`source` text DEFAULT '' NOT NULL,
	`marketing` integer DEFAULT 0 NOT NULL,
	`status` text DEFAULT 'New inquiry' NOT NULL,
	`assigned_to` text DEFAULT 'Owner' NOT NULL,
	`next_action` text DEFAULT 'Review service fit and reply' NOT NULL,
	`next_date` text DEFAULT '' NOT NULL,
	`lost_reason` text DEFAULT '' NOT NULL,
	`admin_minutes` integer DEFAULT 0 NOT NULL,
	`first_response_at` text,
	`created_at` text NOT NULL,
	`updated_at` text NOT NULL,
	`mode` text DEFAULT 'review' NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `inquiries_request_id_unique` ON `inquiries` (`request_id`);--> statement-breakpoint
CREATE INDEX `idx_inquiries_status_created` ON `inquiries` (`status`,`created_at`);--> statement-breakpoint
CREATE TABLE `outbox` (
	`id` text PRIMARY KEY NOT NULL,
	`kind` text NOT NULL,
	`record_id` text NOT NULL,
	`payload` text NOT NULL,
	`status` text DEFAULT 'pending' NOT NULL,
	`attempts` integer DEFAULT 0 NOT NULL,
	`due_at` text NOT NULL,
	`last_error` text DEFAULT '' NOT NULL,
	`created_at` text NOT NULL
);
--> statement-breakpoint
CREATE INDEX `idx_outbox_status_due` ON `outbox` (`status`,`due_at`);--> statement-breakpoint
CREATE TABLE `subscriptions` (
	`id` text PRIMARY KEY NOT NULL,
	`email` text NOT NULL,
	`consented_at` text NOT NULL,
	`consent_version` text NOT NULL,
	`token_hash` text NOT NULL,
	`status` text DEFAULT 'pending' NOT NULL,
	`updated_at` text NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `subscriptions_email_unique` ON `subscriptions` (`email`);