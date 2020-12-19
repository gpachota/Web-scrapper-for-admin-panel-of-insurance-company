def set_model_name(model_name):
    model_name_list = ["iPhone 4s", "iPhone 4", "iPhone 5C", "iPhone 5S", "iPhone 5", "iPhone 6S Plus", "iPhone 6S", "iPhone 6 Plus", "iPhone 6",
                       "iPhone 7 Plus", "iPhone 7", "iPhone 8 Plus", "iPhone 8", "iPhone SE", "iPhone XS Max", "iPhone XS", "iPhone Xr", "iPhone X", "Iphone 11 Pro Max", "A3 2016",
                       "A3 2017", "A5 2015", "A5 2016", "A5 2017", "A8", "J1 J100", "J3 2016", "J3 2017", "J5 2015", "J5 2016", "J5 2017", "J7 2015", "J7 2016", "J7 2017",
                       "Note 3", "Note 4", "Note 8", "S6 Edge", "S6 Edge Plus", "S6", "S7 Edge", "S7", "S8 Plus", "S8+", "S8",
                       "S9 Plus", "S9+", "S9", "Xcover 3", "Xcover 4S", "Xcover 4", "Note 9", "A6+", "A6 PLUS",  "S5", "J4+", "J4 Plus", "S3 Neo",
                       "S5 Neo", "J6+", "Grand Prime SM-G531", "A9", "S10+", "S10 Plus", "S10e", "S10", "A50", "A40", "A80", "A20e", "A20s", "A31", "M51",
                       "A70", "A10", "A6", "J6", "Note 10+", "Note 10", "A30s", "E4", "E4G", "E500BT", "E50", "E5", "L1", "M21", "M2", "M2 Aqua", "M4 Aqua", "M5",
                       "T3", "X Performance F8131", "XA Ultra", "XA1 Ultra", "XA1", "XA2 Ultra", "XA2", "XA", "XZ", "XZ Premium", "Z1", "Z1 Compact", "Z2", "Z3", "Z3 Compact",
                       "Z5", "Z5 Compact", "XZ1", "XZ2", "XZ2 Compact", "XZ1 Compact", "Z5 Premium", "XZ3", "Z3+", "X Compact", "10 Plus", "Redmi Note 4", "Redmi 4X",
                       "Mi A2 Lite", "P20 Lite", "P9 Lite 2017 PRA-LX1", "G7 ThinQ", "7A", "Flip 3", "Charge 3", "FC6408/01", "SRSXB30B", "Charge 2Plus", "A51", "Xtreme",
                       "Flip 4", "EP ML992EE", "E45BT", "Xperia 10", "Xperia L3", "A71", "A7", "Free X", "Note 10 Lite", "E65BT", "BEATSX MTH62EE/A", "Solo3 Wireless",
                       "SYNCHROS E 50 4.0", "Xtreme 2", "MDR-XB950B1B", "Studio3 Wireless", "Xcover 4S G398", "E55BT", "Playstation 4",
                       "iPhone 11 Pro", "iPhone 11", "Charge 4", "Solo 2 Wireless", "Tune 600BT", "S20 Ultra 5G G988", "WH1000XM3", "Everest Elite 700", "S20+", "S20 Plus", "S20", "Boombox",
                       "Xperia L4", "A21s", "M31s", "M11"]

    model_name_list_real = ["iPhone 4s", "iPhone 4", "iPhone 5C", "iPhone 5S", "iPhone 5", "iPhone 6S Plus", "iPhone 6S", "iPhone 6 Plus", "iPhone 6", "iPhone 7 Plus",
                            "iPhone 7", "iPhone 8 Plus", "iPhone 8", "iPhone SE", "iPhone XS Max", "iPhone XS", "iPhone Xr", "iPhone X", "Iphone 11 Pro Max", "A3 A310",
                            "A3 A320", "A5 A500", "A5 A510", "A5 A520", "A8 A530", "J1 J100", "J3 J320", "J3 J330", "J5 J500", "J5 J510", "J5 J530", "J7 J700", "J7 J710", "J7 J730",
                            "Note 3 N9005", "Note 4 N910", "Note 8 N950", "S6 Edge G925", "S6 Edge Plus G928", "S6 G920", "S7 Edge G935",  "S7 G930", "S8 Plus G955", "S8 Plus G955", "S8 G950",
                            "S9 Plus G965", "S9 Plus G965", "S9 G960", "Xcover 3 G388", "Xcover 4S G398", "Xcover 4 G390", "Note 9 N960", "A6 PLUS A605", "A6 PLUS A605", "S5", "J4+ J415", "J4+ J415", "S3 Neo",
                            "S5 Neo", "J6+ J610", "Grand Prime SM-G531", "A9 A920", "S10+ G975", "S10+ G975", "S10e G970", "S10 G973", "A50 A505", "A40 A405", "A80 A805", "A20e A202", "A20s A207", "A31 A315", "M51 M515",
                            "A70 A705", "A10 A105", "A6 A600", "J6 J600", "Note 10+ N975", "Note 10 N970", "A30s A307", "E4", "E4G", "E500BT", "E50", "E5", "L1", "M21 M215", "M2", "M2 Aqua", "M4 Aqua", "M5",
                            "T3", "X Performance F8131", "XA Ultra", "XA1 Ultra", "XA1", "XA2 Ultra", "XA2", "XA", "XZ", "XZ Premium", "Z1", "Z1 Compact", "Z2", "Z3", "Z3 Compact",
                            "Z5", "Z5 Compact", "XZ1", "XZ2", "XZ2 Compact", "XZ1 Compact", "Z5 Premium", "XZ3", "Z3+", "X Compact", "10 Plus L4213", "Redmi Note 4", "Redmi 4X",
                            "Mi A2 Lite", "P20 Lite", "P9 Lite 2017 PRA-LX1", "G7 ThinQ", "7A", "Flip 3", "Charge 3", "FC6408/01", "SRSXB30B", "Charge 2Plus", "A51 A515", "Xtreme",
                            "Flip 4", "EP ML992EE", "E45BT", "Xperia 10", "Xperia L3", "A71 A715", "A7 A750", "Free X", "Note 10 Lite N770", "E65BT", "BEATSX MTH62EE/A", "Solo3 Wireless",
                            "SYNCHROS E 50 4.0", "Xtreme 2", "MDR-XB950B1B", "Studio3 Wireless", "Xcover 4S G398", "E55BT", "Playstation 4",
                            "iPhone 11 Pro", "iPhone 11", "Charge 4", "Solo 2 Wireless", "Tune 600BT", "S20 Ultra 5G G988", "WH1000XM3", "Everest Elite 700", "S20+ G985", "S20+ G985", "S20 G980", "Boombox",
                            "Xperia L4", "A21s A217", "M31s M317", "M11 M115"]

    for i in model_name_list:
        if i.lower() in model_name.lower():
            index = model_name_list.index(i)
            model = model_name_list_real[index]
            break

        else:
            model = model_name

    return(model)


def set_device_colour(device_info):
    colours = ["SPACE GRAY", "SPACE GREY", "ROSE GOLD", "CANARY YELLOW", "YELLOW", "AURA GLOW", "CERAMIC BLACK", "BLACK", "WHITE", "GREEN", "SILVER",
                "GOLD", "BLUE", "CORAL", "RED", "PURPLE", "TURKUS", "GREY", "PINK", "MORO", "N/A"]

    for i in colours:
        if i.lower() in device_info.lower():
            colour = i
            break
        else:
            colour = ""

    return(colour)
