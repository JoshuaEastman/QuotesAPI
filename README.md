# Quotes API (Django + DRF)

A tiny, production‑style demo that shows clean Django/DRF patterns, OpenAPI docs, and a minimal Tailwind UI.

> This is a demo application not designed for deployment.

---

## Quick Links (when running locally)

* **Admin:** http://localhost:8000/admin/
* **Docs (Swagger UI):** http://localhost:8000/quotes/docs/)
* **Demo UI:** [http://localhost:8000/quotes/demo/](http://localhost:8000/quotes/demo/
* **Health:** (http://localhost:8000/quotes/health/
* **Random Quote (JSON):** http://localhost:8000/quotes/v1/random/

> Paths may differ slightly if you’ve customized URLs; these are the defaults in this repo.

---

## Requirements

* **Python** ≥ 3.13
* **Node.js & npm** (for Tailwind build via `django-tailwind`)
* (Recommended) **virtual environment**: https://docs.python.org/3/library/venv.html

---

## Quickstart (Development)

### 1) Clone & enter

```bash
git clone git@github.com:JoshuaEastman/QuotesAPI.git
cd QuotesAPI
```

### 2) Create & activate a virtualenv

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux (bash):**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3) Install Python deps

```bash
pip install -r requirements.txt
```

### 4) Database migrations

```bash
python manage.py migrate
```

### 5) Tailwind (CSS) — one‑time install, then build

```bash
python manage.py tailwind install
python manage.py tailwind build
```

> For live dev watching, use: `python manage.py tailwind start` (Ctrl+C to stop)

### 6) Create an admin user

```bash
python manage.py createsuperuser
```

### 7) Run the server

```bash
python manage.py runserver
```

Open [http://localhost:8000/](http://localhost:8000/) and use the **Quick Links** above.

---

## Seeding Content

Visit **/admin/** and create a few Quotes (text, author, optional tag). The demo UI and API will use whatever you add.

---

## Endpoints

### GET `/quotes/v1/random/`

Returns a single random quote.

**Example response**

```json
{
  "id": 12,
  "text": "Simplicity is the soul of efficiency.",
  "author": "Austin Freeman",
  "tags": ["inspirational"],
  "language": "en"
}
```

> Exact fields reflect the serializer/model; see the Swagger UI for the authoritative schema.

### GET `/quotes/health/`

Simple health/uptime check.

### GET `/quotes/docs/`

OpenAPI 3.1.1 docs (Swagger UI). Useful for exploring the schema.

### GET `/quotes/demo/`

A tiny Tailwind front‑end that calls the random quote endpoint.

---

## Testing

This project uses `pytest` + `pytest-django`.

```bash
pip install pytest pytest-django
pytest -q
```

If needed, the repo includes a `pytest.ini` pointing to the Django settings module. Run tests from the project root (same folder as `manage.py`).

---

## Tailwind Notes

* This repo uses **django-tailwind**; Node/npm must be available.
* Build once with `python manage.py tailwind build`, or run the watcher with `python manage.py tailwind start` during development.
* Compiled assets live under `static/`. A `.gitkeep` is committed so the folder exists on fresh clones.

---

## Deployment (brief)

* Defaults to SQLite for local dev. For production, configure `DATABASE_URL` and `ALLOWED_HOSTS`.
* If you deploy with WhiteNoise, run `python manage.py collectstatic` and ensure `STATIC_ROOT` is set.

---

## License

MIT (see `LICENSE`).
