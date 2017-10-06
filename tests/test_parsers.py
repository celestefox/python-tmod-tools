from __future__ import absolute_import, division, print_function, unicode_literals

import os
from builtins import *  # noqa: F401,F403
from pathlib import Path

from construct import GreedyString
from future.utils import bytes_to_native_str as n
from hypothesis import given
from hypothesis.strategies import text

from tmod_tools import parser


def test_csharp_string_basic():
    assert parser.csharp_string.parse(b"\x06\x30\x2e\x31\x30\x2e\x31") == u"0.10.1"


@given(text())
def test_csharp_string_roundtrip(string):
    assert parser.csharp_string.parse(parser.csharp_string.build(string)) == string


@given(text())
def test_HeaderlessZlib_roundtrip_string(string):
    class_ = parser.HeaderlessZlib(GreedyString(encoding=n(b'utf8')))
    assert class_.parse(class_.build(string)) == string
    class2 = parser.HeaderlessZlib(GreedyString(encoding=n(b'utf8')), level=0)
    assert class2.parse(class2.build(string)) == string


def test_ExampleMod():
    filebytes = None
    examplemod = Path(os.path.dirname(os.path.abspath(__file__))) / 'ExampleMod.tmod'
    with examplemod.open('r+b') as f:
        filebytes = f.read()
    parsed = parser.tmod_file.parse(filebytes)
    assert parsed.magic == b"TMOD"
    assert parsed.modloader_version == u"0.10.1"
    assert parsed.hash() == b'\xee\x07\xcc\xec\xd7\xaa\xd8D\xd8\xfek[\xf5\x08Y\xcf2\xcf<\xa9'
    assert parsed.data.value.mod_name == u"ExampleMod"
    assert parsed.data.value.mod_version == u"0.10.1"
    assert parsed.data.value.files[0].file_name == u"Info"
