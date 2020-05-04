from typing import TextIO, List, Optional
import random
import json


def load_comp(input_stream: TextIO) -> Optional[List[str]]:
    try:
        return json.load(input_stream)
    except:
        return None


def select_comp(comps: List[str]) -> Optional[str]:
    try:
        return random.sample(comps, 1)[0]
    except:
        return None
