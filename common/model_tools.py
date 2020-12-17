
def get_n_params(model):
    np = 0
    for p in list(model.parameters()):
        np += p.nelement()
    return np
