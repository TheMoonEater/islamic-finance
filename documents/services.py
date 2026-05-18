from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_scoring_pdf(scoring):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Rapport de Scoring",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    client_info = Paragraph(
        f"""
        Client : {scoring.client.nom}
        {scoring.client.prenom}
        """,
        styles['BodyText']
    )

    elements.append(client_info)

    elements.append(Spacer(1, 10))

    score = Paragraph(
        f"Score : {scoring.score}",
        styles['BodyText']
    )

    elements.append(score)

    taux = Paragraph(
        f"""
        Taux d'endettement :
        {round(scoring.taux_endettement, 2)} %
        """,
        styles['BodyText']
    )

    elements.append(taux)

    decision = Paragraph(
        f"Décision : {scoring.decision}",
        styles['BodyText']
    )

    elements.append(decision)

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf






def generate_simulation_pdf(
    simulation
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Simulation Mourabaha",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    fields = [

        f"Prix du bien : {simulation.prix_bien}",

        f"Apport : {simulation.apport}",

        f"""
        Montant financé :
        {simulation.montant_finance}
        """,

        f"Marge : {simulation.marge} %",

        f"Prix final : {simulation.prix_final}",

        f"""
        Durée :
        {simulation.duree_mois} mois
        """,

        f"""
        Mensualité :
        {round(simulation.mensualite, 2)}
        """
    ]

    for field in fields:

        p = Paragraph(
            field,
            styles['BodyText']
        )

        elements.append(p)

        elements.append(Spacer(1, 10))

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf