def get_client_financial_data(client):
    return {
        "salaire": client.salaire_mensuel,
        "charges": client.charges_mensuelles,
        "credits": client.credits_en_cours,
        "anciennete": client.anciennete_annees,
        "situation": client.situation_familiale,
    }