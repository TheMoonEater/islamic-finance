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


TVA = 0.19


def calcul_salaire_total(
    salaire_acheteur,
    salaire_co_acheteur
):
    return (
        salaire_acheteur
        + salaire_co_acheteur
    )


def calcul_ce_brute(
    salaire_total
):
    return salaire_total * 0.30


def calcul_ce_nette(
    ce_brute,
    credit_consomme
):
    return ce_brute - credit_consomme


def calcul_apport_minimum(
    prix_bien,
    ce_nette,
    duree_mois
):
    return max(
        prix_bien -
        (ce_nette * duree_mois),
        0
    )


def calcul_total_marge(
    montant_finance,
    taux_marge
):
    return (
        montant_finance
        * (taux_marge / 100)
    )


def calcul_total_tva(
    total_marge
):
    return total_marge * TVA