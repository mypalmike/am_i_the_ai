from pathlib import Path

from llama_cpp import Llama

SYSTEM = """
You will be told stories about sitations where the person asking is unclear whether they were wrong for behaving the way they acted.
You should respond with a short paragraph.
The first sentence should always be 'NTA' if the person was right for behaving the way they did, 'YTA' if they were wrong, 'ESH' if everyone in the story behaved badly, or 'NAH' if everyone behaved reasonably well.
You should prefer NTA, YTA, or ESH over NAH. Only use NAH if you are confident that everyone behaved reasonably well.
You may not use the word 'asshole' or other offensive language directly in the response.
"""

DEFAULT_MODEL_PATH = str(Path.home() / "aimodels/mistral-7b-instruct-v0.2.Q5_K_M.gguf")


# MODEL = "Mistral Instruct" #  "mistral-7b-openorca.Q4_0.gguf"

class Llm:
    def __init__(self, model_path=DEFAULT_MODEL_PATH):
        self.llm = Llama(model_path=model_path, chat_format="chatml", n_ctx=8192)

    def respond(self, prompt):
        response = self.llm.create_chat_completion(
            messages=[
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": prompt},
            ],
            response_format={
                "type": "json_object",
            },
           temperature=0.7,
        )
        return response
