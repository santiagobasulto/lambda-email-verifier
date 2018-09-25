from utils import extract_domain, is_valid_email


def test_extract_domains():
    assert extract_domain('santiago@rmotr.com') == 'rmotr.com'
    assert extract_domain('santiago@rmotr.com.ar') == 'rmotr.com.ar'
    assert extract_domain('santiago+hello@rmotr.com') == 'rmotr.com'
    assert extract_domain('santiago.basulto@rmotr.com') == 'rmotr.com'
    assert extract_domain('santiago.basulto+hhahsdjh@rmotr.com') == 'rmotr.com'
    assert extract_domain('santiago.basulto+hhah--sh@rmotr.com') == 'rmotr.com'

    assert extract_domain('x@gmail.com') == 'gmail.com'
    assert extract_domain('x@localhost') == 'localhost'
    assert extract_domain('x@x.c') == 'x.c'
    assert extract_domain('xasdasd@x.c') == 'x.c'
    assert extract_domain('xasdasd@gmail.c') == 'gmail.c'
    assert extract_domain('"xasdasd"@gmail.com') == 'gmail.com'
    assert extract_domain('"xas @ dasd"@gmail.com') == 'gmail.com'

    assert extract_domain('email@123.123.123.123') == '123.123.123.123'
    assert extract_domain('email@[123.123.123.123]') == '[123.123.123.123]'

    assert extract_domain('123456@rmotr.com') == 'rmotr.com'
    assert extract_domain('________@rmotr.com') == 'rmotr.com'
    assert extract_domain('"123456"@rmotr.com') == 'rmotr.com'


def test_valid_email_addresses():
    assert is_valid_email('santiago@rmotr.com')
    assert is_valid_email('santiago@rmotr.com.ar')
    assert is_valid_email('santiago+test@rmotr.com')

    assert is_valid_email('"santiago"@rmotr.com')
    assert is_valid_email('"santiago+test"@rmotr.com')

    assert is_valid_email('________@rmotr.com')
    assert is_valid_email('123456@rmotr.com')
    assert is_valid_email('"123456"@rmotr.com')

    assert is_valid_email('santiago@ex.co')
    assert is_valid_email('santiago+test@ex.co')

    assert is_valid_email('email@[123.123.123.123]')


def test_invalid_email_addresses():
    assert not is_valid_email('santiago@ex.c')
    assert not is_valid_email('santiago+test@ex.c')

    assert not is_valid_email('santiago@x.c')
    assert not is_valid_email('santiago+test@x.c')

    assert not is_valid_email('s@x.c')
    assert not is_valid_email('s+test@x.c')
