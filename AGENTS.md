# Public distribution repository

This repo contains intentionally public Infinite Audience connection configuration and documentation. Do not add platform source, credentials, customer records, environment files, or internal reviewer/submission details.

Preserve each client's schema. Keep endpoint and billing disclosures consistent; avoid hard-coded tool counts. Update only confirmed listing and compatibility statuses. Configuration validation does not establish successful live OAuth.

Run `python3 scripts/validate.py` after changes. Review the full public diff before publishing. Live verification should use authentication and tool listing; billable matching/delivery requires separate explicit authorization. Do not automate paid test calls.

Respect the user's publication permissions. Do not submit to new directories, add gallery-discovery topics, or change approval policies just because configuration files exist. Prefer one repository with vendor-specific formats/artifacts over one repository per vendor.
