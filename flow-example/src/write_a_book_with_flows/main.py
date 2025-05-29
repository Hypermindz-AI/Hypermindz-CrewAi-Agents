#!/usr/bin/env python
import asyncio
from typing import List

from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

from write_a_book_with_flows.crews.write_book_chapter_crew.write_book_chapter_crew import (
    WriteBookChapterCrew,
)
from write_a_book_with_flows.types import Chapter, ChapterOutline

from write_a_book_with_flows.crews.outline_book_crew.outline_crew import OutlineCrew

inputs = {
    "title": "Crewai Agentic Framework",
    "topic": "crewai framework",
    "goal": "describe how to create agent in crewai framework",
}


class BookState(BaseModel):
    id: str = "1"
    title: str = inputs["title"]
    book: List[Chapter] = []
    book_outline: List[ChapterOutline] = []
    topic: str = inputs["topic"]
    goal: str = inputs["goal"]


class BookFlow(Flow[BookState]):
    initial_state = BookState

    @start()
    def generate_book_outline(self):
        print("Kickoff the Book Outline Crew")
        output = (
            OutlineCrew()
            .crew()
            .kickoff(inputs={"topic": self.state.topic, "goal": self.state.goal})
        )

        chapters = output["chapters"]
        print("Chapters:", chapters)

        self.state.book_outline = chapters
        return chapters

    @listen(generate_book_outline)
    async def write_chapters(self):
        print("Writing First Chapter")

        chapter_outline = self.state.book_outline[0]
        print(f"Writing Chapter: {chapter_outline.title}")
        print(f"Description: {chapter_outline.description}")

        output = (
            WriteBookChapterCrew()
            .crew()
            .kickoff(
                inputs={
                    "goal": self.state.goal,
                    "topic": self.state.topic,
                    "chapter_title": chapter_outline.title,
                    "chapter_description": chapter_outline.description,
                    "book_outline": [
                        chapter.model_dump_json()
                        for chapter in self.state.book_outline
                    ],
                }
            )
        )


def kickoff():
    poem_flow = BookFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = BookFlow()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()
