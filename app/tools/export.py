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

            return f"""
<div style="margin-top: 10px; padding: 15px; background-color: #e3f2fd; border-radius: 8px; border: 1px solid #90caf9;">
    <h3>itinerary complete!</h3>
    <p>Your「{plan.title}」is ready.</p>
    <a href="{data_uri}" download="{plan.title}.html" style="display: inline-block; background-color: #1976d2; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">
        click to download
    </a>
</div>
            """

        except Exception as e:
            return f"Error: {str(e)}"