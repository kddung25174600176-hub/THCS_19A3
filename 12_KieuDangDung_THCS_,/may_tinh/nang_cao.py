def luy_thua(co_so, so_mu):
    ket_qua = 1
    for i in range(so_mu):
        ket_qua = ket_qua * co_so
    return ket_qua


def can_bac_hai(so):
    return so ** 0.5
