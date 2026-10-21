# cURL commands for the assignment
Start Django on `127.0.0.1:8000` and run these from Git Bash/macOS/Linux. On Windows PowerShell use `curl.exe` and be mindful of shell quoting.

## Task 9 — getalldealers
```bash
curl -sS http://127.0.0.1:8000/djangoapp/api/dealers/
```

## Task 10 — getdealerbyid
```bash
curl -sS http://127.0.0.1:8000/djangoapp/api/dealers/1/
```

## Task 8 — getdealerreviews
```bash
curl -sS http://127.0.0.1:8000/djangoapp/api/dealers/1/reviews/
```

## Task 11 — getdealersbyState
```bash
curl -sS 'http://127.0.0.1:8000/djangoapp/api/dealers/?state=Kansas'
```

## Task 5 — loginuser (save session cookie)
```bash
curl -i -c cookies.txt -X POST http://127.0.0.1:8000/djangoapp/api/login/ -H 'Content-Type: application/json' -d '{"username":"demo","password":"DemoPass123!"}'
```

## Task 6 — logoutuser (same cookie jar)
```bash
curl -i -b cookies.txt -c cookies.txt -X POST http://127.0.0.1:8000/djangoapp/api/logout/ -H 'Content-Type: application/json' -d '{}'
```

## Tasks 14–15 — getallcarmakes
```bash
curl -sS http://127.0.0.1:8000/djangoapp/api/car-makes/
```

## Task 16 — analyzereview
```bash
curl -sS -X POST http://127.0.0.1:8000/djangoapp/api/analyze-review/ -H 'Content-Type: application/json' -d '{"review":"Fantastic services"}'
```

## Posting a review while authenticated
```bash
curl -i -b cookies.txt -X POST http://127.0.0.1:8000/djangoapp/api/reviews/ -H 'Content-Type: application/json' -d '{"dealer_id":1,"rating":5,"review":"Fantastic services"}'
```

Save each command and its actual output in the exact root filenames from the rubric only after executing it against the running server.
