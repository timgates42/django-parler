# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase

from parler.templatetags.parler_tags import _url_qs
from parler.utils import get_parler_languages_from_django_cms
from parler.utils.i18n import get_language_title


class UtilTestCase(TestCase):

    def test_get_parler_languages_from_django_cms(self):
        cms = {
            1: [
                {
                    'code': 'en',
                    'fallbacks': ['es'],
                    'hide_untranslated': True,
                    'name': 'English',
                    'public': True,
                    'redirect_on_fallback': True
                },
                {
                    'code': 'es',
                    'fallbacks': ['en'],
                    'hide_untranslated': True,
                    'name': 'Spanish',
                    'public': True,
                    'redirect_on_fallback': True
                },
                {
                    'code': 'fr',
                    'fallbacks': ['en'],
                    'hide_untranslated': True,
                    'name': 'French',
                    'public': True,
                    'redirect_on_fallback': True
                }
            ],
            'default': {
                'fallbacks': ['en', ],
                'hide_untranslated': True,
                'public': True,
                'redirect_on_fallback': True
            }
        }

        parler = {
            1: [
                {
                    'code': 'en',
                    'fallbacks': ['es'],
                    'hide_untranslated': True,
                    'redirect_on_fallback': True
                },
                {
                    'code': 'es',
                    'fallbacks': ['en'],
                    'hide_untranslated': True,
                    'redirect_on_fallback': True
                },
                {
                    'code': 'fr',
                    'fallbacks': ['en'],
                    'hide_untranslated': True,
                    'redirect_on_fallback': True
                }
            ],
            'default': {
                'fallbacks': ['en', ],
                'hide_untranslated': True,
                'redirect_on_fallback': True
            }
        }

        computed = get_parler_languages_from_django_cms(cms)
        for block, block_config in computed.items():
            self.assertEqual(computed[block], parler[block])

    def test_get_language_title(self):
        """Test get_language_title utility function"""
        language_code = 'en'
        self.assertEqual(get_language_title(language_code), 'English')

        # Test the case where requested language is not in settings.
        # We can not override settings, since languages in get_language_title()
        # are initialised during import. So, we use fictional language code.
        language_code = 'xx'
        try:
            self.assertEqual(get_language_title(language_code), language_code)
        except KeyError:
            self.fail(
                "get_language_title() raises KeyError for missing language")

    def test_url_qs(self):
        matches = [
            ('http://www.example.com/search/', 'q=è453è5p4j5uih758')
        ]
        for match in matches:
            merged = _url_qs(match[0], match[1])
            self.assertTrue(merged)