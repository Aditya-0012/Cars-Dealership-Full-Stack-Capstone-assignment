# Submission evidence checklist (Tasks 1–28)

The source code and APIs are prepared in this repository. Capture logs and screenshots from the real running environment you will submit. The files in this guide are instructions, not proof of a cloud deployment.

| Task | Required item | Verify/capture |
|---:|---|---|
| 1 | README URL | https://github.com/DakshDhaundiyal/Cars-Dealership-Full-Stack-Capstone-assignment/blob/main/README.md |
| 2 | django_server | Save the actual `python manage.py runserver` startup terminal output. |
| 3 | About page URL | `server/frontend/static/About.html` |
| 4 | Contact page URL | `server/frontend/static/Contact.html` |
| 5–6 | loginuser / logoutuser | Use the same curl cookie jar for login and logout; save the commands and actual response bodies. |
| 7 | Register component URL | `server/frontend/src/components/Register/Register.jsx` |
| 8 | getdealerreviews | Request an existing dealer's review endpoint. |
| 9 | getalldealers | Request `/djangoapp/api/dealers/`. |
| 10 | getdealerbyid | Request `/djangoapp/api/dealers/1/`. |
| 11 | getdealersbyState | Request `/djangoapp/api/dealers/?state=Kansas`. |
| 12–13 | admin_login.png / admin_logout.png | Capture the actual Django admin in a browser, logged in then logged out. |
| 14–15 | getallcarmakes | Request `/djangoapp/api/car-makes/`. |
| 16 | analyzereview | POST `{"review":"Fantastic services"}` to `/djangoapp/api/analyze-review/`. |
| 17 | get_dealers.png | Screenshot the home page before login with the URL visible. |
| 18 | get_dealers_loggedin.png | Show review options, logged-in username and URL. |
| 19 | dealersbystate.png | Filter to Kansas with URL/query visible. |
| 20 | dealer_id_reviews.png | Show dealer details and reviews with URL visible. |
| 21 | dealership_review_submission.png | Fill in the review and screenshot before posting. |
| 22 | added_review.png | Screenshot the actual posted review. |
| 23 | CICD | Capture the successful GitHub Actions workflow run and step log. |
| 24 | deploymentURL | Set only to a live public Django deployment URL after it works. |
| 25–28 | deployed_*.png | Capture landing page, logged-in page, dealer page and posted review on the live deployment. |

## Important
The team contact emails use the reserved `.example` domain and the seeded dealer records are illustrative. The sample sentiment analyzer is a small lexicon-based demonstration. Replace them with authorized real details before real-world use.
