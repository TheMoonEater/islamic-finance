VALID_TRANSITIONS = {

    'BROUILLON': [
        'EN_ANALYSE'
    ],

    'EN_ANALYSE': [
        'VALIDATION_EMPLOYE',
        'REFUSE'
    ],

    'VALIDATION_EMPLOYE': [
        'VALIDATION_RETAIL',
        'REFUSE'
    ],

    'VALIDATION_RETAIL': [
        'COMITE',
        'REFUSE'
    ],

    'COMITE': [
        'ACCEPTE',
        'REFUSE'
    ]
}


def can_transition(
    current_status,
    new_status
):

    return (
        new_status
        in VALID_TRANSITIONS.get(
            current_status,
            []
        )
    )