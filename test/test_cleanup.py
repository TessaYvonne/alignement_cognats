from Word import Word
from cleanup import cleanup_pa80
from reconstructions import cleanup_all


def test_cleanup():
    assert (cleanup_all("d-ɔ̀l°° (fskbvs) / m-ɔ̀x") == Word("ɔ̀l", "d-"))
    assert (cleanup_all("d-ɔ̀l°° / m-ɔ̀x") == Word("ɔ̀l", "d-"))
    assert (cleanup_all("d-ɔ̀l°° ") == Word("ɔ̀l", "d-"))
    assert (cleanup_all("ɔ̀l°° ") == Word("ɔ̀l", ""))


def test_cleanup_pa80():
    assert (cleanup_pa80("°(N-)ɟɔ́Kdíbá̀") == Word("°ɟɔ́Kdíbá̀", "(N-)"))
    assert (cleanup_pa80("°-(ò)dómV̀") == Word("°dómV̀", "(ò)"))
    assert (cleanup_pa80("°(N-)bèŋ(Ò)") == Word("°bèŋ(Ò)", "(N-)"))
    assert (cleanup_pa80("d-ɔ̀l°° / m-ɔ̀x") == Word("°ɔ̀l", "d-"))
    assert (cleanup_pa80("d-ɔ̀l°° ") == Word("°ɔ̀l", "d-"))
    assert (cleanup_pa80("ɔ̀l°° ") == Word("°ɔ̀l", ""))
    assert (cleanup_pa80("") == Word("", ""))
