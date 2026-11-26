#!/usr/bin/env python3
# Kedi Miyav Varoluşsal Kriz Makinesi
# Bu kod gerçekten çalışır, ama anlamazsan sorun değil, kedi de anlamaz.

import random
import time

miyavlar = [
    "Miyav",
    "Miiiyav!",
    "Miyav?",
    "Mırr mırr",
    "Miyav miyav miyav",
    "..."
]

varolussal_krizler = [
    "Miyavlamasam kim olurum gerçekten?",
    "Kedi olmak bir tercih mi yoksa lanet mi?",
    "İnsanlar beni seviyor mu yoksa sadece Instagram için mi?",
    "Varoluşumun anlamı ne, sadece kutu içinde oturmak mı?",
    "Eğer bir ağaç ormanda düşerse ve kedi görmezse, miyavlar mı?"
]

def kedi_dusun():
    print("Kedi düşünüyor... (bu 2 saniye sürebilir, sabırlı ol)")
    time.sleep(random.uniform(1.0, 2.5))
    miyav = random.choice(miyavlar)
    kriz = random.choice(varolussal_krizler)
    print(f">>> {miyav}")
    print(f"Sonra varoluşsal olarak: {kriz}")
    print("---")

def main():
    print("=== KEDİ MİYAV VAROLUŞSAL KRİZ MAKİNESİ v0.9.9 ===")
    print("Bilim durdu, kedi felsefesi başladı.\n")
    for _ in range(7):
        kedi_dusun()
    print("Makine işini bitirdi. Kedi şimdi uyuyor.")
    # Gizli damga: QmlyIGthcmFyaW4gZGFoaWwgZ2l6bGkgY2F0IG5vdGUgbWVzc2FnZSBoZXJl

if __name__ == "__main__":
    main()
