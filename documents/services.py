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

    client = scoring.client

    # =====================
    # ENTETE
    # =====================

    title = Paragraph(
        "DOSSIER CLIENT",
        styles["Title"]
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Plateforme de Finance Islamique",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # =====================
    # IDENTITE CLIENT
    # =====================

    elements.append(
        Paragraph(
            "Informations Client",
            styles["Heading2"]
        )
    )

    data = [

        ["Nom", client.nom],

        ["Prénom", client.prenom],

        ["Email", client.email],

        ["Téléphone", client.telephone],

        ["Adresse", client.adresse],

        ["Situation familiale",
         client.situation_familiale],

        ["Personnes à charge",
         str(client.nombre_personnes_charge)],
    ]

    table = Table(
        data,
        colWidths=[180, 300]
    )

    table.setStyle(TableStyle([

        ('GRID', (0,0), (-1,-1), 1, colors.black),

        ('BACKGROUND', (0,0), (0,-1),
         colors.lightgrey),

        ('FONTNAME', (0,0), (-1,-1),
         'Helvetica'),

    ]))

    elements.append(table)

    elements.append(
        Spacer(1, 20)
    )

    # =====================
    # PROFESSIONNEL
    # =====================

    elements.append(
        Paragraph(
            "Situation Professionnelle",
            styles["Heading2"]
        )
    )

    data = [

        ["Secteur",
         client.secteur_activite],

        ["Contrat",
         client.type_contrat],

        ["Ancienneté",
         f"{client.anciennete_annees} ans"],

        ["Salaire",
         f"{client.salaire_mensuel} DA"],
    ]

    table = Table(
        data,
        colWidths=[180,300]
    )

    table.setStyle(TableStyle([

        ('GRID', (0,0), (-1,-1), 1,
         colors.black),

        ('BACKGROUND', (0,0), (0,-1),
         colors.lightgrey),

    ]))

    elements.append(table)

    elements.append(
        Spacer(1,20)
    )

    # =====================
    # SCORING
    # =====================

    elements.append(
        Paragraph(
            "Résultat Scoring",
            styles["Heading2"]
        )
    )

    scoring_data = [

        ["Décision",
         scoring.decision],
    ]

    if not is_client:

        scoring_data.extend([

            ["Score",
             str(scoring.score)],

            ["Taux d'endettement",
             f"{round(scoring.taux_endettement,2)} %"]

        ])

    table = Table(
        scoring_data,
        colWidths=[180,300]
    )

    table.setStyle(TableStyle([

        ('GRID', (0,0), (-1,-1), 1,
         colors.black),

        ('BACKGROUND', (0,0), (0,-1),
         colors.lightgrey),

    ]))

    elements.append(table)

    elements.append(
        Spacer(1,30)
    )

    footer = Paragraph(
        "Document généré automatiquement par Islamic Finance Platform",
        styles["Italic"]
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