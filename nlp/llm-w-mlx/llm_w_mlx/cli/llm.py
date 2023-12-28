import argparse

from llm_w_mlx.model import LLM
from personalities import personalities


def parse_args():
    # Create the parser
    parser = argparse.ArgumentParser(description="LLM chat arguments")

    parser.add_argument(
        "--personality",
        default="dwight",
        type=str,
        choices=list(personalities.keys()),
    )

    parser.add_argument(
        "--model",
        default="Mistral-7B-Instruct-v0.1",
        required=False,
        type=str,
        help="Model name."
    )

    parser.add_argument(
        "--weights",
        required=True,
        type=str,
        help="Mistral weights path (npz file)."
    )

    parser.add_argument(
        "--tokenizer",
        required=True,
        type=str,
        help="Mistral tokenizer path (model file)."
    )

    parser.add_argument(
        "--max_tokens",
        default=500,
        type=int,
        help="Max tokens for the chat."
    )

    # Parse the arguments
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_args()

    print(f"> LLM with personality: {args.personality.upper()}")

    llm = LLM.build(
        model_name=args.model,
        weights_path=args.weights,
        tokenizer_path=args.tokenizer,
        personality=personalities[args.personality]["personality"],
        examples=personalities[args.personality]["examples"],
    )

    llm.chat(max_tokens=args.max_tokens)