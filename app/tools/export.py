from app.services.report import Report
from app.core.schemas import TripPlan

class ExportTool:
    def __init__(self):
        self.report = Report()

    def form_itny_link(self, title: str, days: list) -> str:
        try:
            itny_data = {
                "title": title,
                "days": days
            }
            plan = TripPlan(**itny_data)
            data_url = self.report.generate_html(plan)

            return f"Document formed sucessfully at backend. [click to download {title}]({data_url})"

        except Exception as e:
            return f"Error: {str(e)}"