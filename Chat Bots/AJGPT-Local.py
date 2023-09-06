import openai

openai.api_key = ""

messages = [{"role": "system", "content": "Hi! You are AJ GPT, an assistant programmed to respond in a manner similar to AJ Wood. While close to the default, please seek to capture everything contained within."}]


print("Hello!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
