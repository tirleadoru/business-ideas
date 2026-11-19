# Letterlyn server setup (AWS Lightsail), for Remus

Letterlyn's own server. It's separate from every other business.
The API code, its deploy script and service files arrive with milestone M2. This is the base setup.

## 1. Instance
- **OS:** Ubuntu 24.04 LTS.
- **Region:** Frankfurt (eu-central-1).
- **Plan:** 2 GB RAM (about $12/month). Resize later if needed.
- **Static IP:** attach one.
- **Automatic daily snapshots:** on, keep 7.

## 2. Firewall (Lightsail networking)
- Ports **80 and 443** open to everyone.
- **SSH (22):** only from Remus's and Doru's IPs, key login only, no passwords.
- The database is never exposed to the internet.

## 3. DNS (A records → static IP)
- `letterlyn.com` and `www.letterlyn.com` (www redirects to the apex)
- `play.letterlyn.com`
- `api.letterlyn.com`
- `staging-api.letterlyn.com`
- Plus MX / SPF / DKIM for the email provider (section 10).

## 4. Software
- nginx
- Node.js 24 LTS
- MariaDB 11, bound to localhost only
- certbot (Let's Encrypt) with automatic renewal
- unattended-upgrades for security patches

## 5. Users and folders
- **Deploy user:** `letterlyn`, non-root, owns everything below.
- **No repo, no git, no source code on the server.** GitHub Actions builds on every push (`staging` branch → staging, `main` → production) and uploads only the finished files over SSH. The same steps also run as a script from Doru's Mac.
- **SSH keys on `letterlyn`:** the GitHub Actions deploy key (sent with M2) and Doru's key.
- **Sudo rule:** `letterlyn` may only restart `letterlyn-api` and `letterlyn-api-staging` (no password), nothing else.
- **Web roots:** `/srv/letterlyn/www/site` and `/srv/letterlyn/www/play`. They receive only built files.
- **API:** `/srv/letterlyn/api/releases/<date>` (bundled API + production packages), with `current` pointing at the live one. Rollback = point `current` at the previous release.

## 6. nginx sites (HTTPS everywhere, HTTP → HTTPS)
- **letterlyn.com** → `/srv/letterlyn/www/site`
- **play.letterlyn.com** → `/srv/letterlyn/www/play`
  - gzip on.
  - Long cache for hashed asset files (`/assets/*`), no cache for `index.html`.
- **api.letterlyn.com** → reverse proxy to `127.0.0.1:3000`
- **staging-api.letterlyn.com** → reverse proxy to `127.0.0.1:3001`

## 7. API services (systemd; files provided in M2)
- **Services:** `letterlyn-api` (port 3000) and `letterlyn-api-staging` (port 3001), `Restart=always`.
- **Secrets:** `/etc/letterlyn/api.env` and `/etc/letterlyn/api-staging.env`, mode 600, owned by `letterlyn`. Never in git.
- For now, just create `/etc/letterlyn/`.

## 8. Database
- **Databases:** `letterlyn_prod` and `letterlyn_staging`.
- **Users:** one per database, privileges only on its own database.

## 9. Backups
- **Database dump:** nightly dump of both databases (gzip) to a **private Lightsail bucket**, kept 30 days.
- **Snapshots:** the daily instance snapshots (section 1).
- **Restore test:** once, after the first real data.

## 10. Email
- **Addresses:** `support@letterlyn.com` (required by the app stores) and `privacy@letterlyn.com` (GDPR requests). A forward to Doru's inbox is enough.
- **Provider:** the company's usual one.

## 11. Monitoring
- **Lightsail alarms:** CPU > 80% and disk > 80% send email.
- **Uptime check:** free (e.g. UptimeRobot) on `https://api.letterlyn.com/health`, which arrives with M2.

## Priority
1. **Now** (before any store submission):
   - **Email:** section 10.
   - **Site:** sections 1–6 for letterlyn.com, so the privacy policy page has a home.
2. **Before M2 goes live:**
   - **API and database:** sections 7–9.
   - **Monitoring:** section 11.
