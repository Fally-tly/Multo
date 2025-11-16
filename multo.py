import time
import sys

def ketik_teks(teks, kecepatan=0.01):
    """Menampilkan teks dengan efek typewriter."""
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(kecepatan)
    print()  # ganti baris


def jalanin_lirik():
    # Lirik + jeda per baris
    lirik = [
        ("'Di mo ba ako lilisanin?", 0.9),
        ("Hindi pa ba sapat pagpapa­hirap sa'kin?", 1.0),
        ("Hindi na ba ma-mamamayapa?", 0.14),
        ("Hindi na ba ma-mamamayapa?", 0.14),
        ("Hindi na makalaya...", 1.5)
    ]

    # Delay khusus (opsional) jika ingin sinkron seperti musik
    delay = [0.3, 4.8, 9.5, 14.0, 17.3]

    print("\n=== multo - cup of joe - ===\n")

    for indeks, (teks, jeda) in enumerate(lirik):
        ketik_teks(teks, kecepatan=0.09)
        time.sleep(jeda)  # jeda setelah baris
        # Jika ingin memakai delay khusus:
        # time.sleep(delay[indeks])

    print("\n=== KITA BUKANLAH TOKOH UTAMA ===")


if __name__ == "__main__":
    jalanin_lirik()