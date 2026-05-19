from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import A4


def generate_scoring_pdf(
    scoring,
    is_client=False
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    elements = []

    # TITRE
    title = Paragraph(
        "RAPPORT DE SCORING",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 30))

    # CLIENT INFO
    client = scoring.client

    infos = [

        ['Nom', client.nom],

        ['Prénom', client.prenom],

        ['Salaire', f"{client.salaire_mensuel} DA"],

        ['Décision', scoring.decision],
    ]

    # SCORE INTERNE UNIQUEMENT
    if not is_client:

        infos.append([
            'Score',
            str(scoring.score)
        ])

        infos.append([
            'Taux endettement',
            f"{round(scoring.taux_endettement, 2)} %"
        ])

    table = Table(
        infos,
        colWidths=[200, 250]
    )

    table.setStyle(TableStyle([

        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),

        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),

        ('GRID', (0, 0), (-1, -1), 1, colors.black),

        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),

        ('FONTSIZE', (0, 0), (-1, -1), 11),

        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))

    elements.append(table)

    elements.append(Spacer(1, 30))

    footer = Paragraph(
        "Document généré automatiquement par Islamic Finance Platform",
        styles['Italic']
    )

    elements.append(footer)

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf





def generate_simulation_pdf(
    simulation
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "SIMULATION MOURABAHA",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 30))

    client = simulation.client

    data = [

        ['Nom', client.nom],

        ['Prénom', client.prenom],

        ['Prix du bien',
         f"{simulation.prix_bien} DA"],

        ['Apport',
         f"{simulation.apport} DA"],

        ['Montant financé',
         f"{simulation.montant_finance} DA"],

        ['Marge',
         f"{simulation.marge} %"],

        ['Prix final',
         f"{simulation.prix_final} DA"],

        ['Durée',
         f"{simulation.duree_mois} mois"],

        ['Mensualité',
         f"{round(simulation.mensualite, 2)} DA"],
    ]

    table = Table(
        data,
        colWidths=[200, 250]
    )

    table.setStyle(TableStyle([

        ('GRID', (0, 0), (-1, -1), 1, colors.black),

        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),

        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))

    elements.append(table)

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf