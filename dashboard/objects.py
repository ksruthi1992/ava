class User:

    def __init__(self, email, username, name, age):
        self.email = email
        self.username = username
        self.name = name
        self.age = age

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


class Recipe:

    def __init__(self, ingredients, directions, recipe_meta, feedback):
        self.ingredients = ingredients
        self.directions = directions
        self.recipe_meta = recipe_meta
        self.feedback = feedback

    def get_ingredients(self):
        return self.ingredients

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def get_directions(self):
        return self.directions

    def set_directions(self, directions):
        self.directions = directions

    def get_recipe_meta(self):
        return self.recipe_meta

    def set_recipe_meta(self, recipe_meta):
        self.recipe_meta = recipe_meta

    def get_feedback(self):
        return self.feedback

    def set_feedback(self, feedback):
        self.feedback = feedback

class Pantry:

    def __init__(self, user, ingredients):
        self.user = user
        self.ingredients = ingredients

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_ingredients(self):
        return self.ingredients

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients