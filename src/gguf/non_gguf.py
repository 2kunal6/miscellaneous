from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

import time
import torch



start_time = time.time()
quantization_config = BitsAndBytesConfig(
   load_in_4bit=True,
   bnb_4bit_compute_dtype=torch.float16
)
model_id = 'codellama/CodeLlama-13b-Instruct-hf'
tokenizer = AutoTokenizer.from_pretrained(model_id, quantization_config=quantization_config,)
model = AutoModelForCausalLM.from_pretrained(model_id)
print(f"Time taken to load model without GGUF: {time.time() - start_time} seconds")



for i in range(10):
    text = f"write a python code to add {i} numbers"
    start_time = time.time()
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    generated_ids = model.generate(input_ids, max_length=128)
    print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
    print(f"Time taken to infer model without GGUF: {time.time() - start_time} seconds")
