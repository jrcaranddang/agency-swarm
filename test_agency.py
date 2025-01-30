from agency_swarm import Agent, Agency, set_openai_key
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI key
set_openai_key(os.getenv("OPENAI_API_KEY"))

# Create a simple CEO agent
ceo = Agent(
    name="CEO",
    description="A test CEO agent for verifying the setup.",
    instructions="You are a helpful CEO agent that responds to basic queries.",
    tools=[],
    model="gpt-3.5-turbo-0125"  # Using GPT-3.5 Turbo with specific version
)

# Create the agency
agency = Agency(
    [ceo],  # CEO will be the entry point for communication with the user
    shared_instructions="This is a test agency for verifying the setup."
)

if __name__ == "__main__":
    # Run the demo in terminal
    agency.run_demo() 