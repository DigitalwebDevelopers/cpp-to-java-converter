from ai_credentials import api_key # Import the API key from a separate credentials file
from google import genai
import re

def generate_text(prompt):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # Specify the desired AI model
        contents=prompt,  # Pass the prompt that asks the AI to convert code
    )
    return response

def extract_java_code_flexible(text):
    match = re.search(
        r"(import java.*?public static void main(.*?{.*?}.*?)\n})",  # Regex pattern
        text,
        re.DOTALL,  # Enables the '.' to match newline characters as well
    )

    # If a match is found, return the Java code block
    if match:
        return match.group(1).strip() + "\n}"

    # If no match is found, return None
    return None

if __name__ == "__main__":
    code = """"""
    with open("main.cpp", "r") as file:
        code = file.read()  # Read the entire content of the file
        file.close()  # Close the file explicitly (optional with 'with' block)

    prompt = "convert this cpp code into java code: " + code
    print("converting cpp to java...")
    response = generate_text(prompt)
    java_code = extract_java_code_flexible(response.text)
    with open("main.java", "w") as file:
        file.write(java_code)  # Write the extracted Java code to the file
        file.close()  # Close the file to ensure the content is saved properly

    print("cpp to java conversion done!")  # Print a success message