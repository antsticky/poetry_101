from packageB.utils import info as infoB
from packageA.utils import info as infoA

def main():
    infoA()
    infoB()

if __name__ == '__main__':
    main()