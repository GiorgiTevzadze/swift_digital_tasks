from config import settings
import random
from string import ascii_letters, digits


SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)


def code_generator(size=6, chars=ascii_letters + digits):
    return ''.join(random.choices(chars, k=size))


def create_short_code(instance, size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    Shortener = instance.__class__
    while Shortener.objects.filter(short_code=new_code).exists():
        new_code = code_generator(size=size)
    return new_code

