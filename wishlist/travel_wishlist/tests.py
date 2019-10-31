from django.test import TestCase
from django.urls import reverse

from .models import Place

class TestHomePageIsEmptyList(TestCase):

    def test_load_home_page_shows_empty_list(self):
        response = self.client.get(reserve('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assetFalse(response.context['places'])
        self.assertContains(response, 'You have no places in your wishlist')
        



