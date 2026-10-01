# Issue Tracker API

A small REST API for creating, viewing, updating, and deleting issues. It is built with FastAPI and stores issues in a local JSON file.

## Run locally

From the project directory, create and activate a virtual environment in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the pinned dependencies from `requirements.txt` and start the development server:

```powershell
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive Swagger documentation is at `http://127.0.0.1:8000/docs`.

## Endpoints

All issue endpoints use the `/api/V1issues` prefix.

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/api/V1issues/` | List all issues |
| `POST` | `/api/V1issues/` | Create an issue |
| `GET` | `/api/V1issues/{issue_id}` | Get an issue by ID |
| `PUT` | `/api/V1issues/{issue_id}` | Update an issue |
| `DELETE` | `/api/V1issues/{issue_id}` | Delete an issue |

Issue IDs are generated as UUID strings when an issue is created. Copy the returned `id` to use it in the individual issue endpoints.

## Create an issue

Send a `POST` request to `/api/V1issues/` with a JSON body like:

```json
{
  "title": "Login page error",
  "description": "The login form returns an error for valid credentials.",
  "priority": "medium"
}
```

`title` must be 3-100 characters and `description` must be 10-1000 characters. `priority` can be `low`, `medium`, or `high`; if omitted, it defaults to `medium`. New issues start with `open` status.

For `PUT`, provide any fields to change. Supported status values are `open`, `in_progress`, and `closed`. Issues are stored in `data/issues.json`, which is created when the first issue is saved.