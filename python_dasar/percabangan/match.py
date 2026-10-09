hari = "sabtu"

match hari:
    case "sabtu" | "Minggu":
        print("Libur!")
    case "senin":
        print("Semangat!")
    case _:
        print("Hari kerja")