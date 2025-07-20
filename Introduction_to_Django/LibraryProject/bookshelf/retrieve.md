## how to reteive  and view data

### command
'''python
book = Book.objects.get(title="1984")
 book.__dict__


 ### output
 '''bash
 {'_state': <django.db.models.base.ModelState object at 0x000001BAC8D5E780>, 'id': 2, 'title': 'valkyrie', 'author': 'james', 'publication_year': 2025}