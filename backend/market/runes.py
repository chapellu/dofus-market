from .database.runes_data import runes, proba, specific_runes


def mean(liste: list) -> float:
    if len(liste) == 0:
        return 0.0
    return sum(liste) / len(liste)


def rune_power(jet: int, percentile: int, poids_unitaire: float) -> float:
    return jet * poids_unitaire * 2 / 3 * (0.9 + percentile * 0.002)


def decoupage_ra(_rune_power: float, rune_name: str) -> tuple[float, float]:
    power_ra = runes[rune_name]["poids_ra"] + 2 * runes[rune_name][
        "poids_pa"] + 4 * runes[rune_name]["poids_ba"]
    _decoupage_ra = _rune_power // power_ra
    rest_ra = _rune_power - _decoupage_ra * runes[rune_name]["poids_ra"]
    return _decoupage_ra, rest_ra


def decoupage_pa(_rune_power: float,
                 rune_name: str) -> tuple[float, float, float, float]:
    power_pa = runes[rune_name]["poids_pa"] + 2 * runes[rune_name]["poids_ba"]
    _decoupage_ra, rest_ra = decoupage_ra(_rune_power, rune_name)
    _decoupage_pa = rest_ra // power_pa
    rest_pa = rest_ra - _decoupage_pa * runes[rune_name]["poids_pa"]
    return _decoupage_ra, rest_ra, _decoupage_pa, rest_pa


def decoupage_ba(_rune_power: float,
                 rune_name: str) -> tuple[float, float, float]:
    power_ba = runes[rune_name]["poids_ba"]
    _decoupage_ra, _, _decoupage_pa, rest_pa = decoupage_pa(
        _rune_power, rune_name)
    return _decoupage_ra, _decoupage_pa, rest_pa // power_ba


def decoupage(jet: int, rune_name: str):
    runes_ba = []
    runes_pa = []
    runes_ra = []

    for percentile in range(0, 101, 20):
        _rune_power = rune_power(jet, percentile,
                                 runes[rune_name]["poids_unitaire"])
        ra, pa, ba = decoupage_ba(_rune_power, rune_name)
        runes_ra.append(ra)
        runes_pa.append(pa)
        runes_ba.append(ba)
    return mean(runes_ra), mean(runes_pa), mean(runes_ba)


def step(jet_min: int, jet_max: int) -> int:
    res = int(0.1 * (jet_max - jet_min))
    return res if res > 0 else 1


def decoupage_special(lvl, rune, jet_max):
    ba = proba[lvl][rune] * 0.01 * jet_max
    return 0, 0, ba


def brisage_rune(lvl: int, jet_min: int, jet_max: int,
                 rune: str) -> tuple[float, float, float]:
    jet_min = max(jet_min, 0)
    jet_max = max(jet_max, 0)
    runes_ba = []
    runes_pa = []
    runes_ra = []

    if rune in specific_runes:
        _, _, ba = decoupage_special(lvl, rune, jet_max)
        runes_ba.append(ba)
    else:
        for jet in range(jet_min, jet_max + 1, step(jet_min, jet_max)):
            ra, pa, ba = decoupage(jet, rune)
            runes_ra.append(ra)
            runes_pa.append(pa)
            runes_ba.append(ba)
    return round(mean(runes_ra), 2), round(mean(runes_pa),
                                           2), round(mean(runes_ba), 2)
