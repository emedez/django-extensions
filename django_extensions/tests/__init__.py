from django.db import models  # NOQA
from django_extensions.tests.test_dumpscript import DumpScriptTests
from django_extensions.tests.utils import TruncateLetterTests
from django_extensions.tests.json_field import JsonFieldTest
from django_extensions.tests.uuid_field import (UUIDFieldTest,
                                                PostgreSQLUUIDFieldTest)
from django_extensions.tests.shortuuid_field import ShortUUIDFieldTest
from django_extensions.tests.fields import AutoSlugFieldTest
from django_extensions.tests.management_command import CommandTest, ShowTemplateTagsTests
from django_extensions.tests.test_templatetags import TemplateTagsTests

__test_classes__ = [
    DumpScriptTests, JsonFieldTest, UUIDFieldTest, AutoSlugFieldTest, CommandTest,
    ShowTemplateTagsTests, TruncateLetterTests, TemplateTagsTests, ShortUUIDFieldTest,
    PostgreSQLUUIDFieldTest,
]

try:
    from django_extensions.tests.encrypted_fields import EncryptedFieldsTestCase
    __test_classes__.append(EncryptedFieldsTestCase)
except ImportError:
    pass
