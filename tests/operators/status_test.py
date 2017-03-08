import pook
import pytest
import requests


def test_status(should):
    pook.get('foo.com', reply=201)
    requests.get('http://foo.com') | should.be.status(201)

    pook.get('foo.com', reply=200)
    requests.get('http://foo.com') | should.be.status('OK')

    with pytest.raises(AssertionError):
        pook.get('foo.com', reply=500)
        requests.get('http://foo.com') | should.be.status('OK')


#
# def test_true_operator_message(should):
#     (TrueOperator
#         | should.have.property('kind')
#         > should.be.equal.to('accessor'))
#
#     (TrueOperator
#         | should.have.property('operators')
#         > should.be.equal.to(('true',)))
#
#     TrueOperator | should.have.property('aliases') > should.be.empty
#
#     TrueOperator | should.have.property('expected_message')
#
#
# def test_false_operator(ctx):
#     assert FalseOperator(ctx).match(False) == (True, [])
#     assert FalseOperator(ctx).match(True) == (False, [])
#
#     assert FalseOperator(ctx).match(0) == (False,
#                                            ['subject is not a bool type'])
#
#
# def test_false_operator_message(should):
#     (FalseOperator
#         | should.have.property('kind')
#         > should.be.equal.to('accessor'))
#
#     (FalseOperator
#         | should.have.property('operators')
#         > should.be.equal.to(('false',)))
#
#     FalseOperator | should.have.property('aliases') > should.be.empty
#
#     FalseOperator | should.have.property('expected_message')
