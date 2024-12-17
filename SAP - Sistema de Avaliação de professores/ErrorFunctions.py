def TamanhoError(SenhaUser):
    if len(SenhaUser) < 8:
        print ("Coloque uma senha com no mínimo 8 caracteres!")
        raise OverflowError