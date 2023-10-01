import openai
import constants

openai.api_key = constants.OPENAI_API_KEY
# You can change the model engine with whatever you want check chatgpt docs
model_engine = "text-davinci-003"

def get_response(prompt) -> str:
    completion = openai.Completion.create(engine=model_engine,
                                        prompt=prompt,
                                        max_tokens=1024,
                                        n=1,
                                        stop=None,
                                        temperature=0.7)
    res=""
    for choice in completion.choices:
        res += choice.text
        print(f"Response: %s" % choice.text)
    return res