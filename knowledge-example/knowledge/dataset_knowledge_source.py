# src/dataset_finder/knowledge/dataset_knowledge_source.py
from crewai.knowledge.source.base_knowledge_source import BaseKnowledgeSource
from pydantic import Field
from typing import Dict, Any
import json

class DatasetKnowledgeSource(BaseKnowledgeSource):
    """Production-grade loader that chunks large dataset catalog for CrewAI."""

    file_path: str = Field(description="Path to dataset JSON file")

    def load_content(self) -> Dict[Any, str]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            datasets = data.get("datasets", [])
            chunks = {}

            for ds in datasets:
                ds_id = ds.get("id")
                formatted = self._format(ds)
                if ds_id and formatted:
                    chunks[ds_id] = formatted

            return chunks

        except Exception as e:
            raise ValueError(f"Failed to load JSON: {str(e)}")

    def validate_content(self, content: Any) -> str:
        return str(content)

    def add(self) -> None:
        content = self.load_content()
        for _, chunk in content.items():
            self.chunks.append(chunk)
        self._save_documents()

    def _format(self, ds: dict) -> str:
        schema_cols = ", ".join([col.get("name", "") for col in ds.get("schema", {}).get("columns", [])])
        tags = ", ".join(ds.get("metadata", {}).get("tags", []))
        return f"""
ID: {ds.get("id")}
Name: {ds.get("name")}
Description: {ds.get("description")}
Provider: {ds.get("provider")}
Type: {ds.get("type")}
Tags: {tags}
Quality Score: {ds.get("qualityScore")}
Schema Fields: {schema_cols}
"""
