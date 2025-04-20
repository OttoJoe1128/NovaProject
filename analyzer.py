def analyze_ecosystem(data):
    if not data:
        return "Veri yok."

    analysis = {
        "Toplam": sum(data),
        "Ortalama": sum(data) / len(data),
        "Maksimum": max(data),
        "Minimum": min(data)
    }

    return analysis
