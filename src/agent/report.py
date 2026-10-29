"""Сборка отчёта по скважине: факт, прогноз, рабочая точка."""


def build_report(server, well_id: str, horizon_months: int = 12) -> dict:
    """Один отчёт из трёх вызовов MCP. У каждого числа — единица и источник."""
    # TODO B: перенесите сюда код из ячеек выше: история, прогноз, узловой анализ
    # TODO B: верните словарь той же структуры, что report
    history = server.call("get_production_history", well_id=well_id, months=24)

    forecast = server.call("forecast_production", well_id=well_id, horizon_months=horizon_months)

    opened = server.call("open_well_model", well_id=well_id)

    nodal = server.call("run_nodal_analysis", session_id=opened["session_id"])

    report = {
        "fact": {
            "date": history["points"][-1]["date"],
            "q_m3_day": history["points"][-1]["q_m3_day"],
            "unit": history["units"]["q_m3_day"],
            "source": "get_production_history"
        },
        "forecast": {
            "first_date": forecast["points"][0]["date"],
            "first_q_m3_day": forecast["points"][0]["q_m3_day"],
            "last_date": forecast["points"][-1]["date"],
            "last_q_m3_day": forecast["points"][-1]["q_m3_day"],
            "q_unit": forecast["units"]["q_m3_day"],

            "annual_decline": forecast["fit"]["annual_decline"],
            "annual_decline_unit": forecast["units"]["annual_decline"],

            "r2": forecast["fit"]["r2"],
            "r2_unit": "dimensionless",

            "source": "forecast_production"
        },
        "operating_point": {
            "q_m3_day": nodal["operating_point"]["q_m3_day"],
            "q_unit": nodal["units"]["q_m3_day"],

            "pwf_bar": nodal["operating_point"]["pwf_bar"],
            "pwf_unit": nodal["units"]["pwf_bar"],

            "source": "run_nodal_analysis"
        }
    }
    return report