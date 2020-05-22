# PR ke 2

# SOAL 1
# ----- 0 +++++ 5 ----- 8 +++++ 11 ------

inputUser = float(input("1) Masukkan angka:"))

# ----- 0 +++++
LebihDari_0 = (inputUser > 0)
print("Lebih dari 0 :", LebihDari_0)

# +++++ 5 -----
KurangDari_5 = (inputUser < 5)
print("Kurang dari 5 :", KurangDari_5)

# ----- 8 +++++
LebihDari_8 = (inputUser > 8)
print("Lebih dari 8 :", LebihDari_8)

# +++++ 11 -----
KurangDari_11 = (inputUser < 11)
print("Kurang dari 11 :", KurangDari_11)

Correct1 = (LebihDari_0 and KurangDari_5) or (LebihDari_8 and KurangDari_11)
print("Jawaban anda adalah:", Correct1)

# SOAL 2
# +++++ 0 ----- 5 +++++ 8 ----- 11 +++++

inputUser = float(input("2) Masukkan angka:"))

# +++++ 0 -----
KurangDari_0 = (inputUser < 0)
print("Kurang dari 0 :", KurangDari_0)

# ----- 5 +++++
LebihDari_5 = (inputUser > 5)
print("Lebih dari 5 :", LebihDari_5)

# +++++ 8 -----
KurangDari_8 = (inputUser < 8)
print("Kurang dari 8 :", KurangDari_8)

# ----- 11 +++++
LebihDari_11 = (inputUser > 11)
print("Lebih dari 11 :", LebihDari_11)

Correct2 = (KurangDari_0 or LebihDari_5) and (KurangDari_8 or LebihDari_11)
print("Jawaban anda adalah:", Correct2)