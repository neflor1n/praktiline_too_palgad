
from MyModul import*


palgad = [1200,2500,750,395,1200]
inimesed = ["A","B","C","D","E"]

while True:
    print("\n###########\n0 - Naita andmed veerudes\n1 - andmete lisamine\n2 - Andmete eemaldamine\n3 - kellel on suurim palk\n"
          "4- kellel on vaiksem palk\n5 - sorteerimine Z-A\n6 - sorteerimine A-Z")
    valik = int(input())
    if valik == 1:
        inimesed, palgad = inimeste_ja_palkade_liisamine(inimesed,palgad,int(input("Mitu inimest lisame?")))
    elif valik == 0:
        andmed_veerudes(inimesed, palgad)
    elif valik == 2:
        andmete_eemaldamine_nimi_jargi(inimesed, palgad)
    elif valik == 3:
        print(kellel_on_suurim_palk(inimesed, palgad))
    elif valik == 4:
        print(kellel_on_vaiksem_palk(inimesed, palgad))
    elif valik == 5:
        print(sorteerimineZ_A(inimesed, palgad))
    elif valik == 6:
        print(sorteerimineA_Z(inimesed, palgad))
