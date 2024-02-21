from typing import Type


def summa(arv1:int, arv2:int, arv3 = 0) -> int:
    """ Funksioon tagastab kolme arvu summa
    Summa(arv1, arv2, arv3)
    :param int arv1: arv1 sisetab kasutaja:
    :param int arv2: arv2 sisetab kasutaja:
    :param int arv3: arv3 sisetab kasutaja:
    rtupe: int
    """
    s = arv1 + arv2 + arv3
    return 
def IntKontroll(x):
    """ Funksioon tagastab sissestatud andme õiges formaadis 
    IntKontroll()
    rtype: any
    """
    x = input("sisetage andmed")
    try:
        x = int(x)
        return int(x)
    except:
        try:
            x = float(x)
        except:
            return str(x)

def arifmetic(arv1:int, arv2:int, argument):
    if argument == "-":
        s = arv1 - arv2
    elif argument == "+":
        s = arv1 + arv2
    elif argument == "/":
        if arv2 == 0:
            print("vale andmed(null)")
        else:
             s = arv1 / arv2  
    elif argument == "*":
        s = arv1 * arv2       
        return s
    

