import yaml
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
import streamlit as st
from src.builders.module_builder import ModuleBuilder
from src.variables import Variables

class PageSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    name = fields.Str(required=False, load_default='AI Service')
    description = fields.Str(required=False, load_default='')
    author = fields.List(fields.Str(required=False, load_default=''))
    version = fields.Str(required=False, load_default='')
    tags = fields.List(fields.Str(), required=False, load_default=[])
    craft = fields.List(fields.Dict(), required=True)


class PageBuilder:
    def __init__(self, yaml_path: str):
        self.page = PageSchema().load(self._load_yaml(yaml_path))

    @staticmethod
    def _load_yaml(yaml_path: str):
        with open(yaml_path, "r") as stream:
            return yaml.safe_load(stream)

    def build(self):
        variables = Variables()
        variables.clear()

        st.set_page_config(
            page_title=self.page['name'],
            menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"
            }
        )

        st.title(self.page['name'])
        st.markdown(self.page['description'])
        st.markdown(f"**Author**: {', '.join(self.page['author'])}")
        st.markdown(f"**Version**: {self.page['version']}")
        st.markdown(f"**Tags**: {', '.join(self.page['tags'])}")
        st.markdown('---')
        for craft in self.page['craft']:
            ModuleBuilder(craft, variables).build()