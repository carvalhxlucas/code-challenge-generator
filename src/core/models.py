from typing import List
from pydantic import BaseModel, Field

class TestCase(BaseModel):
    input_val: str = Field(description="The input value for the test case")
    output_val: str = Field(description="The output value for the test case")
    is_hidden: bool = Field(default=False, description="Whether the test case is hidden")

class Challenge(BaseModel):
    title: str = Field(description="The title of the challenge")
    description: str = Field(description="The description of the challenge")
    test_cases: List[TestCase] = Field(description="The test cases for the challenge")
    solution: str = Field(description="The solution to the challenge")
    difficulty: str = Field(description="The difficulty of the challenge")

    def __str__(self):
        return f"{self.title} ({self.difficulty})"