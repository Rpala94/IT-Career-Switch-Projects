from collections import namedtuple

country = namedtuple("country", ["name", "capital", "continent"])

France = country("France", "Paris", "europe")
senegal = country("Senegal", "Dakar", "africa")
japan = country("Japan","Tokyo", "Asia")

countries = (japan, France, senegal)