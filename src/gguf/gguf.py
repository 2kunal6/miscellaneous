from ctransformers import AutoModelForCausalLM

import time


text = "write a python code to add 2 numbers"

start_time = time.time()
llm = AutoModelForCausalLM.from_pretrained("TheBloke/CodeLlama-34B-Instruct-GGUF", model_file="codellama-34b-instruct.Q8_0.gguf", model_type="llama", gpu_layers=0)
print(f"Time taken to load model with GGUF: {time.time() - start_time} seconds")



for i in range(10):
    text = f"write a python code to add {i} numbers"
    start_time = time.time()
    print(llm(text))
    print(f"Time taken to infer model with GGUF: {time.time() - start_time} seconds")
