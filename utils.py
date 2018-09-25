import validators


def extract_domain(email):
    domain = email.rsplit('@', 1)
    if len(domain) > 1:
        return domain[1]


def is_valid_email(email):
    return validators.email(email)
