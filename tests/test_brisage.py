import pytest
from src.runes import brisage_rune


@pytest.mark.parametrize("lvl, jet_min, jet_max, rune, result",
                         [(128, 100, 120, "Vi", (0.0, 2.38, 7.05)),
                          (128, 30, 40, "Ine", (0.89, 2.38, 6.80)),
                          (128, 21, 30, "Sa", (0.1, 2.7, 7.43)),
                          (128, 7, 10, "Ré Terre", (0, 0.75, 2.96)),
                          (128, 7, 10, "Ré Feu", (0, 0.75, 2.96)),
                          (128, 1, 2, "Cri", (0, 0, 0.5)),
                          (128, 4, 6, "Do Feu", (0, 0, 2.83)),
                          (128, 4, 6, "So", (0, 0, 2.83)),
                          (128, 11, 15, "Prospe", (0, 1.13, 4.8)),
                          (128, 1, 1, "Ga Pa", (0, 0, 0.67))])
def test_brisage(lvl, jet_min, jet_max, rune, result):
    assert brisage_rune(lvl, jet_min, jet_max, rune) == result
