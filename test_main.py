from main import *
import os
def test_findchronopost():
    relais=findchronopost('47.08962662991442','6.335217770257565','25580','LES PREMIERS SAPINS')
    assert len(relais)>0