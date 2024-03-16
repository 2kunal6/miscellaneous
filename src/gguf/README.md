## Run Instructions
- python3 -m pipenv shell
- phthon3 -m pip install pipenv
- python3 -m pipenv install
- python3 gguf.py
- python3 non_gguf.py


## Comparison
- The following comparison was done on a machine with 64GB memory and 8 cores. 
- Simple prompt instructions to write a python code was provided (see gguf.py and non_gguf.py)

#### Results of the GGUF vs Non-GGUF Comparison:
- CodeLlama-7B-Instruct:
  - Without gguf: >170s 
  - With gguf 10-100 seconds
- CodeLlama-13B-Instruct 
  - Without gguf: Memory usage quickly got to 100% (even with 4 bit quantization) and hence the process was killed.  The CPU util hovered around 102%.
  - With gguf: between 50-200 seconds
- CodeLlama-34B-Instruct
  - Without gguf: Since the 13B model did not work, this is not going to run.
  - With gguf: between 150-500 seconds.  Memory utilization almost remained constant 86% and CPU utilization was around 400%.
