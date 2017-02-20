from django.db import models

class MenuDetails(models.Model):
	CATEGORY_SOUP = "soup"
	CATEGORY_STARTER = "starter"
	CATEGORY_MAINCOURSE = "maincourse"
	CATEGORY_DESSERT = "dessert"

	menu_category_choice = (
		(CATEGORY_SOUP, "Soup"),
		(CATEGORY_STARTER, "Starter"),
		(CATEGORY_MAINCOURSE, "Main Course"),
		(CATEGORY_DESSERT, "Dessert")
	)

	menuid = models.AutoField(primary_key=True)
	menu_name = models.CharField(max_length=200)
	menu_description = models.CharField(max_length=200, null=True)
	menu_category = models.CharField(choices=menu_category_choice, max_length=20, null=True)
	price = models.FloatField()

	def __str__(self):
		return self.menu_name

	class Meta:
		db_table = 'menu_details'
