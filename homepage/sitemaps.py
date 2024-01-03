from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class mysiteMap(Sitemap):

    def items(self):
        return ['home', 'iceland', 'norway', 'winter', 'coversvol1', 'intheautumnforest', 'bc']

    def location(self, item):
        return reverse(item)
