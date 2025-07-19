from mongodb_insertion import run as step1
from embeddings_generation import run as step2
from supabase_insertion import run as step3
import schedule
import time

def automation():
    print("Starting Automation Pipeline...")
    step1()
    step2()
    step3()
    print("Automation Pipeline Completed.")

schedule.every(1).hours.do(automation)

while True:
    schedule.run_pending()
    time.sleep(60)