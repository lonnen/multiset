# -*- coding: utf-8 -*-
import pytest

from multiset import Multiset, FrozenMultiset

@pytest.fixture(autouse=True)
def add_default_expressions(doctest_namespace):
    doctest_namespace['Multiset'] = Multiset
    doctest_namespace['FrozenMultiset'] = FrozenMultiset

def pytest_generate_tests(metafunc):
    if 'MultisetCls' in metafunc.fixturenames:
        metafunc.parametrize('MultisetCls', ['frozen', 'regular'], indirect=True)

@pytest.fixture
def MultisetCls(request):
    if request.param == 'frozen':
        return FrozenMultiset
    elif request.param == 'regular':
        return Multiset
    else:
        raise ValueError("Invalid internal test config")
