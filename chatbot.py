from transformers import AutoTokenizer, AutoModelForSeq2SeqLM



model_name = "facebook/blenderbot-400M-distill"



model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


conversation_history = []


while True:

    history_string = "\n".join(conversation_history)

    input_text = input("You: ")

    inputs = tokenizer(history_string + input_text, return_tensors="pt", max_length=128, truncation=True)

    tokenizer.pretrained_vocab_files_map

    outputs = model.generate(**inputs)


    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    print("Bot:", response)

    conversation_history.append(input_text)
    conversation_history.append(response)

    if len(conversation_history) > 12:
        conversation_history = conversation_history[-12:]



