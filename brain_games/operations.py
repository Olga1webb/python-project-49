from random import choice


def generate_operator():
    """Generates random operation"""
    operator = choice('+-*')
    return operator