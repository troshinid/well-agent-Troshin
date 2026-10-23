"""tools."""
import math


def ipr_vogel(p_res: float, p_test: float, q_test: float, p_wf: float) -> float:
    """Дебит по Вогелю, м3/сут. Давления абсолютные, атм."""
    # TODO B: перенесите сюда рабочий код занятия 3 вместе с проверкой диапазонов
    if not (
        p_res > 0
        and 0 <= p_test < p_res
        and 0 <= p_wf <= p_res
        and q_test >= 0
    ):
        raise ValueError(
            "Некорректные параметры: проверьте p_res > 0, "
            "0 <= p_test < p_res, 0 <= p_wf <= p_res, q_test >= 0"
        )

    x_test = p_test / p_res
    denom = 1 - 0.2 * x_test - 0.8 * x_test**2
    q_max = q_test / denom

    x_wf = p_wf / p_res
    q_wf = q_max * (1 - 0.2 * x_wf - 0.8 * x_wf**2)
    return q_wf


def arps_decline(q0: float, annual_decline: float, years: float) -> float:
    """Экспоненциальный спад дебита, м3/сут."""
    # TODO B: перенесите сюда рабочий код занятия 3
    if not (q0 > 0 and annual_decline >= 0 and years >= 0):
        raise ValueError(
            "Некорректные параметры: требуется q0 > 0, D >= 0, t >= 0"
        )

    return q0 * math.exp(-annual_decline * years)