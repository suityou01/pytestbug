#!/usr/bin/env python3
import pytest
from  targetcode.modulea import MyModule

class TestSuite:
    def test_one(self,shared_fixture):
        assert shared_fixture=="From shared fixture"

    def test_two(self,shared_fixture):
        t = MyModule(shared_fixture)
        assert t._db == shared_fixture