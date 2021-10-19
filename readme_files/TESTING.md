## Testing

---

### Functionality Testing

### Compatibility Testing

### User Story Testing

### Admin User Story Testing

### Issues and Bugs

1.

Error running python3 manage.py migrate

Hadn't saved so there was nothing to migrate. This issue was resolved when file was saved.

2.

Error when running the site using python3 manage.py runserver in the development environment.

Error was occuring as the `{% extends 'base.html' %}` templating was missing `''`.

When the `''` were added everything works as expected.

3.

Database info was still being push to github despite `*.sqlite3` being in the .gitignore.

Added `db.sqlite3` to the .gitignore file to rectify this.

4.

Error trying to load /camps page in development environment.

The error was showing whenever trying to manually view the camps page and test this works by typing /camps at the end of the url.

The `''` had been missed off `return render` in views.py. When the `''` were added everything worked as expected.

5.

The no image fill wasn't showing when no image was submitted with a data entry on the admin panel.

There was a typo in the link and this was rectified. This may need editing again later when static files are linked to aws.

6.

Error when trying to display camps by a certain category. No camps were showing when a category was selected from the dropdown.

This is was generated due to a vital missing part in views.py of the camps folder. `.split(',')` was missging from the end of `request.GET['categories']` so the relayed information wasn't matching that requested from the url.

When `.split(',')` was added everything worked as expected.

### Performance Testing

### Code Validation

[Back to Table of Contents](README.md#table-of-contents)