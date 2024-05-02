import pytest

from Pyhon.conftest import DataLoad


@pytest.mark.usefixtures("DataLoad")
class TestExample2:

    def editprofile(self, DataLoad):
        print(DataLoad)
