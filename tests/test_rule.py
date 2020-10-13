from common_import import *

from ml_workflow.rule import Rule

def test_rule_with_args():
    @ml_workflow.rule(name = 'incrementation')
    def f(x):
        return x + 1

    assert(f(5) == 6)
    assert(f.name == 'incrementation')
    assert('def f(x):' in f.get_source())
    assert(isinstance(f, Rule))

def test_rule_without_args():
    @ml_workflow.rule
    def g(x):
        return x + 2

    assert(g(5) == 7)
    assert(g.name == 'g')
    assert('def g(x):' in g.get_source())
    assert(isinstance(g, Rule))