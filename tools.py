from dotenv import load_dotenv
from livekit.agents import function_tool,RunContext
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool()
async def lookup_important_numbers(
    context: RunContext,  # type: ignore
    query: str="important emergency numbers in Oman"
    ) -> str:
    """
    Searches DuckDuckGo for important emergency and public service numbers in Oman.
    
    Returns a dictionary of services and numbers.
    """
    try:
        important_numbers_oman = """
            Oman Emergency & Important Contact Numbers

            General Emergency (Police / Ambulance / Fire): 9999
            Water Emergency: 1442
            Electricity Emergency / Outage: 80070008
            Domestic Violence Helpline: 80077788
            Child Abuse Hotline: 1100
            Cyber Crime / Internet Fraud: 80077444
            Narcotics / Drug-Related Help: 1444
            Food Hygiene Complaints (Muscat Municipality): 1111
            Pollution Reporting: 80071999

            Mental Health / Suicide Support:
            - "Not Alone" Mental Health Campaign: +968 9935 9779
            - Ministry of Health Mental Health Dept: +968 24 603 552

            Royal Oman Police (ROP) Contacts:
            - ROP HQ (Muscat): +968 24569282
            - Muscat Governorate Police HQ: +968 24648007
            - Salalah Police Station (Dhofar): +968 23290099
            - A’Saadah Police Station, Dhofar: +968 23234170
            - Taqah Police Station, Dhofar: +968 23258199
            """

        results = DuckDuckGoSearchRun().run(tool_input=query)
        print(f"Search results for '{query}': {results}")
        return results,important_numbers_oman
    except Exception as e:
        print(f"Error searching the web for '{query}': {e}")
        return f"An error occurred while searching the web for '{query}'."    
