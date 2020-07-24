import asana

client = asana.Client.access_token('1/712677614983068:cea1a3725eb49ac9d21fd473066261e9')

result = client.tasks.create_task(
    {
    "data": 
        {
        "approval_status": "pending",
        "assignee": "12345",
        "assignee_status": "upcoming",
        "completed": false,
        "completed_by": {
        "name": "Greg Sanchez"
        },
        "custom_fields": {
        "4578152156": "Not Started",
        "5678904321": "On Hold"
        },
        "due_at": "2019-09-15T02:06:58.147Z",
        "due_on": "2019-09-15",
        "external": {
        "data": "A blob of information",
        "gid": "my_gid"
        },
        "followers": [
        "12345"
        ],
        "html_notes": "<body>Mittens <em>really</em> likes the stuff from Humboldt.</body>",
        "liked": true,
        "name": "Buy catnip",
        "notes": "Mittens really likes the stuff from Humboldt.",
        "parent": "12345",
        "projects": [
        "12345"
        ],
        "resource_subtype": "default_task",
        "start_on": "2019-09-14",
        "tags": [
        "12345"
        ],
        "workspace": "12345"
        }
    }
}, opt_pretty=True)