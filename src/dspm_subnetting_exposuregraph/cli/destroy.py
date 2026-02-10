
import shutil, json, datetime
from pathlib import Path

def main():
    out = Path("out")
    if out.exists():
        shutil.rmtree(out)
    receipt = {
        "action":"destroy",
        "timestamp_utc": datetime.datetime.utcnow().isoformat()+"Z",
        "status":"completed"
    }
    with open("destroy_receipt.json","w") as f:
        json.dump(receipt,f,indent=2)
    print("DESTROY complete")

if __name__ == "__main__":
    main()
