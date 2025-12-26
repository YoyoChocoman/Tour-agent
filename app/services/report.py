from jinja2 import Environment, FileSystemLoader
from app.core.config import settings
from app.core.schemas import TripPlan

class ReportService:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader(settings.TEMPLATE_DIR))

    def generate_html(self, plan: TripPlan, template_name: str = "itinerary.html") -> str:
        try:
            template = self.env.get_template(template_name)

        except Exception as e:
            print(f"{template_name}not found, using default...")
            template = self.env.get_template("itinerary.html")

        data = plan.model_dump()
        return template.render(**data)