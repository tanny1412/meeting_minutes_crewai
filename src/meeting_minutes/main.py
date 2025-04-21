#!/usr/bin/env python
import sys
print("\n".join(sys.path))



from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start
from pydub import AudioSegment
from pydub.utils import make_chunks
from pathlib import Path
from crews.gmailcrew.gmailcrew import GmailCrew
from dotenv import load_dotenv

load_dotenv()

from crews.meeting_minutes_crew.meeting_minutes_crew import MeetingMinutesCrew

from openai import OpenAI
client = OpenAI()




class MeetingMinutesState(BaseModel):
    transcript: str = ""
    meeting_minutes: str = ""


class MeetingMinutesFlow(Flow[MeetingMinutesState]):

    @start()
    def transcribe_meeting(self):

        print("Generating transcript")
        SCRIPT_DIR = Path(__file__).parent
        audio_path = str(SCRIPT_DIR / "EarningsCall.wav")
        

        # Load the audio file
        audio = AudioSegment.from_file(audio_path, format="wav")
        
        # Define chunk length in milliseconds (e.g., 1 minute = 60,000 ms)
        chunk_length_ms = 60000
        chunks = make_chunks(audio, chunk_length_ms)

        # Transcribe each chunk
        full_transcription = ""
        for i, chunk in enumerate(chunks):
            print(f"Transcribing chunk {i+1}/{len(chunks)}")
            chunk_path = f"chunk_{i}.wav"
            chunk.export(chunk_path, format="wav")
            
            with open(chunk_path, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_file
                )
                full_transcription += transcription.text + " "

        self.state.transcript = full_transcription
        print(f"Transcription: {self.state.transcript}")

    @listen(transcribe_meeting)
    def generate_meeting_minutes(self):

        print("Generating meeting minutes")

        crew=MeetingMinutesCrew()

        inputs = {
            'transcript': self.state.transcript
        }

        meeting_minutes = crew.crew().kickoff(inputs)

        self.state.meeting_minutes = meeting_minutes


    @listen(generate_meeting_minutes)

    def create_draft_meeting_minutes(self):
        print("Creating draft meeting minutes")

        crew = GmailCrew()

        inputs = {
            'body': self.state.meeting_minutes
        }


        draft = crew.crew().kickoff(inputs)

        print(f"Draft: {draft}")

        

    
            

        






def kickoff():
    meeting_minutes_flow = MeetingMinutesFlow()
    meeting_minutes_flow.plot()
    meeting_minutes_flow.kickoff()



if __name__ == "__main__":
    kickoff()
