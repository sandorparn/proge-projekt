import random

def taringu_viskamine():
    input("Vajuta ENTER klahvi, et veeretada täringut")
    return random.randint(1, 6)

def liikumine():
    asukoht = 1

    while asukoht < 100:
        print(f"Sa oled positsioonil {asukoht}")

        taring = taringu_viskamine()
        print(f"Sa veeretasid {taring}")
        asukoht += taring

        #ussid
        if asukoht == 17:
            asukoht = 7
            print(f"Uss! Mine tagasi positsioonile {asukoht}.")
           
        elif asukoht == 54:
            asukoht = 34
            print(f"Uss! Mine tagasi positsioonile {asukoht}.")
           
        elif asukoht == 62:
            asukoht = 19
            print(f"Uss! Mine tagasi positsioonile {asukoht}.")
           
        elif asukoht == 64:
            asukoht = 60
            print(f"Uss! Mine tagasi positsioonile {asukoht}.")
           
        elif asukoht == 87:
            asukoht = 24
            print(f"Uss! Mine tagasi positsioonile {asukoht}.")
           
        elif asukoht == 93:
            asukoht = 73
            print(f"Uss! Mine tagasi positsioonile {asukoht}.")
           
        elif asukoht == 95:
            asukoht = 79
            print(f"Uss! Mine tagasi positsioonile {asukoht}.")
           
        elif asukoht == 98:
            asukoht = 75
            print(f"Uss! Mine tagasi positsioonile {asukoht}.")
           
        #redelid
        elif asukoht == 1:
            asukoht = 38
            print(f"Redel! Roni positsioonile {asukoht}.")
           
        elif asukoht == 4:
            asukoht = 14
            print(f"Redel! Roni positsioonile {asukoht}.")
           
        elif asukoht == 9:
            asukoht = 31
            print(f"Redel! Roni positsioonile {asukoht}.")
           
        elif asukoht == 21:
            asukoht = 42
            print(f"Redel! Roni positsioonile {asukoht}.")
           
        elif asukoht == 28:
            asukoht = 84
            print(f"Redel! Roni positsioonile {asukoht}.")
           
        elif asukoht == 51:
            asukoht = 67
            print(f"Redel! Roni positsioonile {asukoht}.")
           
        elif asukoht == 71:
            asukoht = 91
            print(f"Redel! Roni positsioonile {asukoht}.")
           
        elif asukoht == 80:
            asukoht = 100
            print(f"Redel! Roni positsioonile {asukoht}.")
           

    print("Palju õnne! Sa jõudsid finišisse!")
         
liikumine()