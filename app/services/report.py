from jinja2 import Environment, FileSystemLoader
from app.core.config import settings
from app.core.schemas import TripPlan
import os

class Report:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader(settings.TEMPLATE_DIR))
        self.output_dir = settings.OUTPUT_DIR

    def generate_html(self, plan: TripPlan, template_name: str = "itinerary.html") -> str:
        try:
            template = self.env.get_template(template_name)

        except Exception as e:
            print(f"{template_name}not found, using default...")
            template = self.env.get_template("itinerary.html")

        data = plan.model_dump()
        html_content = template.render(**data)
        safe_title = plan.title.replace(" ", "_")
        filename = f"{safe_title}.html"
        file_path = os.path.join(self.output_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        return f"http://localhost:8000/downloads/{filename}"