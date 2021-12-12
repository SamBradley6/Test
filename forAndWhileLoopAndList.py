[11:29] Bilal Shafiq
    sudo apt update && sudo apt install python3 -y
​[11:29] Bilal Shafiq
    sudo apt install python3-pip
​[11:45] Bilal Shafiq
    2. 
def f():
return 2 * 10 / 5 + (10-8) ** 2
def test_f():
assert f() == 8
​[11:45] Bilal Shafiq
    python3 -m pytest two_test.py
​[11:46] Bilal Shafiq
    def doubler(num):
return num * 2

def test_doubler():
assert doubler(6) == 12
​[11:46] Bilal Shafiq
    
pip3 install pytest-cov
​[11:47] Bilal Shafiq
    python3 -m pytest [file containing tests] --cov=[file to check coverage of]

