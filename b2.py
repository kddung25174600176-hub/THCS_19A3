def giai_phuong_trinh_bac_nhat(a, b) :
    if a == 0 :
        if b == 0 :
            print("phương trình vô nghiệm")
        else:
            print("phương trình vô số nghiệm")
    else:
        x = -b/a 
        print("phương trình có nghiệm x =", x)
giai_phuong_trinh_bac_nhat(-2, 4)
giai_phuong_trinh_bac_nhat(0, 0)
giai_phuong_trinh_bac_nhat(0, 5)

        