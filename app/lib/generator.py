from transformers import AutoModelForCausalLM,AutoTokenizer,pipeline

class TextGenerator:
    def instruction_prompt(self, instruction, prompt_input=None):
        if prompt_input:
            return f"""
            Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

            ### Instruction:
            {instruction}

            ### Input:
            {prompt_input}

            ### Response:
            """.strip()
        else:
            return f"""
            Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

            ### Instruction:
            {instruction}

            ### Response:
            """.strip()
        
    def __init__(self):
        self.model_name_or_path = "./model"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(
			self.model_name_or_path,
			device_map = 'auto'
		)
        self.text_generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=500
        )
            
    def get_result(self, instruction, prompt):
        return self.text_generator(self.instruction_prompt(instruction, prompt))

