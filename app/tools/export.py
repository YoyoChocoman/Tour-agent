import base64
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
            content = self.report.generate_html(plan)
            b64_html = base64.b64encode(content.encode('utf-8')).decode('utf-8')
            data_uri = f"data:text/html;charset=utf-8;base64,{b64_html}"

            return f'<a href="{data_uri}" download="{plan.title}.html">Click to download</a>'

        except Exception as e:
            return f"Error: {str(e)}"