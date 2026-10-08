

import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
from insight_crew.crew import Researh_and_Insight_agent



def run():
    """
    Run the crew.
    """
    print("\n======================================")
    print("   AI Research & Insight System")
    print("======================================\n")

    while True:

        user_topic = input("Enter Your Topic : ")

        if user_topic.lower() in ["exit","end","quit"]:
            print("Thank You !")
            break

        inputs = {
            "topic" : user_topic
        }


        try:
            result = Researh_and_Insight_agent().crew().kickoff(
                inputs=inputs
            )

            print("\n======================================")
            print("           FINAL REPORT")
            print("======================================\n")

            print(result)

        except Exception as e:
                print("\n❌ Error occurred:")
                print(e)
                import traceback
                traceback.print_exc()



    