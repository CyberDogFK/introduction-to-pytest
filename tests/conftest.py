import pytest
from stuff.accum import Accumulator


@pytest.fixture
# also have scope setting like (scope='session', 'class') where session it's run only once for every
def accum() -> Accumulator:
    yield Accumulator()  # take this value, and all next steps in function will be as "clean up"
    print("DONE with this test!")
