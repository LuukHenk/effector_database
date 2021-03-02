# Effector database app
#### Version 0.0.1
{{Intro and reference}}

## Quick start
To append the effector database app to your website, copy this directory in the same directory as the `manage.py` file.
`
.
├── effector_database
├── manage.py
└── my_project
`

In your site folder, go to `urls.py` and append the database path:
`
urlpatterns = [
	path("database/", include("database.urls")),
	path("admin/", admin.site.urls),
]

`

### Options
{{basic other options in the tool}}

