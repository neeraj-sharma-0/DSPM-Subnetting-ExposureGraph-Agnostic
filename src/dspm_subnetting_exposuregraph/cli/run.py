
import json, os
from pathlib import Path
import pandas as pd

def main():
    Path("out").mkdir(exist_ok=True)
    pd.DataFrame({"status":["created"]}).to_csv("out/scores_assets.csv", index=False)
    with open("out/exposure_graph.json","w") as f:
        json.dump({"graph":"created"}, f)
    print("CREATE complete")

if __name__ == "__main__":
    main()
