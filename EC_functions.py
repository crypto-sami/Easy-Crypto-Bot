
work1mine = 25
work1_success = 2
cpul1 = (f"The level 1 CPU - Intel Core I5-7600K\n")
ram1 = (f"The level 1 RAM - 8Gb running at 2400Mhz\n")
gpu1 = (f"The level 1 GPU - GTX 1070 with 8Gb VRAM\n")
psu1 = (f"The level 1 Power Supply - Seasonic 550 Watt PSU\n")

work2mine = 20
work2_success = 2
cpul2 = (f"The level 2 CPU - Intel Core I7-7700K\n")
ram2 = (f"The level 2 RAM - 16Gb running at 2400Mhz\n")
gpu2 = (f"The level 2 GPU - GTX 1080 with 8Gb VRAM\n")
psu2 = (f"The level 2 Power Supply - Thermaltake 650 Watt PSU\n")

work3mine = 15
work3_success = 2
cpul3 = (f"The level 3 CPU - Intel Core I7-11700K\n")
ram3 = (f"The level 3 RAM - 16Gb running at 3200Mhz\n")
gpu3 = (f"The level 3 GPU - RTX 2070 with 8Gb VRAM\n")
psu3 = (f"The level 3 Power Supply - Cooler Master 750 Watt PSU\n")

work4mine = 10
work4_success = 2
cpul4 = (f"The level 4 CPU - Intel Core I9-10900K\n")
ram4 = (f"The level 4 RAM - 32Gb running at 3000Mhz\n")
gpu4 = (f"The level 4 GPU - RTX 3080 with 10Gb VRAM\n")
psu4 = (f"The level 4 Power Supply - EVGA 950 Watt PSU\n")

work5mine = 5
work5_success = 2
cpul5 = (f"The level 5 CPU - Intel Core I9-11900K\n")
ram5 = (f"The level 5 RAM - 64Gb running at 3600Mhz\n")
gpu5 = (f"The level 5 GPU - RTX 3090 with 24Gb VRAM\n")
psu5 = (f"The level 5 Power Supply - EVGA 1100 Watt PSU\n")

def print_w(workstation):
    if workstation == 1:
        msg = cpul1 + ram1 + gpu1 + psu1
        return(msg)
    if workstation == 2:
        msg = cpul2 + ram2 + gpu2 + psu2
        return(msg)
    if workstation == 3:
        msg = cpul3 + ram3 + gpu3 + psu3
        return(msg)
    if workstation == 4:
        msg = cpul4 + ram4 + gpu4 + psu4
        return(msg)
    if workstation == 5:
        msg = cpul5 + ram5 + gpu5 + psu5
        return(msg)

