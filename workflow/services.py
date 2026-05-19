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








ROLE_TRANSITIONS = {

    'EMPLOYE': [
        'EN_ANALYSE'
    ],

    'RETAIL': [
        'VALIDATION_RETAIL'
    ],

    'RISQUE': [
        'COMITE'
    ],

    'COMITE': [
        'ACCEPTE',
        'REFUSE'
    ],

    'ADMIN': [
        'EN_ANALYSE',
        'VALIDATION_RETAIL',
        'COMITE',
        'ACCEPTE',
        'REFUSE'
    ]
}


def can_validate(
    user_role,
    new_status
):

    return (
        new_status
        in ROLE_TRANSITIONS.get(
            user_role,
            []
        )
    )