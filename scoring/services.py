def calcul_taux_endettement(
    salaire,
    charges,
    mensualite,
):
    return ((charges + mensualite) / salaire) * 100


def calcul_score(client, mensualite):

    score = 0

    # salaire
    if client.salaire_mensuel >= 100000:
        score += 30

    elif client.salaire_mensuel >= 60000:
        score += 20

    else:
        score += 10

    # ancienneté
    if client.anciennete_annees >= 5:
        score += 25

    elif client.anciennete_annees >= 2:
        score += 15

    else:
        score += 5

    # contrat
    if client.type_contrat.lower() == "cdi":
        score += 20

    else:
        score += 10

    # situation familiale
    if client.situation_familiale == "MARIE":
        score += 10

    else:
        score += 5

    # endettement
    taux = calcul_taux_endettement(
        client.salaire_mensuel,
        client.charges_mensuelles,
        mensualite
    )

    if taux < 30:
        score += 15

    elif taux < 40:
        score += 10

    else:
        score += 0

    return score, taux


def get_decision(score):

    if score >= 80:
        return "ELIGIBLE"

    elif score >= 60:
        return "A_ANALYSER"

    return "REFUSE"