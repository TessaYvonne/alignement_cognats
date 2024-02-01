from reconstructions import cleanup_all


def test_cleanup():
    assert(cleanup_all("d-ɔ̀l°° (fskbvs) / m-ɔ̀l") == "ɔ̀l")


def test_it():
    assert(cleanup_all(", bòǎ̰") == "test")