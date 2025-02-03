from requests import get, post, put, delete, HTTPError


def test_api():
    """
    An automated version of the manual testing I've been doing,
    testing the lifecycle of an inserted document.
    """
    root = "http://localhost:8000/"
    proj_root = f"{root}projects/"
    wl_root = f"{root}worklogs/"


    initial_proj = {
        "title": "projecttest",
        "code": "PJT",
        "description": "Project sample",
    }

    try:
        response = get(root)
        response.raise_for_status()

        # # Insert a project
        response = post(proj_root, json=initial_proj)
        response.raise_for_status()
        doc = response.json()
        print(doc)
        inserted_proj_id = doc["id"]
        print(f"Inserted document with id: {inserted_proj_id}")
        assert doc["title"] == "projecttest"
        assert doc["code"] == "PJT"
        assert doc["description"] == "Project sample"

        # # List project and ensure it's present
        response = get(proj_root)
        response.raise_for_status()
        projs = response.json()
        print(projs)
        proj_ids = [s["id"] for s in projs.get('projects')]
        assert inserted_proj_id in proj_ids

        # # Insert a worklog
        worklog_doc = {
            "day": "2024-02-02",
            "worked_hours": 2,
            "descr": "Dev and fix app",
            "ref_activity": inserted_proj_id
        }
        response = post(wl_root, json=worklog_doc)
        response.raise_for_status()
        doc = response.json()
        print(doc)
        inserted_wl_id = doc["id"]
        print(f"Inserted document with id: {inserted_wl_id}")
        assert doc["day"] == "2024-02-02"
        assert doc["worked_hours"] == 2
        assert doc["descr"] == "Dev and fix app"

        # # List worklog and ensure it's present
        response = get(wl_root)
        response.raise_for_status()
        wls = response.json()
        print(wls)
        wl_ids = [s["id"] for s in wls.get('worklogs')]
        assert inserted_wl_id in wl_ids


        # Get the worklog doc
        response = get(wl_root + inserted_wl_id)
        response.raise_for_status()
        doc = response.json()
        print(doc)

        # # Delete worklog
        response = delete(wl_root + inserted_wl_id)
        response.raise_for_status()

        # Get the project doc
        response = get(proj_root + inserted_proj_id)
        response.raise_for_status()
        doc = response.json()
        print(doc)

        # # Delete project
        response = delete(proj_root + inserted_proj_id)
        response.raise_for_status()

    except HTTPError as he:
        print(he.response.json())
        raise

if __name__ == "__main__":
    test_api()