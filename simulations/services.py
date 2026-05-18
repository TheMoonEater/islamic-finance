def calcul_montant_finance(
    prix_bien,
    apport
):
    return prix_bien - apport


def calcul_prix_final(
    montant_finance,
    marge
):
    return montant_finance + (
        montant_finance * (marge / 100)
    )


def calcul_mensualite(
    prix_final,
    duree_mois
):
    return prix_final / duree_mois