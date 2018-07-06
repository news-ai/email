# Email

Sending users daily emails about things that happen. This is emailing outside the API (welcome & confirmation emails). This is more to help increase engagement.

### Known bugs

- Daily emails are currently sent for only the newest 5,000 users
- Limit of 5,000 to all ES queries (users, emails, contacts, lists, etc.)

### Google Cloud

`gcloud compute --project "newsai-1166" ssh --zone "us-central1-c" "utilities-1"`
