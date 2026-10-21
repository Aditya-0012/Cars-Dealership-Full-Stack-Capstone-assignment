# Deployment checklist

The repository includes a Dockerfile for building the Django application. A public deployment URL is issued by the hosting provider only after the application is deployed to a project/account you control.

## Before deploying

1. Create a web/container service from this repository or build its Dockerfile.
2. Set `DJANGO_SECRET_KEY` to a long random secret, `DJANGO_DEBUG=False`, and `DJANGO_ALLOWED_HOSTS` to the exact public hostname provided by your host.
3. If React is served from another origin, update `server/config/cors_middleware.py` to allow only that origin.
4. Review database persistence: this coursework starter uses SQLite, which may be ephemeral on container hosts. Use a persistent disk or PostgreSQL before relying on stored reviews.
5. Deploy and verify both `/` and `/djangoapp/api/dealers/`, then save the provider-issued public URL in the rubric's `deploymentURL` file.
6. Capture `deployed_landingpage.png`, `deployed_loggedin.png`, `deployed_dealer_detail.png`, and `deployed_add_review.png` from the live hostname with the actual browser address bar visible.

Do not enter a guessed hostname in `deploymentURL`: the URL must be issued by the provider and verified reachable.

## Local smoke test

```bash
docker compose up --build
```

Then visit `http://127.0.0.1:8000/`. The CI workflow also runs Django's checks/tests and builds the React registration UI.
