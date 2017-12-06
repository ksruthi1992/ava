import os
from datetime import datetime

import math
from elasticsearch import Elasticsearch
from hashids import Hashids

if __name__ == '__main__' and __package__ is None:
    os.sys.path.append(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ava.settings")

import django

from django.contrib.sessions.backends.db import SessionStore
django.setup()

from dashboard.models import User, Recipe, Recipe_Ingredient, Ingredient
import numpy as np
# session_key = 'ei4npjnrlqwewxedox5a991vtaor2bfh'
#
# # s = SessionStore()
# # key = s.create()
# # print s.session_key
# # user = User.objects.create(email="asd@fsd.com", password="sad", first_name="asd").save()
#
# es = Elasticsearch()
# # es.indices.create(index='my-index', ignore=400)
# es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
#
# print es.get(index="my-index", doc_type="test-type", id=42)['_source']['any']

recipe = Recipe.objects.get(id=1)

recipe_ings = Recipe_Ingredient.objects.filter(recipe_id=recipe.id)
recipe_ings_list = []
for i in recipe_ings:
    recipe_ings_list.append(i.ingredient_id)


#
user_ingredients = [1,4,6,8,10,44,56,67]
user_ingredients_tuple=tuple(user_ingredients)

recipe_ings_tuple = tuple(recipe_ings_list)
matching_ings = np.intersect1d(recipe_ings_list, user_ingredients)
print matching_ings.size
# hashids = Hashids()
#
# hashid_user = hashids.encode(*user_ingredients)
# hashid_recipe = hashids.encode(*recipe_ings_tuple)
# print hashid_user
# print hashid_recipe

# ints_list =  list(ints)
