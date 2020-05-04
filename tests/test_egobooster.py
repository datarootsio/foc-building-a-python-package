import boostmyego.compliment as bc

def test_fetcher():
    assert type(bc.fetch_compliments()) == list
    assert len(bc.fetch_compliments()) > 0

def test_compliment():
    cs = bc.fetch_compliments()
    assert len(bc.give_compliment(cs)) > 0