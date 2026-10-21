# Cars Dealership — Full-Stack Capstone

A responsive dealership directory with Django APIs, dealer/review pages, a React signup component, session login/logout, and review sentiment analysis.

## Stack
- Django + SQLite: API, server-rendered pages, authentication and admin
- React + Vite: registration component and frontend
- GitHub Actions: CI checks
- Docker: container deployment starter

## Deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/DakshDhaundiyal/Cars-Dealership-Full-Stack-Capstone-assignment)

Alternatively, open the [Render Blueprint setup page](https://dashboard.render.com/blueprint/new?repo=https://github.com/DakshDhaundiyal/Cars-Dealership-Full-Stack-Capstone-assignment), review the checked-in `render.yaml`, and choose **Deploy Blueprint**. After Render finishes provisioning, copy the actual service URL into the rubric's `deploymentURL` file and capture deployment screenshots from that live URL.

## Run locally
```bash
pip install -r requirements.txt
cd server
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. Django admin is at `/admin/`. A seed/demo account is `demo` / `DemoPass123!`; it is for local evaluation only and must be changed or removed before public production use.

Run the React frontend separately:
```bash
cd server/frontend
npm install
npm run dev
```

## API endpoints
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/djangoapp/api/dealers/` | List dealers; optionally `?state=Kansas` |
| GET | `/djangoapp/api/dealers/<id>/` | Dealer details |
| GET | `/djangoapp/api/dealers/<id>/reviews/` | Dealer reviews |
| POST | `/djangoapp/api/register/` | Create an account |
| POST | `/djangoapp/api/login/` | Start session |
| POST | `/djangoapp/api/logout/` | End session |
| POST | `/djangoapp/api/reviews/` | Post review (requires login) |
| GET | `/djangoapp/api/car-makes/` | Car makes and models |
| POST | `/djangoapp/api/analyze-review/` | Analyze text sentiment |

## Files for the rubric
- About Us: [server/frontend/static/About.html](server/frontend/static/About.html)
- Contact Us: [server/frontend/static/Contact.html](server/frontend/static/Contact.html)
- React Sign-up: [server/frontend/src/components/Register/Register.jsx](server/frontend/src/components/Register/Register.jsx)
- Evidence capture guide: [docs/EVIDENCE_CHECKLIST.md](docs/EVIDENCE_CHECKLIST.md)
- cURL examples: [docs/curl-examples.md](docs/curl-examples.md)

The terminal logs, screenshots, GitHub Actions run evidence and deployment URL in the assignment must be captured from an actually running app. Do not submit fabricated logs or represent a local page as a cloud deployment.

## Security and deployment
Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, and `DJANGO_ALLOWED_HOSTS` in production. Use HTTPS, secure session cookies, and a production database. Seed dealer listings and email addresses are illustrative sample data. Sentiment analysis is a lightweight lexicon-based demo.
