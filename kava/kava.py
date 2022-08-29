# Zeptejte se zákazníka, zda chce malou nebo velkou kávu.
# Zeptejte se zákazníka, zda chce ke kávě cukr.
# Zeptejte se zákazníka, zda chce ke kávě mléko.
# Oznamte zákazníkovi konečnou cenu kávy.


mleko_do_kavy = 2
mala_kava = 20
velka_kava = 30
cukr_do_kavy = 5

kava = input("Jakou kávu chcete?\n")

# Malá káva
if kava == "malou":
    # Malá káva s cukrem.
    cukr = input("Chcete cukr do kávy?\n")    
    if cukr == "ano":
        # Malá káva s cukrem a mlékem.
        mleko = input("Dáte si mléko do kávy?\n")
        if mleko == "ano":                
            print(f"Malá káva s cukrem a mlékem stojí {mala_kava + cukr_do_kavy + mleko_do_kavy} Kč.")
        # Malá káva s cukrem, ale bez mléka.
        elif mleko == "ne":
            print(f"Malá káva s cukrem stojí {mala_kava + cukr_do_kavy} Kč.")
        else:
            print("Dáte si ke kávě ještě něco?")
    # Malá káva bez cukru.
    elif cukr == "ne":
        # Malá káva bez cukru, ale s mlékem.      
        mleko = input("Dáte si mléko do kávy?\n")
        if mleko == "ano":                
            print(f"Malá káva s mlékem stojí {mala_kava + mleko_do_kavy} Kč.")
        # Malá káva bez cukru a bez mléka.
        elif mleko == "ne":
            print(f"Malá káva stojí {mala_kava} Kč.")
        else:
            print("Dáte si ke kávě ještě něco?")
    else:
        print("Dáte si ke kávě ještě něco?")
# Velká káva.
elif kava == "velkou":
    # Velká káva s cukrem  
    cukr = input("Chcete cukr do kávy?\n")
    if cukr == "ano":
        # Velká káva s cukrem a mléke.
        mleko = input("Chcete do kávy mléko?\n")
        if mleko == "ano":
            print(f"Velká káva s cukrem a mlékem stojí {velka_kava + cukr_do_kavy + mleko_do_kavy} Kč.")
        # Velká káva bez cukru a bez mléka.
        elif mleko == "ne":
            print(f"Velká káva s cukrem stojí {velka_kava + cukr_do_kavy} Kč.")
        else:
            print("Dáte si ke kávě ještě něco?")
    # Velká káva bez cukru.
    elif cukr == "ne":        
        mleko = input("Chcete do kávy mléko?\n")
        # Velká káva bez cukru, ale s mlékem.
        if mleko == "ano":
            print(f"Velká káva s mlékem stojí {velka_kava + mleko_do_kavy} Kč.")
        # Velká káva bez cukru a bez mléka.
        elif mleko == "ne":
            print(f"Velká káva stojí {velka_kava} Kč.")
        else:
            print("Dáte si ke kávě ještě něco?")
    else:
            print("Dáte si ke kávě ještě něco?")
else:
    print("Dáte si něco jiného?")
