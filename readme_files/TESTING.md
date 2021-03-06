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

Error was occuring as the {% extends 'base.html' %} templating was missing ''.

When the '' were added everything works as expected.

3.

Database info was still being push to github despite *.sqlite3 being in the .gitignore.

Added db.sqlite3 to the .gitignore file to rectify this.

4.

Error trying to load /camps page in development environment.

The error was showing whenever trying to manually view the camps page and test this works by typing /camps at the end of the url.

The '' had been missed off return render in views.py. When the '' were added everything worked as expected.

5.

The no image fill wasn't showing when no image was submitted with a data entry on the admin panel.

There was a typo in the link and this was rectified. This may need editing again later when static files are linked to aws.

6.

Error when trying to display camps by a certain category. No camps were showing when a category was selected from the dropdown.

This is was generated due to a vital missing part in views.py of the camps folder. .split(',') was missging from the end of request.GET['categories'] so the relayed information wasn't matching that requested from the url.

When .split(',') was added everything worked as expected.

7.

Error when trying to load camp page preview in development environment. Error saying redirect is undefined.

Missing redirect import at the top of bag views.url.

When this was added the problem was rectified.

8.

Error when viewing the cbag page when an item was there that had no image to load (had the no image fill image on camp page)

This was causing the page to run an error as { item.camp.image.url } was looking for an image that didn't exist.

Added an if statement to show the no image fill if an image doesn't exist. This now works as expected.

9.

When clicking the increment or decrement buttons the value would'nt increase or decrease it would just submit the item to the bag.

This was caused due to the use of jQuery and not having the script tag to link to the jQuery CDN.

When this was added the buttons worked as expected.

10.

Error when trying to submit payment information in checkout page. Card field would freeze (disable) and the information wouldn't submit.

Forgot to link client secret variable from python file to javascript file. `{{ client_secret|json_script:"id_client_secret" }}` was added to base.html page.

When this was added everything worked as expected.

11.

When submitting payment user was directed to the camps page instead of the success page. Using print statements I found the checkout view wasn't reciving a POST method hence the ridect as stated in the else if the if statement below.

This was caused do to a mistake in the url templating route. `{% url 'camps' %}` was specified in the action of the form instead of `{% url 'checkout' %}`

When this was ammend the form behaved as expected.

12.

Error when deleting orders from the admin console. This error was caused due to a value of None being passed when attemping to delete an order throwing an error statement.

This was fixed by adding an `or 0` to the end of `self.total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0`

The admin console now allows orders to be deleted without an error showing.

13.

Error when trying to test the delete function created in camps/views.py

Page was showing a routing error when the url to delete a product id was typed in. This was fixed by addin a `/` to the end of the delete url so the url's path read `'delete/<int:camp_id>/'`.

Everything worked as expected when the forward slash was added to this path.

14.

Aplication Error when trying to load app in Heroku for the first time. When looking at the logs the system wasn't connecting to Heroku because the DATABASE_URL wasn't being called correctly and the Proficle app wasn't defined correctly.

This was fixed by adding `os.environ.get` to the database dictionary for the heroku app. The app I was trying to connect to in the procfile worked when the letter case errors were corrected.

Eveything worked as expected when these changes were made.

### Performance Testing

### Code Validation

[Back to Table of Contents](README.md#table-of-contents)