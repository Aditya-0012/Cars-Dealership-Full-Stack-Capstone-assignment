# Deployment checklist

The repository includes a Dockerfile for building the Django application. A public deployment URL is issued by the hosting provider only after the application is deployed to a project/account you control.

## Before deploying

1. Easiest option: connect your Render account, choose **New → Blueprint**, and select this repository; Render reads the checked-in `render.yaml`. Alternatively, create a web/container service from the Dockerfile.
2. Set `DJANGO_SECRET_KEY` to a long random secret, `DJANGO_DEBUG=False`, and `DJANGO_ALLOWED_HOSTS` to the exact public hostname provided by your host.
3. If React is served from another origin, update `server/config/cors_middleware.py` to allow only that origin.
4. Review database persistence: this coursework starter uses SQLite, which may be ephemeral on container hosts. Use a persistent disk or PostgreSQL before relying on stored reviews.
5. Deploy and verify both `/` and `/djangoapp/api/dealers/`, then save the provider-issued public URL in the rubric's `deploymentURL` file.
6. In GitHub, open **Actions → Capture deployed submission screenshots → Run workflow** and paste the real service URL. The workflow registers a temporary evidence user, captures `deployed_landingpage.png`, `deployed_loggedin.png`, `deployed_dealer_detail.png`, and `deployed_add_review.png` from the live hostname, saves the actual URL to `deploymentURL`, and commits the evidence files. It will fail rather than capture screenshots if the supplied site is not responding with the expected dealer API.

Do not enter a guessed hostname in `deploymentURL`: the URL must be issued by the provider and verified reachable.

## Local smoke test

```bash
docker compose up --build
```

Then visit `http://127.0.0.1:8000/`. The CI workflow also runs Django's checks/tests and builds the React registration UI.
