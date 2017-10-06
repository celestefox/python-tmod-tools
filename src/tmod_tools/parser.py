from __future__ import absolute_import, division, print_function, unicode_literals

import hashlib
from builtins import *  # noqa: F401,F403

from construct import (Bytes, Checksum, Const, GreedyBytes, Int32sl, OnDemand, PascalString, Prefixed, PrefixedArray,
                       RawCopy, Struct, Tunnel, VarInt)
from future.utils import bytes_to_native_str as n

csharp_string = PascalString(VarInt, encoding=n(b"utf8"))
csharp_int32 = Int32sl


class HeaderlessZlib(Tunnel):
    r"""
    Compresses and decompresses the underlying stream with zlib, but drops the extra header/footer on both encide and decode.
    """

    __slots__ = ["level"]

    def __init__(self, subcon, level=None):
        super(HeaderlessZlib, self).__init__(subcon)
        self.level = level
        import zlib
        self.lib = zlib

    def _decode(self, data, context):
        return self.lib.decompress(data, -15)  # This means that it doesn't care that there are no headers

    def _encode(self, data, context):
        if self.level is None:
            return self.lib.compress(data)[2:-4]  # These slice off the header/footer
        else:
            return self.lib.compress(data, self.level)[2:-4]


tmod_file = Struct(
    "magic" / Const(b"TMOD"),
    "modloader_version" / csharp_string,
    "hash" / OnDemand(Checksum(Bytes(20), lambda data: hashlib.sha1(data).digest(), lambda this: this.data.data)),
    "signature" / Bytes(256),
    "data" / Prefixed(csharp_int32, RawCopy(HeaderlessZlib(Struct(
        "mod_name" / csharp_string,
        "mod_version" / csharp_string,
        "files" / PrefixedArray(csharp_int32, Struct(
            "file_name" / csharp_string,
            "file_contents" / Prefixed(csharp_int32, GreedyBytes)
        ))
    )))))
