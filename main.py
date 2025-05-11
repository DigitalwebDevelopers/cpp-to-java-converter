# Import Supporters or Libraries
# --------------------------------------------------------
from ai_credentials import apikey
import re
from google import genai


# program for sending and getting ai model request
# ----------------------------------------------------------
def generate_text(prompt):
    client = genai.Client(api_key=apikey) # using api key here
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response

# Extraction code of java form Block of response
# ----------------------------------------------------------
def extract_javacode(text):
    match = re.search(
        r"```java\s+(.*?)```",
        text,
        re.DOTALL #enables the '.' to match new line characters as well
    )
    if match:
        return match.group(1).strip() + "\n"
    # if no match then,
    return None

# Core Process of Program held Here
# ----------------------------------------------------------
if __name__ == "__main__":
    code = ""
    try:
        with open("main.cpp", 'r') as file:
            code = file.read() # read the entire cpp file
    except FileNotFoundError:
        print("Error: 'main.cpp' not found.")
        exit()

    prompt = "Convert this C++ code into Java code: " + code
    print("Converting C++ to Java...")
    response = generate_text(prompt)

    # collect the java code here
    java_code = extract_javacode(response.text)

    if java_code:
        try:
            with open("main.java", "w") as file:
                file.write(java_code) # write the extracted code into java file
            print("C++ to Java conversion done. Java code saved to 'main.java'")
        except Exception as e:
            print(f"Error writing to 'main.java': {e}")
    else:
        print("No Java code found in the AI response.")
