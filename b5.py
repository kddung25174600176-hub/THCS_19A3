def kiem_tra_chuoi_doi_xung(n):
    chu_so = str(n)
    return chu_so == chu_so[::-1] 
print(kiem_tra_chuoi_doi_xung(526))
print(kiem_tra_chuoi_doi_xung(515))